.PHONY: help install lint format typecheck test

help: ## Show this help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Targets:'
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  %-20s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

install: ## Install dependencies
	uv sync --locked
	uv audit

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
