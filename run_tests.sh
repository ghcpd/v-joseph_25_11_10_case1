#!/bin/bash

# ProductManager v2.1 - Test Execution Script
# Runs all test suites to verify the library and documentation

set -e  # Exit on error

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

echo "=================================================="
echo "ProductManager v2.1 - Test Suite"
echo "=================================================="

# Check if Python virtual environment exists
if [ ! -d ".venv" ]; then
    echo "Error: Virtual environment not found."
    echo "Please run: bash setup.sh"
    exit 1
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

echo "Python: $(python --version)"
echo ""

# Run test suites
test_count=0
passed_count=0
failed_count=0

run_test() {
    local test_file=$1
    local test_name=$2
    
    echo "=================================================="
    echo "Running: $test_name"
    echo "=================================================="
    
    test_count=$((test_count + 1))
    
    if python "$test_file"; then
        passed_count=$((passed_count + 1))
        echo ""
        echo "✓ $test_name passed"
        echo ""
    else
        failed_count=$((failed_count + 1))
        echo ""
        echo "✗ $test_name failed"
        echo ""
    fi
}

# Run all test files
if [ -d "test_files" ]; then
    # Test 1: Basic Operations
    if [ -f "test_files/test_basic_operations.py" ]; then
        run_test "test_files/test_basic_operations.py" "Basic Operations Test Suite"
    fi
    
    # Test 2: Documentation Examples
    if [ -f "test_files/test_documentation_examples.py" ]; then
        run_test "test_files/test_documentation_examples.py" "Documentation Examples Test Suite"
    fi
    
    # Test 3: Defects Verification
    if [ -f "test_files/test_defects_verification.py" ]; then
        run_test "test_files/test_defects_verification.py" "Defects Verification Test Suite"
    fi
else
    echo "Error: test_files directory not found"
    exit 1
fi

# Print final summary
echo "=================================================="
echo "TEST EXECUTION SUMMARY"
echo "=================================================="
echo "Total Test Suites: $test_count"
echo "Passed: $passed_count"
echo "Failed: $failed_count"
echo ""

if [ $failed_count -eq 0 ]; then
    echo "✓ ALL TEST SUITES PASSED!"
    echo ""
    echo "The ProductManager library is working correctly."
    echo "The corrected_readme.md contains accurate documentation."
    exit 0
else
    echo "✗ $failed_count test suite(s) failed"
    exit 1
fi
