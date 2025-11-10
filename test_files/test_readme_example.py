import traceback

from product_manager import ProductManager


def run_readme_snippet():
    mgr = ProductManager(currency="EUR")

    try:
        # README uses wrong param names; this should raise TypeError
        pid = mgr.add_product(title="Laptop", cost=-1000, amount=-5, labels=["electronics", "featured"])
        print("Added product id (unexpected):", pid)
    except Exception as e:
        print("add_product failed as expected:")
        traceback.print_exc()

    try:
        # README calls a non-existent method modify_stock
        mgr.modify_stock("pid", new_value=10)
    except Exception as e:
        print("modify_stock failed as expected:")
        traceback.print_exc()

    try:
        products = mgr.list_products(available_only=True)
        print("list_products returned (unexpected):", products)
    except Exception as e:
        print("list_products failed as expected:")
        traceback.print_exc()

    try:
        print("Total value:", mgr.calculate_total_value())
    except Exception as e:
        print("calculate_total_value failed as expected:")
        traceback.print_exc()

    try:
        mgr.export_inventory_to_csv("inventory.csv")
    except Exception as e:
        print("export_inventory_to_csv failed as expected:")
        traceback.print_exc()

    try:
        logs = mgr.get_activity_log()
        print(logs)
    except Exception as e:
        print("get_activity_log failed (unexpected):")
        traceback.print_exc()


if __name__ == "__main__":
    run_readme_snippet()
