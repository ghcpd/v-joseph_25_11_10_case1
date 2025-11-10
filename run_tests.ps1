Set-StrictMode -Version Latest
Write-Host "Activating .venv and running tests..."
. .\.venv\Scripts\Activate.ps1
pytest -q; if ($LASTEXITCODE -ne 0) { Write-Host "pytest had failures" }
python .\tests\run_readme_examples.py
