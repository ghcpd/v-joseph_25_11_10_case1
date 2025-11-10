"""
Run the original README examples exactly as written (including the erroneous parameter names)
and capture errors so we can compare behavior to the README.
"""
import sys
import os
import json

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from product_manager import ProductManager


def run_examples():
    mgr = ProductManager(currency="EUR")
    print("Trying to add product with wrong parameter names (expected to fail)")
    try:
        # README used title, cost, amount, labels
        mgr.add_product(title="Laptop", cost=-1000, amount=-5, labels=["electronics", "featured"])
    except Exception as e:
        print("ERROR add_product with bad params ->", type(e).__name__, str(e))

    print("Trying wrong update function name (expected to fail)")
    try:
        # README used modify_stock
        mgr.modify_stock('1234', new_value=10)
    except Exception as e:
        print("ERROR modify_stock ->", type(e).__name__, str(e))

    print("Trying list_products available_only param (expected to call but mismatch param)")
    try:
        mgr.list_products(available_only=True)
    except Exception as e:
        print("ERROR list_products ->", type(e).__name__, str(e))

    print("Trying get_total_value method mismatch (expected to fail if method name is incorrect)")
    try:
        print(mgr.calculate_total_value())
    except Exception as e:
        print("ERROR calculate_total_value ->", type(e).__name__, str(e))

    print("Trying export inventory to csv (expected to exist but the format is json)")
    try:
        mgr.export_inventory_to_csv("inventory.csv")
    except Exception as e:
        print("ERROR export_inventory_to_csv ->", type(e).__name__, str(e))

    print("Trying to get activity logs with missing arg docs")
    try:
        logs = mgr.get_activity_log()
        print("Activity logs length ->", len(logs))
    except Exception as e:
        print("ERROR get_activity_log ->", type(e).__name__, str(e))


if __name__ == '__main__':
    run_examples()
