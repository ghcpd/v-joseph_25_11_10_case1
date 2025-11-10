param()

Set-Location -Path $PSScriptRoot
$env:PYTHONPATH = "$PSScriptRoot"

& "$PSScriptRoot/.venv/Scripts/python.exe" "$PSScriptRoot/test_files/test_readme_example.py"
& "$PSScriptRoot/.venv/Scripts/python.exe" "$PSScriptRoot/test_files/test_product_manager_correct_usage.py"

try {
    & "$PSScriptRoot/.venv/Scripts/pytest.exe" -q
} catch {
    Write-Host "pytest not available; skipping pytest run. Use pip install -r requirements.txt to add pytest."
}

Write-Host "Tests complete."
