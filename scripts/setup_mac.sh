#!/usr/bin/env bash
# One-shot setup on macOS: tools, Python env, pre-checks. Safe to re-run.
set -euo pipefail
command -v brew >/dev/null || { echo "Homebrew missing: https://brew.sh"; exit 1; }
command -v uv >/dev/null || brew install uv
command -v git >/dev/null || brew install git
uv sync
uv run pytest -q
echo "OK. Open the folder in Cursor: cursor ."
