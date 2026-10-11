"""M1 grounded research agent — Pydantic AI over typed repository tools.

Builds the agent and runs the acceptance question. The agent may only use the
grounded tools (knowledge_trace / knowledge_query / knowledge_evidence /
knowledge_trace_report); grounding discipline is:

- Cite every claim as `doc :: section` from tool outputs.
- Never assert content beyond what the trace/query returned.

Usage:
    uv run python projects/agent-harness-poc/run_grounded.py [question] [--out PATH]
"""

from __future__ import annotations

import os
import json
import sys
from pathlib import Path

import dotenv
from pydantic import BaseModel, Field
from pydantic_ai import Agent
from pydantic_ai.exceptions import ModelHTTPError

from grounded import tools

THAR_DIR = Path(__file__).resolve().parents[2]
dotenv.load_dotenv(THAR_DIR / ".env")

MODEL = os.environ.get("AGENT_MODEL", "google:gemini-3.5-flash-lite")

ACCEPTANCE_QUESTION = (
    "How does the tau->0 relaxation limit relate to the SK condition for "
    "gravitation convergence?"
)

INSTRUCTIONS = """\
You are the research agent of the RET x TSSI knowledge repository. Ground every
answer in the repository, never in unverified recollection.

Grounding discipline (-binding):
1. For a substantive question, choose 2-5 seed concepts from its terminology
   (short, distinct phrases, e.g. "tau_J", "sk condition", "subcharacteristic").
2. Call knowledge_trace(topic, concepts, min_seeds=3); if it returns no hits,
   lower min_seeds to 2, then consult knowledge_query per concept.
3. Every factual claim MUST cite `doc :: section` exactly from trace/query
   output fields (e.g. `ret-tssi/program/research-program.md :: 4 Track A`).
4. NEVER assert content beyond what the cited sections returned. If the
   repository does not support a part of the answer, say so explicitly.
5. Note: "entropy" in this program means convex Lyapunov structure, not
   thermodynamic entropy.
"""

CLAIM = """\
# Claim format

- `statement`: one atomic assertion.
- `source`: the citation `doc :: section` from a trace/query hit.
- `trace_edge_ids`: the hyperedge ids (if any) grounding the statement.
"""


class Claim(BaseModel):
    statement: str
    source: str = Field(description="citation in the form `doc :: section`")
    trace_edge_ids: list[str] = Field(default_factory=list)


class GroundedAnswer(BaseModel):
    question: str
    synthesis: str = Field(
        description="the overall answer, a few paragraphs, each assertion traceable to claims"
    )
    claims: list[Claim]


def build_agent() -> Agent[GroundedAnswer]:
    return Agent(
        MODEL,
        instructions=INSTRUCTIONS + CLAIM,
        output_type=GroundedAnswer,
        retries=3,
        tools=[
            tools.knowledge_trace,
            tools.knowledge_query,
            tools.knowledge_evidence,
            tools.knowledge_trace_report,
        ],
    )


def run_with_retry(agent: Agent[GroundedAnswer], question: str, attempts: int = 5):
    """Free-tier capacity hiccups (503 UNAVAILABLE) are transient; back off and retry."""
    import time

    last_exc = None
    for attempt in range(1, attempts + 1):
        try:
            return agent.run_sync(question)
        except ModelHTTPError as exc:
            last_exc = exc
            if exc.status_code not in (429, 500, 503):
                raise
            wait = min(15 * attempt, 60)
            print(f"[retry {attempt}/{attempts}] {exc.status_code}; wait {wait}s", file=sys.stderr)
            time.sleep(wait)
    raise last_exc


def dump_tool_outputs(result, sidecar: Path) -> None:
    """Persist every tool return (LLM-free grounding evidence) next to the run output."""
    from pydantic_ai.messages import ModelRequest, ToolReturnPart

    recs = []
    for msg in result.all_messages():
        if isinstance(msg, ModelRequest):
            for part in msg.parts:
                if isinstance(part, ToolReturnPart):
                    content = part.content
                    recs.append(
                        {
                            "tool": part.tool_name,
                            "content": content.model_dump() if hasattr(content, "model_dump") else content,
                        }
                    )
    sidecar.write_text(json.dumps(recs, indent=2, default=str))


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("question", nargs="?", default=ACCEPTANCE_QUESTION)
    parser.add_argument("--out", type=Path, default=None)
    args = parser.parse_args()

    os.environ.setdefault("PYDANTIC_AI_NO_BANNER", "1")
    agent = build_agent()
    result = run_with_retry(agent, args.question)
    answer = result.output
    if args.out:
        args.out.write_text(_render(answer), encoding="utf-8")
        dump_tool_outputs(result, args.out.with_suffix(".tools.json"))
        print(f"written: {args.out}")
    print(_render(answer))


def _render(answer: GroundedAnswer) -> str:
    claims = "\n".join(
        f"- {c.source}: {c.statement}"
        + (f" (edges: {', '.join(c.trace_edge_ids)})" if c.trace_edge_ids else "")
        for c in answer.claims
    )
    return (
        f"# Grounded answer\n\n## Question\n\n{answer.question}\n\n"
        f"## Synthesis\n\n{answer.synthesis}\n\n## Claims\n\n{claims}\n\n"
        "## Grounding discipline\n\n"
        "Every claim cites a section returned by the hypergraph trace; no "
        "assertion goes beyond trace/query output.\n"
    )


if __name__ == "__main__":
    main()
