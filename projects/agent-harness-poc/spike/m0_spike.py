"""M0 spike — identity pipeline through the persevere.plumbing pydantic adapter.

Runs the two upstream integration modes with the Nix-built plumb binary
(the PyPI wheel's bundled binary needs libsodium.so.23, absent from this
system's Nix store):

1. Bare API: pb.call_sync(spec, msg, binary=...) -> echoed output.
2. Model mode: PlumbingModel(spec, binary=...) wrapped in a Pydantic AI
   Agent, stateful multi-turn via message_history (upstream eval.py shape).

No API key needed (identity pipeline plays the "model").

Usage: uv run python projects/agent-harness-poc/spike/m0_spike.py
"""

from pathlib import Path
import os

import persevere.plumbing as pb
from persevere.plumbing.provider import PlumbingModel

PLUMB_BIN = os.environ.get(
    "PLUMB_BIN",
    str(Path.home() / "tools/plumbing/_build/default/bin/plumb/main.exe"),
)
SPEC = Path.home() / "tools/plumbing/examples/pydantic/pipeline.plumb"


def bare_api() -> None:
    results = pb.call_sync(SPEC, "hello from bare API", binary=PLUMB_BIN)
    for result in results:
        print(f"bare   : {result}")


async def model_mode() -> None:
    from pydantic_ai import Agent

    async with PlumbingModel(SPEC, binary=PLUMB_BIN) as model:
        agent = Agent(model)
        result1 = await agent.run("hello")
        print(f"model 1: {result1.output}")
        result2 = await agent.run("world", message_history=result1.all_messages())
        print(f"model 2: {result2.output}")
        print(f"model name: {model.model_name}")


if __name__ == "__main__":
    bare_api()
    import asyncio

    asyncio.run(model_mode())
    print("M0 spike: all checks passed")
