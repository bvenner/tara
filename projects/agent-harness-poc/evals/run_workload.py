"""M6 CLI — run a committed workload manifest through a registered adapter.

Adapter map and semantics live in grounded.workloads. Offline adapters:
static-baseline (recorded opencode artifact), mechanical-probe (M3a;
LLM-free but needs plumbing binaries). Cached live adapters: pydantic-agent,
pydantic-agent-fanout. plumb-* adapters are the M7 stubs.

Usage:
    uv run python projects/agent-harness-poc/evals/run_workload.py \
        --workload <id> --adapter <name> [--refresh] [--out report.json]
"""
import asyncio
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from grounded.workloads import load_manifest, run_workload_full  # noqa: E402


def main() -> int:
    import argparse
    import json

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workload", required=True)
    parser.add_argument("--adapter", required=True)
    parser.add_argument("--refresh", action="store_true", help="bypass agent-output cache")
    parser.add_argument("--judge", action="store_true", help="add claim-entailment judging (LLM, cached)")
    parser.add_argument("--out", type=Path, default=None)
    args = parser.parse_args()

    m = load_manifest(args.workload)
    os.environ.setdefault("PYDANTIC_AI_NO_BANNER", "1")
    try:
        report = asyncio.run(run_workload_full(m, args.adapter, refresh=args.refresh, judge=args.judge))
    except NotImplementedError as exc:
        print(f"SKIP   {args.workload}/{args.adapter}: {exc}", file=sys.stderr)
        return 3
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(json.dumps(report, indent=2, default=str))
        print(f"written: {args.out}")
    print(json.dumps(report, indent=2, default=str))
    return 0


if __name__ == "__main__":
    sys.exit(main())
