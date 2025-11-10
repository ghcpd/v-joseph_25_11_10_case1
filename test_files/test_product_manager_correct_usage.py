from product_manager import ProductManager


def run_correct_usage():
    mgr = ProductManager(currency="EUR")

    # Add product using the actual API
    pid = mgr.add_product(name="Laptop", price=1000.0, stock=5, tags=["electronics", "featured"])
    print("Added product id:", pid)

    # Update stock properly
    mgr.update_stock(pid, 5)
    print("Stock after update:", mgr.products[pid]["stock"])  # expecting 10

    # List only in-stock items (option reversed in API)
    products = mgr.list_products(include_out_of_stock=False)
    print("Available products:", products)

    # Get total value via actual method
    print("Total value:", mgr.get_total_value())

    # Export to JSON
    mgr.export_inventory("inventory.json")

    # See activity logs
    logs = mgr.get_activity_log()
    print("Activity log:", logs)


if __name__ == "__main__":
    run_correct_usage()
