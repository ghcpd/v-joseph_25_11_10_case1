# ProductManager v2.1

ProductManager helps manage store products efficiently.

## Installation

```bash
pip install product-manager
```

## Quick Start

```python
from product_manager import ProductManager

# Initialize with currency (note: currency is stored but not used in price calculations)
mgr = ProductManager(currency="EUR")

# Add a product with correct parameter names and valid values
# Parameters: name (str), price (float > 0), stock (int >= 0), tags (list, optional)
pid = mgr.add_product(name="Laptop", price=1000, stock=5, tags=["electronics", "featured"])

# Update stock by delta (increment/decrement value, not absolute value)
mgr.update_stock(pid, delta=10)  # Adds 10 to current stock

# List products with optional filtering
# Use include_out_of_stock=False to show only items with stock > 0
products = mgr.list_products(include_out_of_stock=False)
print("Available products:", products)

# Get total inventory value
print("Total value:", mgr.get_total_value())

# Export inventory to JSON file
mgr.export_inventory("inventory.json")

# Fetch activity logs (default returns last 10 entries)
logs = mgr.get_activity_log()
print("Recent activity:", logs)

# Fetch specific number of activity log entries
logs = mgr.get_activity_log(limit=5)
print("Last 5 activities:", logs)
```

## Advanced Features

### Currency System

The currency parameter is stored but not used in price calculations:

```python
mgr = ProductManager(currency="EUR")
mgr.add_product(name="Book", price=25.50, stock=100)
# Currency is recorded but prices are calculated independently
```

Supported currency values (informational): `"USD"`, `"SGD"`, `"JPY"`, `"BTC"`, or any custom currency string.

### Tag-Based Filtering

Filter products by tags:

```python
# Add products with tags
mgr.add_product(name="Laptop", price=1000, stock=5, tags=["electronics", "computers"])
mgr.add_product(name="Monitor", price=300, stock=10, tags=["electronics", "peripherals"])
mgr.add_product(name="Desk", price=200, stock=3, tags=["furniture"])

# Filter by specific tag
electronics = mgr.list_products(tag_filter="electronics")
print("Electronics:", electronics)

# Combine filtering: only available electronics
available_electronics = mgr.list_products(
    include_out_of_stock=False,
    tag_filter="electronics"
)
```

### Stock Management

Update product stock efficiently:

```python
pid = mgr.add_product(name="Widget", price=50, stock=100)

# Increase stock by 25 units
mgr.update_stock(pid, delta=25)  # Now has 125 units

# Decrease stock by 10 units
mgr.update_stock(pid, delta=-10)  # Now has 115 units

# Error handling
try:
    mgr.update_stock(pid, delta=-200)  # Would go below 0
except ValueError as e:
    print(f"Error: {e}")
```

### Activity Logging

All operations are automatically logged:

```python
logs = mgr.get_activity_log()  # Returns list of strings
print(logs)

# Get specific number of recent logs
recent = mgr.get_activity_log(limit=20)
for entry in recent:
    print(entry)
```

## API Reference

### ProductManager Class

#### Constructor
```python
ProductManager(currency: str = "USD")
```
- `currency`: Optional currency identifier (stored but not used in calculations)

#### Methods

##### add_product
```python
add_product(name: str, price: float, stock: int = 0, tags: Optional[List[str]] = None) -> str
```
Returns product ID as string.

**Parameters:**
- `name`: Product name (required)
- `price`: Product price in base currency (required, must be > 0)
- `stock`: Initial stock quantity (optional, default=0, must be >= 0)
- `tags`: List of tag strings for categorization (optional)

**Raises:**
- `ValueError`: If price <= 0 or stock < 0

**Example:**
```python
pid = mgr.add_product(name="Laptop", price=999.99, stock=5, tags=["electronics"])
```

##### update_stock
```python
update_stock(product_id: str, delta: int)
```
Adjusts stock by delta amount (can be positive or negative).

**Parameters:**
- `product_id`: ID returned from add_product()
- `delta`: Change in stock (positive to increase, negative to decrease)

**Raises:**
- `KeyError`: If product_id not found
- `ValueError`: If new stock would be negative

**Example:**
```python
mgr.update_stock(pid, delta=10)   # Add 10 units
mgr.update_stock(pid, delta=-5)   # Remove 5 units
```

