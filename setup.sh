#!/usr/bin/env bash
# Setup virtual environment and install requirements
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"
VENV_DIR="$ROOT_DIR/.venv"

python -m venv "$VENV_DIR"
source "$VENV_DIR/bin/activate"
pip install --upgrade pip
if [ -f "$ROOT_DIR/requirements.txt" ]; then
  pip install -r "$ROOT_DIR/requirements.txt"
fi

echo "Setup complete. Activate the venv with: source $VENV_DIR/bin/activate"
