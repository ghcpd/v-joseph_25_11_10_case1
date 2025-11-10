#!/usr/bin/env bash
# Run test scripts and optionally pytest
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"
export PYTHONPATH="$ROOT_DIR"

echo "Running script tests..."
"$ROOT_DIR/.venv/Scripts/python.exe" "$ROOT_DIR/test_files/test_readme_example.py"
"$ROOT_DIR/.venv/Scripts/python.exe" "$ROOT_DIR/test_files/test_product_manager_correct_usage.py"

if command -v "$ROOT_DIR/.venv/Scripts/pytest.exe" >/dev/null 2>&1; then
  echo "Running pytest..."
  "$ROOT_DIR/.venv/Scripts/pytest.exe" -q
else
  echo "pytest not installed; skipping pytest run. To run pytest: pip install -r requirements.txt"
fi

echo "All tests finished." 
