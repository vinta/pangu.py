.PHONY: help install lint format typecheck test

help: ## Show this help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Targets:'
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  %-20s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

install: ## Install dependencies
	uv sync --locked
# CVE-2025-71176: pytest < 9.0.3 trusts /tmp/pytest-of-{user}, exploitable only by another local user; locked only for Python 3.8/3.9 (the fix needs 3.10+), dev-only, not shipped
	uv audit --ignore GHSA-6w46-j5rx-g56g

lint: ## Run ruff formatter check and linter
	uv run ruff format --check .
	uv run ruff check .

format: ## Auto-format and fix lint issues
	uv run ruff format .
	uv run ruff check --fix .

typecheck: ## Run ty type checker
	uv run ty check

test: ## Run tests
	uv run pytest -v
