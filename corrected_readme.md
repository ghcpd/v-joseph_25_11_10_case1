# ProductManager v2.1 (Corrected)

ProductManager helps manage and track products for small online stores.

## Installation

```bash
pip install product-manager
```

## Quick Start

```python
from product_manager import ProductManager

mgr = ProductManager(currency="EUR")

# Add a product
pid = mgr.add_product(name="Laptop", price=1000.00, stock=5, tags=["electronics", "featured"])

# Update stock
mgr.update_stock(pid, delta=10)

# List only available items
products = mgr.list_products(include_out_of_stock=False)
print(products)

# Get total inventory value
print("Total value:", mgr.get_total_value())

# Export to JSON file
mgr.export_inventory("inventory.json")

# Fetch recent activity logs
logs = mgr.get_activity_log(limit=5)
for line in logs:
    print(line)
```

## Advanced Features

### Currency
The `currency` argument is optional and used for display only.  
There is no strict validation on currency codes in v2.1.

### Product Listing Filters
You can control which products are returned:
- `include_out_of_stock`: set to `False` to skip items with zero stock.
- `tag_filter`: specify a tag to show only products with that label.
```python
mgr.list_products(tag_filter="electronics", include_out_of_stock=False)
```

### Export
Exports the full inventory as a UTF-8 JSON file using:
```python
mgr.export_inventory("inventory.json")
```

### Activity Log
Retrieve recent system actions with:
```python
logs = mgr.get_activity_log(limit=10)
```
(Default limit is 10.)
