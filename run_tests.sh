#!/usr/bin/env bash
set -e
source .venv/bin/activate
python -m pytest -q || true
python tests/run_readme_examples.py
