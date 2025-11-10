"""
test_documentation_examples.py
Tests all examples from corrected_readme.md to verify they work correctly.
"""

import sys
import json
import os
from pathlib import Path

# Add parent directory to path to import product_manager
sys.path.insert(0, str(Path(__file__).parent.parent))

from product_manager import ProductManager


def test_quick_start_example():
    """Test Quick Start example from corrected_readme.md"""
    print("\n[TEST] Quick Start Example")
    try:
        # Initialize with currency
        mgr = ProductManager(currency="EUR")

        # Add a product with correct parameter names and valid values
        pid = mgr.add_product(name="Laptop", price=1000, stock=5, tags=["electronics", "featured"])
        assert pid is not None

        # Update stock by delta
        mgr.update_stock(pid, delta=10)
        assert mgr.products[pid]["stock"] == 15

        # List products with optional filtering
        products = mgr.list_products(include_out_of_stock=False)
        assert len(products) >= 1

        # Get total inventory value
        total = mgr.get_total_value()
        assert total > 0

        # Export inventory to JSON file
        mgr.export_inventory("test_inventory.json")
        assert os.path.exists("test_inventory.json")

        # Fetch activity logs
        logs = mgr.get_activity_log()
        assert len(logs) > 0

        # Fetch specific number of activity log entries
        logs = mgr.get_activity_log(limit=5)
        assert len(logs) > 0

        os.remove("test_inventory.json")
        print("✓ PASSED: Quick Start example works correctly")
        return True
    except Exception as e:
        print(f"✗ FAILED: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_currency_system_example():
    """Test Currency System example from corrected_readme.md"""
    print("\n[TEST] Currency System Example")
    try:
        mgr = ProductManager(currency="EUR")
        mgr.add_product(name="Book", price=25.50, stock=100)
        
        # Verify currency is stored
        assert mgr.currency == "EUR"
        
        print("✓ PASSED: Currency System example works correctly")
        return True
    except Exception as e:
        print(f"✗ FAILED: {e}")
        return False


def test_tag_filtering_example():
    """Test Tag-Based Filtering example from corrected_readme.md"""
    print("\n[TEST] Tag-Based Filtering Example")
    try:
        mgr = ProductManager()
        
        # Add products with tags
        mgr.add_product(name="Laptop", price=1000, stock=5, tags=["electronics", "computers"])
        mgr.add_product(name="Monitor", price=300, stock=10, tags=["electronics", "peripherals"])
        mgr.add_product(name="Desk", price=200, stock=3, tags=["furniture"])

        # Filter by specific tag
        electronics = mgr.list_products(tag_filter="electronics")
        assert len(electronics) == 2

        # Combine filtering: only available electronics
        available_electronics = mgr.list_products(
            include_out_of_stock=False,
            tag_filter="electronics"
        )
        assert len(available_electronics) == 2
        
        print("✓ PASSED: Tag-Based Filtering example works correctly")
        return True
    except Exception as e:
        print(f"✗ FAILED: {e}")
        return False


def test_stock_management_example():
    """Test Stock Management example from corrected_readme.md"""
    print("\n[TEST] Stock Management Example")
    try:
        mgr = ProductManager()
        pid = mgr.add_product(name="Widget", price=50, stock=100)

        # Increase stock by 25 units
        mgr.update_stock(pid, delta=25)
        assert mgr.products[pid]["stock"] == 125

        # Decrease stock by 10 units
        mgr.update_stock(pid, delta=-10)
        assert mgr.products[pid]["stock"] == 115

        # Error handling
        try:
            mgr.update_stock(pid, delta=-200)  # Would go below 0
            print("✗ Should have raised ValueError")
            return False
        except ValueError:
            pass
        
        print("✓ PASSED: Stock Management example works correctly")
        return True
    except Exception as e:
        print(f"✗ FAILED: {e}")
        return False


def test_activity_logging_example():
    """Test Activity Logging example from corrected_readme.md"""
    print("\n[TEST] Activity Logging Example")
    try:
        mgr = ProductManager()
        
        mgr.add_product(name="Item", price=50)
        
        logs = mgr.get_activity_log()
        assert isinstance(logs, list)
        assert len(logs) > 0

        # Get specific number of recent logs
        recent = mgr.get_activity_log(limit=20)
        assert isinstance(recent, list)
        
        print("✓ PASSED: Activity Logging example works correctly")
        return True
    except Exception as e:
        print(f"✗ FAILED: {e}")
        return False


def test_complete_example():
    """Test Complete Example from corrected_readme.md"""
    print("\n[TEST] Complete Example")
    try:
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
        mgr.update_stock(laptop_id, delta=5)
        mgr.update_stock(monitor_id, delta=-3)

        # Query inventory
        all_products = mgr.list_products()
        assert len(all_products) == 3

        # Electronics
        electronics = mgr.list_products(tag_filter="electronics")
        assert len(electronics) == 3

        # In-stock items
        in_stock = mgr.list_products(include_out_of_stock=False)
        assert len(in_stock) == 3

        # Total value
        total = mgr.get_total_value()
        assert total > 0

        # Export and logs
        mgr.export_inventory("test_inventory_backup.json")
        logs = mgr.get_activity_log()
        assert len(logs) > 0

        os.remove("test_inventory_backup.json")
        print("✓ PASSED: Complete example works correctly")
        return True
    except Exception as e:
        print(f"✗ FAILED: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_error_handling_example():
    """Test Error Handling example from corrected_readme.md"""
    print("\n[TEST] Error Handling Example")
    try:
        mgr = ProductManager()

        # Invalid price
        try:
            mgr.add_product(name="Invalid Item", price=-100)
            print("✗ Should have raised ValueError for negative price")
            return False
        except ValueError:
            pass

        # Invalid stock
        try:
            mgr.add_product(name="Another Invalid", price=50, stock=-5)
            print("✗ Should have raised ValueError for negative stock")
            return False
        except ValueError:
            pass

        # Product not found
        try:
            mgr.update_stock("nonexistent_id", delta=10)
            print("✗ Should have raised KeyError for product not found")
            return False
        except KeyError:
            pass

        # Stock would go negative
        try:
            pid = mgr.add_product(name="Item", price=50, stock=5)
            mgr.update_stock(pid, delta=-10)
            print("✗ Should have raised ValueError for negative stock result")
            return False
        except ValueError:
            pass
        
        print("✓ PASSED: Error Handling example works correctly")
        return True
    except Exception as e:
        print(f"✗ FAILED: {e}")
        return False


def test_api_reference_add_product():
    """Test add_product API reference example"""
    print("\n[TEST] API Reference - add_product")
    try:
        mgr = ProductManager()
        pid = mgr.add_product(name="Laptop", price=999.99, stock=5, tags=["electronics"])
        
        assert pid is not None
        assert mgr.products[pid]["name"] == "Laptop"
        assert mgr.products[pid]["price"] == 999.99
        
        print("✓ PASSED: add_product API reference example works")
        return True
    except Exception as e:
        print(f"✗ FAILED: {e}")
        return False


def test_api_reference_update_stock():
    """Test update_stock API reference example"""
    print("\n[TEST] API Reference - update_stock")
    try:
        mgr = ProductManager()
        pid = mgr.add_product(name="Item", price=50, stock=100)
        
        mgr.update_stock(pid, delta=10)
        assert mgr.products[pid]["stock"] == 110
        
        mgr.update_stock(pid, delta=-5)
        assert mgr.products[pid]["stock"] == 105
        
        print("✓ PASSED: update_stock API reference example works")
        return True
    except Exception as e:
        print(f"✗ FAILED: {e}")
        return False


def test_api_reference_list_products():
    """Test list_products API reference example"""
    print("\n[TEST] API Reference - list_products")
    try:
        mgr = ProductManager()
        
        mgr.add_product(name="Laptop", price=1000, stock=5, tags=["electronics", "computers"])
        mgr.add_product(name="Monitor", price=300, stock=10, tags=["electronics", "peripherals"])

        # All products
        all_products = mgr.list_products()
        assert len(all_products) == 2

        # Only products with stock
        in_stock = mgr.list_products(include_out_of_stock=False)
        assert len(in_stock) == 2

        # Only products with 'electronics' tag
        electronics = mgr.list_products(tag_filter="electronics")
        assert len(electronics) == 2

        # In-stock electronics
        available_electronics = mgr.list_products(include_out_of_stock=False, tag_filter="electronics")
        assert len(available_electronics) == 2
        
        print("✓ PASSED: list_products API reference example works")
        return True
    except Exception as e:
        print(f"✗ FAILED: {e}")
        return False


def run_all_tests():
    """Run all documentation example tests"""
    print("\n" + "="*60)
    print("ProductManager v2.1 - Documentation Examples Test Suite")
    print("="*60)
    
    tests = [
        test_quick_start_example,
        test_currency_system_example,
        test_tag_filtering_example,
        test_stock_management_example,
        test_activity_logging_example,
        test_complete_example,
        test_error_handling_example,
        test_api_reference_add_product,
        test_api_reference_update_stock,
        test_api_reference_list_products,
    ]
    
    results = []
    for test_func in tests:
        try:
            results.append(test_func())
        except Exception as e:
            print(f"\n✗ CRASHED: {test_func.__name__}")
            print(f"  Error: {e}")
            results.append(False)
    
    # Print summary
    print("\n" + "="*60)
    print("TEST SUMMARY")
    print("="*60)
    passed = sum(results)
    total = len(results)
    print(f"Passed: {passed}/{total}")
    print(f"Failed: {total - passed}/{total}")
    
    if passed == total:
        print("\n✓ ALL DOCUMENTATION EXAMPLES WORK!")
        return 0
    else:
        print(f"\n✗ {total - passed} test(s) failed")
        return 1


if __name__ == "__main__":
    exit(run_all_tests())
