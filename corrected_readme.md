# ProductManager v2.1 — Corrected Usage

ProductManager helps manage store products. The README.md examples were out-of-date and used incorrect method/parameter names. This file shows working code and explains the correct signatures.

## Installation (local development)

Create a Python virtual environment and install test requirements:

```bash
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\Activate.ps1 on Windows PowerShell
pip install -r requirements.txt
```

## Quick Start — Correct usage

```python
from product_manager import ProductManager

mgr = ProductManager(currency="EUR")  # currency is informational; no exchange conversion is implemented

# Add a product — correct parameter names and validation
pid = mgr.add_product(name="Laptop", price=1000.00, stock=5, tags=["electronics", "featured"]) 

# Update stock — delta is added to current stock
mgr.update_stock(pid, delta=5)  # stock increases by 5

# List items — to only show in-stock items use include_out_of_stock=False
products = mgr.list_products(include_out_of_stock=False)
print(products)

# Get total value
print("Total value:", mgr.get_total_value())

# Export (writes JSON) — use export_inventory
mgr.export_inventory("inventory.json")

# Fetch recent activity logs (limit optional)
logs = mgr.get_activity_log(limit=50)
print(logs)
```

## Advanced Features (updated)

- Password-protected export: This was removed from the library; `export_inventory(password=...)` is not available. Export writes a JSON file.
- Currency system: The `currency` field is stored but not validated or used for conversion. It is informational only. Supported currency values are not validated in v2.1.
- Tag filtering: `list_products(tag_filter=<tag>)` filters products by tag. Example: `mgr.list_products(tag_filter="electronics")`
- Stock inclusion: `include_out_of_stock` decides whether to include stock `0` items. Default is True (include out of stock); set to False to only include in-stock items.

## Migration notes

If your code calls old names, replace as follows:

- `title` -> `name`
- `cost` -> `price` (must be > 0)
- `amount` -> `stock` (>= 0)
- `labels` -> `tags`
- `modify_stock(pid, new_value=N)` -> `update_stock(pid, delta=X)` — adjust to compute delta
- `calculate_total_value()` -> `get_total_value()`
- `export_inventory_to_csv(...)` -> `export_inventory(...)` (JSON output)

## Examples and tests

Run the test scripts in `test_files/` to reproduce the examples and verify behavior.

On Windows PowerShell (works with .venv already created):

```powershell
$env:PYTHONPATH = "<path-to-project-root>"
& "<path-to-project-root>/.venv/Scripts/python.exe" test_files/test_readme_example.py
& "<path-to-project-root>/.venv/Scripts/python.exe" test_files/test_product_manager_correct_usage.py
```

On Unix / Git Bash you can use the provided script (after making it executable):

```bash
chmod +x run_tests.sh
./run_tests.sh
```