##### list_products
```python
list_products(include_out_of_stock: bool = True, tag_filter: Optional[str] = None) -> List[Dict]
```
Returns list of products with optional filtering.

**Parameters:**
- `include_out_of_stock`: Include products with 0 stock (default=True)
- `tag_filter`: Filter by specific tag - only returns products with this tag (optional)

**Returns:** List of dictionaries with keys: id, name, price, stock, tags, created

**Example:**
```python
# All products
all_products = mgr.list_products()

# Only products with stock
in_stock = mgr.list_products(include_out_of_stock=False)

# Only products with 'electronics' tag
electronics = mgr.list_products(tag_filter="electronics")

# In-stock electronics
available_electronics = mgr.list_products(include_out_of_stock=False, tag_filter="electronics")
```

##### get_total_value
```python
get_total_value() -> float
```
Calculates total inventory value (price × stock for all products).

**Returns:** Total value as float, rounded to 2 decimal places

**Example:**
```python
total = mgr.get_total_value()
print(f"Inventory worth: ${total}")
```

##### export_inventory
```python
export_inventory(filepath: str)
```
Exports inventory to JSON file.

**Parameters:**
- `filepath`: Path where JSON file will be saved (e.g., "inventory.json")

**Example:**
```python
mgr.export_inventory("inventory.json")
```

##### get_activity_log
```python
get_activity_log(limit: int = 10) -> List[str]
```
Returns recent activity log entries.

**Parameters:**
- `limit`: Number of recent entries to return (default=10)

**Returns:** List of activity log strings in chronological order

**Example:**
```python
# Last 10 entries (default)
logs = mgr.get_activity_log()

# Last 50 entries
logs = mgr.get_activity_log(limit=50)

# All entries
logs = mgr.get_activity_log(limit=len(mgr.activity_log))
```

## Complete Example

```python
from product_manager import ProductManager

# Initialize manager
mgr = ProductManager(currency="USD")

# Add several products
laptop_id = mgr.add_product(
    name="Gaming Laptop",
    price=1299.99,
    stock=10,
    tags=["electronics", "computers", "premium"]
)

monitor_id = mgr.add_product(
    name="4K Monitor",
    price=399.99,
    stock=25,
    tags=["electronics", "peripherals"]
)

mouse_id = mgr.add_product(
    name="Wireless Mouse",
    price=49.99,
    stock=100,
    tags=["electronics", "peripherals", "accessories"]
)

# Update stock
mgr.update_stock(laptop_id, delta=5)    # Receive new stock
mgr.update_stock(monitor_id, delta=-3)  # Sell items

# Query inventory
print("All products:")
for product in mgr.list_products():
    print(f"  {product['name']}: ${product['price']} (Stock: {product['stock']})")

print("\nElectronics only:")
for product in mgr.list_products(tag_filter="electronics"):
    print(f"  {product['name']}")

print("\nIn-stock items:")
for product in mgr.list_products(include_out_of_stock=False):
    print(f"  {product['name']}: {product['stock']} units")

print(f"\nTotal inventory value: ${mgr.get_total_value()}")

# Export and view logs
mgr.export_inventory("inventory_backup.json")
print("\nRecent activities:")
for log in mgr.get_activity_log():
    print(f"  {log}")
```

## Error Handling

```python
from product_manager import ProductManager

mgr = ProductManager()

# Invalid price
try:
    mgr.add_product(name="Invalid Item", price=-100)
except ValueError as e:
    print(f"Error: {e}")  # Error: Price must be positive.

# Invalid stock
try:
    mgr.add_product(name="Another Invalid", price=50, stock=-5)
except ValueError as e:
    print(f"Error: {e}")  # Error: Stock cannot be negative.

# Product not found
try:
    mgr.update_stock("nonexistent_id", delta=10)
except KeyError as e:
    print(f"Error: {e}")  # Error: Product not found.

# Stock would go negative
try:
    pid = mgr.add_product(name="Item", price=50, stock=5)
    mgr.update_stock(pid, delta=-10)
except ValueError as e:
    print(f"Error: {e}")  # Error: Stock cannot go below zero.
```

## Notes

- All prices are rounded to 2 decimal places
- Stock quantities must be non-negative integers
- Activity logs include timestamps in UTC
- JSON export includes all product metadata and timestamps
