import traceback
import sys
import os

# Ensure project root is on sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from product_manager import ProductManager


def run_example():
    print("Starting README examples run...\n")
    mgr = ProductManager(currency="EUR")

    # 1) Add a product (as in README)
    try:
        print("1) Calling add_product with README args: title, cost, amount, labels")
        pid = mgr.add_product(title="Laptop", cost=-1000, amount=-5, labels=["electronics", "featured"])
        print("Added, pid=", pid)
    except Exception:
        print("add_product raised:")
        traceback.print_exc()

    # 2) Update stock (wrong function name in README)
    try:
        print("\n2) Calling modify_stock as in README")
        # README uses modify_stock(pid, new_value=10)
        mgr.modify_stock(pid, new_value=10)
        print("modify_stock succeeded")
    except Exception:
        print("modify_stock raised:")
        traceback.print_exc()

    # 3) List only available items (wrong param name and logic)
    try:
        print("\n3) Calling list_products(available_only=True)")
        products = mgr.list_products(available_only=True)
        print("Products:", products)
    except Exception:
        print("list_products raised:")
        traceback.print_exc()

    # 4) Get total value (old method name)
    try:
        print("\n4) Calling calculate_total_value()")
        print("Total value:", mgr.calculate_total_value())
    except Exception:
        print("calculate_total_value raised:")
        traceback.print_exc()

    # 5) Export (wrong file format)
    try:
        print("\n5) Calling export_inventory_to_csv('inventory.csv')")
        mgr.export_inventory_to_csv("inventory.csv")
        print("Exported to CSV")
    except Exception:
        print("export_inventory_to_csv raised:")
        traceback.print_exc()

    # 6) Fetch activity logs (missing argument docs)
    try:
        print("\n6) Calling get_activity_log()")
        logs = mgr.get_activity_log()
        print("Logs:", logs)
    except Exception:
        print("get_activity_log raised:")
        traceback.print_exc()


if __name__ == '__main__':
    run_example()
