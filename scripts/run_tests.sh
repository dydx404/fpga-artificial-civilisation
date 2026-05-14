#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT_DIR/models/python"

if [ -x ".venv/bin/python" ]; then
  .venv/bin/python -m pytest
else
  python3 -m pytest
fi
