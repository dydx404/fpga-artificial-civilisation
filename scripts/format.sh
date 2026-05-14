#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
echo "No formatter is pinned yet."
echo "Suggested future tools: ruff/black for Python, Verible for SystemVerilog, prettier for frontend."
find "$ROOT_DIR" -type f \( -name "*.py" -o -name "*.sv" -o -name "*.md" \) | sort | wc -l

