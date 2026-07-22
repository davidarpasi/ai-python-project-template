set shell := ["bash", "-cu"]

default:
    @just --list

check: lint format-check typecheck test

format:
    uv run ruff format .

format-check:
    uv run ruff format --check .

lint:
    uv run ruff check .

typecheck:
    uv run basedpyright

test:
    uv run pytest

fix:
    uv run ruff check --fix .
    uv run ruff format .

clean:
    find . -type d -name "__pycache__" -exec rm -rf {} +
    rm -rf .pytest_cache
    rm -rf .ruff_cache