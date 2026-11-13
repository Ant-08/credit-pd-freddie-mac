.PHONY: setup test lint fmt api up
setup:
	uv sync
test:
	uv run pytest
lint:
	uv run ruff check . && uv run ruff format --check .
fmt:
	uv run ruff check --fix . && uv run ruff format .
api:
	uv run uvicorn api.main:app --reload
up:
	docker compose up --build
