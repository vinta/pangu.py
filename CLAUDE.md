# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

`pangu.py` is a text spacing library that automatically inserts whitespace between CJK (Chinese, Japanese, Korean) characters and half-width characters (alphabetical letters, numerical digits, and symbols). It is a Python port of the pangu.js v9 engine, shipped as a zero-dependency PyPI package with a module API (`spacing_text`, `spacing_file`, `has_proper_spacing`) and a CLI (`pangu` / `pangu-py`, the latter for when pangu.js's CLI shadows `pangu` on PATH).

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

Requires Python >= 3.11. Everything runs through `uv` (`uv run ...`), never bare `python3`.

**PyPI publishing**: Done via GitHub Actions (`.github/workflows/publish.yml`), triggered by pushing a `v*` tag. Uses PyPI Trusted Publishing (OIDC) — no tokens. Do NOT run `uv publish` locally. The workflow is a deliberate single job with a tag↔`pyproject.toml` version guard; see `docs/adr/0002-single-job-publish.md` before "fixing" its shape.

**Version bumps**: The version lives in two places — `pyproject.toml` and `__version__` in `src/pangu/__init__.py`. `tests/test_package.py` fails CI if they drift.

## Architecture: The Parity Line

The codebase is split by a deliberate parity line (see `docs/adr/0001-traceable-core-pythonic-surface.md`):

- `src/pangu/_core.py` — the engine, a 1:1 port of pangu.js `src/shared/index.ts`. It deliberately stays js-shaped: same UPPER_SNAKE pattern names, same load-bearing pipeline order, same placeholder machinery. Do NOT "clean it up" or pythonize it — its shape is what lets each upstream pangu.js release port as a mechanical diff. Its docstring documents the forced deviations from js regex semantics (`re.ASCII` for `\b`/`\w`, lookbehind workarounds).
- `src/pangu/_cli.py`, `__init__.py`, packaging — the public surface, idiomatic Python that deliberately deviates from js (no Pangu class, no async, keyword-only `encoding`, argparse usage errors exit 2).
- `tests/core/` — the parity spec: 1:1 ported from pangu.js `tests/shared/`, one file per symbol. Commented-out asserts and FIXME comments are intentional 1:1 ports of upstream FIXME cases; leave them.
- `tests/cli/`, `tests/test_package.py` — CLI behavior (uses `fixtures/`) and packaging guards.

**Spacing rule changes flow downstream from pangu.js.** The algorithm's source of truth is upstream; fix or tweak rules in pangu.js first, then port the diff here. Do not let the two engines' behavior fork. `CONTEXT.md` defines the domain language (joiner token, slash/pipe/plus reading, affix reading, pattern preservation) — read it before touching `_core.py`, and keep it in sync when porting upstream changes.

## Development Guidelines

- Maintain zero runtime dependencies.
- Write code comments in English with ASCII characters only. Never paste CJK sample text from tests into a comment; describe the shape generically (`CJK | CJK`, `A+CJK`) and use `\uXXXX` escape notation when a specific character matters.
- Do not wrap comments early. Ruff's line length is 200 (`pyproject.toml`) and its formatter never reflows comment text, so an early-wrapped comment stays narrow forever.
- Lint config lives in `pyproject.toml` with `select = ["ALL"]` and curated ignores. When ruff flags something, read the rule (`ruff rule <CODE>`) and fix the code; the per-file test ignores exist because the test suite is a 1:1 port — don't widen them casually.

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

## Domain Docs

Single-context layout — `CONTEXT.md` (domain language and algorithm semantics) and `docs/adr/` (decision records) at the repo root. Record reversals of documented contracts as ADRs.
