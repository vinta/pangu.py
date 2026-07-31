# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

`pangu.py` is a text spacing library that automatically inserts whitespace between CJK (Chinese, Japanese, Korean) characters and half-width characters (alphabetical letters, numerical digits, and symbols). It is a Python port of the pangu.js v9 engine, shipped as a zero-dependency PyPI package with a module API and a CLI.

## Common Development Commands

```bash
make install                    # uv sync --locked + uv audit
make test                       # Run all tests (pytest)
make lint                       # ruff format --check + ruff check
make format                     # Auto-format and fix lint issues
make typecheck                  # ty check

uv run pytest tests/core/test_symbol_slash.py -v        # Run a single test file
uv run pytest -k "test_name" -v                         # Run tests matching a name
```

## Where Things Live

- Spacing engine, a 1:1 port of pangu.js `src/shared/index.ts`: `src/pangu/_core.py`
- Module API and CLI: `src/pangu/`
- Parity spec, ported 1:1 from pangu.js `tests/shared/`: `tests/core/`
- CLI and packaging tests: `tests/cli/`, `tests/test_package.py` (text fixtures in `fixtures/`)
- Domain language and algorithm semantics: `CONTEXT.md`; decision records: `docs/adr/`

## Gotchas

- `_core.py` deliberately stays js-shaped — same UPPER_SNAKE pattern names, same load-bearing pipeline order as pangu.js. Do NOT pythonize or "clean it up"; its shape is what lets each upstream release port as a mechanical diff (ADR 0001).
- Spacing rule changes flow downstream from pangu.js: fix or tweak rules upstream first, then port the diff. Read `CONTEXT.md` before touching `_core.py`, and keep it in sync when porting.
- Commented-out asserts and FIXME comments in `tests/core/` are intentional 1:1 ports of upstream FIXME cases — leave them. The per-file test lint ignores in `pyproject.toml` exist for the same reason; don't widen them casually.
- The version lives in two places: `pyproject.toml` and `__version__` in `src/pangu/__init__.py`. `tests/test_package.py` fails CI if they drift.
- Publishing is tag-triggered (`v*`) via GitHub Actions with PyPI Trusted Publishing (OIDC) — never publish locally. The single-job publish shape is a decided trade-off; ADR 0002 is the standing answer, don't re-propose the pack/publish split.
- The `pangu-py` entry point exists because pangu.js's CLI shadows `pangu` on PATH.
- Maintain zero runtime dependencies.
- Write code comments in English with ASCII characters only. Never paste CJK sample text into a comment; describe the shape generically (`CJK | CJK`, `A+CJK`) and use `\uXXXX` escape notation when a specific character matters.
- Record reversals of documented contracts as ADRs in `docs/adr/`.

## External Tool Documentation

Invoke the `find-docs` skill BEFORE writing code that touches a dependency's API or config, not only when the user asks about a tool. Do not answer from training data, even for familiar APIs.

### Context7 Library IDs

Pre-resolved IDs for the `find-docs` skill. Pass directly to `ctx7 docs`, skipping the `ctx7 library` step:

| Tool   | `libraryId`          |
| ------ | -------------------- |
| uv     | `/astral-sh/uv`      |
| ruff   | `/astral-sh/ruff`    |
| ty     | `/astral-sh/ty`      |
| pytest | `/pytest-dev/pytest` |
