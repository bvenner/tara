# Plumbing — environment setup & smoke test

Status: working (2026-08-23). Used for Phase A Step 2 (typed pipelines over the hypergraph; `plumb-mcp` exposure to opencode).

## What plumbing provides here

A small language + runtime where a research workflow is an explicit, type-checked graph of processes (agents, tools, programs) moving JSON across channel boundaries. Pipelines are text (`.plumb`), compose, and check shapes at load time.

## Installation — the path that works: Nix source build

The prebuilt wheels do **not** work:

- `pip install persevere-plumbing` (1.1.0) installs bindings + binaries, but the bundled `libzmq` needs `libnorm.so.1` / `libpgm-5.3.so.0` (not bundled, not in the store) and a `libsodium.so.23` (bundled is `.so.26`). Runtime fails: `error while loading shared libraries: ...`.

Working build (supported path from the README):

```bash
# nix available: nix 2.34.7 on this host
mkdir -p ~/tools && cd ~/tools
git clone --depth 1 https://github.com/quantumsoftwarelab/plumbing.git
cd plumbing
nix develop -c dune build      # ~ a few minutes, pulls OCaml toolchain from cache.nixos.org
```

Built executables (each is a directory containing `main.exe`):

```
_build/default/bin/{plumb,check,render,mcp,chat,agent,desugar,peg}/main.exe
```

## Usage

```bash
cd ~/tools/plumbing
# Run a pipeline from a JSON stream on stdin
printf '"hello"' | nix develop -c ./_build/default/bin/plumb/main.exe examples/pydantic/pipeline.plumb

# Type-check at load time
nix develop -c ./_build/default/bin/check/main.exe  /tmp/smoke_map.plumb
# render the architecture as a graph (dot)
nix develop -c ./_build/default/bin/render/main.exe /tmp/smoke_map.plumb

# MCP bridge (exposes pipelines as MCP tools to opencode)
nix develop -c ./_build/default/bin/mcp/main.exe --docroot <pipelines-dir>
```

Telemetry goes to stderr; payloads come out on stdout.

## Smoke-test transcript (all passed)

1. **E2E run** — identity pipeline: `"hello"` in → `"hello"` out, exit 0.
2. **Type-check** — `check` reports `ok (1 types, 2 bindings)` on a typed pipeline.
3. **Typed transform** —
   ```plumb
   type Point = { x: number }
   let double_x : !Point -> !Point = map({x: x * 2})
   let main : !Point -> !Point = plumb(input, output) { spawn double_x(input, output) }
   ```
   `{"x":5}` → `{"x":10.0}`, `{"x":21}` → `{"x":42.0}`.
4. **Boundary validation** — feeding `"oops"` into a `!Point` channel → `input_type_mismatch` (`expected object`), morphism refused before touching the process. This is the load-time/type-shape check working as designed.
5. **Render** — produces a read-only `digraph` of the pipeline (architecture as the program).

## Notes / gotchas

- `map(expr)` uses plumbing's own expression language: `map({x: x * 2})` references input record fields by name (`{set_temp: heat}` in `examples/heat/heat.plumb`); a bare `map(value*2)` on a scalar does not type-check.
- Pipelines are plain text → they port if plumbing is later swapped (see `knowledge-repository-proposal.md`, decision 1: AGPL accepted now; future: strongly-typed host language with multi-party session types).
- The `persevere.plumbing` Python bindings import fine but resolve to the broken bundled binaries; rely on the CLI binaries from the Nix build for Step 2.