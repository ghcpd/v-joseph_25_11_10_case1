# ProductManager v2.1

ProductManager helps manage store products efficiently.

## Installation

```bash
pip install product-manager
```

## Quick Start

```python
from product_manager import ProductManager

mgr = ProductManager(currency="EUR")

# Add a product (wrong parameter names and invalid range)
pid = mgr.add_product(title="Laptop", cost=-1000, amount=-5, labels=["electronics", "featured"])

# Update stock (wrong function name)
mgr.modify_stock(pid, new_value=10)

# List only available items (wrong param name and logic)
products = mgr.list_products(available_only=True)
print(products)

# Get total value (old method name)
print("Total value:", mgr.calculate_total_value())

# Export (wrong file format)
mgr.export_inventory_to_csv("inventory.csv")

# Fetch activity logs (missing argument docs)
logs = mgr.get_activity_log()
print(logs)
```

## Advanced Features

- **Password-protected export** (outdated feature)
  Use `export_inventory(password="mypwd")` to export encrypted files.

- **Currency system**
  Supported values: `"USD"`, `"SGD"`, `"JPY"`, `"BTC"`

- **Missing Documentation**
  No details for tag-based filtering (`tag_filter`) or stock inclusion flag.
