#!/usr/bin/env bash
set -euo pipefail

# Setup script to create a virtual environment and install dependencies
PYTHON=${PYTHON:-python}
${PYTHON} -m venv .venv
if [ -f .venv/bin/activate ]; then
    source .venv/bin/activate
elif [ -f .venv/Scripts/activate ]; then
    # On Windows, the script is different; inform the user
    echo "Activate the virtual environment: .venv\\Scripts\\activate"
fi
pip install --upgrade pip
pip install -r requirements.txt

echo "Setup complete. Activate .venv and run tests with ./run_tests.sh or ./run_tests.ps1 on Windows."
