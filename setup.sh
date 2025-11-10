#!/usr/bin/env bash
# Setup script to create a Python virtualenv named .venv and install requirements
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt || true

echo "Environment setup complete. Activate with: source .venv/bin/activate"
