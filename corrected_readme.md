# ProductManager v2.1 - Corrected README

ProductManager helps manage store products efficiently.

## Installation

Clone the repo and, optionally, install the test dependencies in a venv:

```bash
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
```

Note: The original README suggested `pip install product-manager` — this package isn't published to PyPI in this repo. Use the local module `product_manager.py` instead.

## Quick Start

Corrected example for using ProductManager API (these examples run with the current implementation):

```python
from product_manager import ProductManager

mgr = ProductManager(currency="EUR")  # currency is a free-form string; not validated internally

# Add a product (use actual parameter names: name, price, stock, tags)
pid = mgr.add_product(name="Laptop", price=1000.0, stock=5, tags=["electronics", "featured"])

# Update stock (use update_stock(product_id, delta) to add or remove units)
mgr.update_stock(pid, 5)  # add 5 units

# List only available items (set include_out_of_stock=False)
products = mgr.list_products(include_out_of_stock=False)
print(products)

# Get total value (use get_total_value())
print("Total value:", mgr.get_total_value())

# Export inventory to JSON (the method export_inventory writes JSON)
mgr.export_inventory("inventory.json")

# Fetch activity logs (you can pass a limit, default is 10)
logs = mgr.get_activity_log(limit=20)
print(logs)
```

## Advanced Features

- Password-protected export is not implemented in the current code. The README previously referenced an `export_inventory(password="mypwd")` signature, which does not exist — the method is currently `export_inventory(filepath: str)` and writes a JSON file.

- Currency: The code accepts any string as currency; there is no validation. Typical currency examples: "USD", "EUR", "SGD", "JPY", "BTC".

- Tag filtering: Use `list_products(tag_filter="tag")` to filter results by tag.

- include_out_of_stock: Set to False to exclude products that have zero stock.

## Notes

The README examples were previously out-of-sync with the implementation — this corrected README fixes parameter names, shows proper behavior for stock updates, and clarifies the export and activity log usage.
