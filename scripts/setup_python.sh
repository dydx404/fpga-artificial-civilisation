#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/../models/python"
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
echo "Python environment ready. Activate with: source models/python/.venv/bin/activate"

