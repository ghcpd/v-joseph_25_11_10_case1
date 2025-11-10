#!/bin/bash

# ProductManager v2.1 - Environment Setup Script
# This script sets up the Python virtual environment and installs dependencies

set -e  # Exit on error

echo "=================================================="
echo "ProductManager v2.1 - Environment Setup"
echo "=================================================="

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed or not in PATH"
    exit 1
fi

echo "Python version:"
python3 --version

# Create virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
    echo ""
    echo "Creating virtual environment..."
    python3 -m venv .venv
else
    echo ""
    echo "Virtual environment already exists at .venv"
fi

# Activate virtual environment
echo ""
echo "Activating virtual environment..."
if [ -f ".venv/bin/activate" ]; then
    source .venv/bin/activate
else
    echo "Error: Failed to find activate script"
    exit 1
fi

# Upgrade pip
echo ""
echo "Upgrading pip..."
pip install --upgrade pip

# Install requirements
echo ""
echo "Installing requirements..."
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
    echo "Requirements installed successfully"
else
    echo "Note: No requirements.txt found. Installing pytest for testing..."
    pip install pytest
fi

echo ""
echo "=================================================="
echo "Setup completed successfully!"
echo "=================================================="
echo ""
echo "To activate the environment, run:"
echo "  source .venv/bin/activate"
echo ""
echo "To run tests, run:"
echo "  bash run_tests.sh"
echo ""
