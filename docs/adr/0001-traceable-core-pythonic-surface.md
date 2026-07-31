# Traceable core, pythonic surface

pangu.py v5 ports the pangu.js v9 text-spacing engine, and we chose where the parity line sits: the engine internals (`src/pangu/_core.py`) stay deliberately js-shaped — same UPPER_SNAKE regex names, same pipeline order, same placeholder machinery as `pangu.js/src/shared/index.ts` — so each upstream v9.x release ports as a mechanical diff, while everything user-facing (module functions, argparse CLI, packaging) is idiomatic Python. Output behavior is parity-locked by the 1:1 ported test suite; the public surface deliberately deviates from js: no Pangu class, no async (the engine is CPU-bound regex work — async apps use `asyncio.to_thread`), keyword-only `encoding` on `spacing_file`, stdin support (adopted upstream by the pangu.js v9.1 CLI, so no longer a deviation), and argparse usage errors exiting 2 where js exits 1.

## Consequences

- `_core.py` will read as translated JavaScript (UPPER_SNAKE constants, load-bearing pipeline order). Do not "clean it up" — its shape is its traceability.
- Rejected alternative worth remembering: output-parity-only (pythonic internals). It makes prettier Python but turns every upstream sync into a re-derivation instead of a diff.
