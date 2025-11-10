# ProductManager v2.1 (Corrected Examples)

Quick Start (examples verified with implementation)

```python
from product_manager import ProductManager

mgr = ProductManager(currency="EUR")

# Add a product (use implementation parameter names)
pid = mgr.add_product(name="Laptop", price=1000.0, stock=5, tags=["electronics", "featured"])  

# Update stock (use update_stock with delta)
mgr.update_stock(pid, delta=5)  # increase stock by 5

# List only available items (use include_out_of_stock=False)
products = mgr.list_products(include_out_of_stock=False)
print(products)

# Get total value (use get_total_value)
print("Total value:", mgr.get_total_value())

# Export (implementation exports JSON)
mgr.export_inventory("inventory.json")

# Fetch activity logs (limit is optional)
logs = mgr.get_activity_log(limit=20)
print(logs)
```

Notes:
- Parameter names and function names in the original README were outdated. This corrected file reflects the actual API.
- The export format is JSON via `export_inventory(filepath)`.
- Currency supported values are not enforced; the library stores the currency string as-is.
