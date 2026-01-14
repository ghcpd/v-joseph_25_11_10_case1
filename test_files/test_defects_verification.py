"""
test_defects_verification.py
Tests to verify all documented defects in the original README.md
"""

import sys
from pathlib import Path

# Add parent directory to path to import product_manager
sys.path.insert(0, str(Path(__file__).parent.parent))

from product_manager import ProductManager


def verify_defect_1_wrong_parameter_names():
    """Verify Defect #1: Incorrect parameter names (title, cost, amount, labels)"""
    print("\n[VERIFY] Defect #1: Wrong Parameter Names")
    try:
        mgr = ProductManager()
        
        # These should all fail
        failures = []
        
        # Try 'title' instead of 'name'
        try:
            mgr.add_product(title="Laptop", price=1000)
            failures.append("'title' should not be accepted")
        except TypeError:
            pass
        
        # Try 'cost' instead of 'price'
        try:
            mgr.add_product(name="Laptop", cost=1000)
            failures.append("'cost' should not be accepted")
        except TypeError:
            pass
        
        # Try 'amount' instead of 'stock'
        try:
            mgr.add_product(name="Laptop", price=1000, amount=5)
            failures.append("'amount' should not be accepted")
        except TypeError:
            pass
        
        # Try 'labels' instead of 'tags'
        try:
            mgr.add_product(name="Laptop", price=1000, labels=["electronics"])
            failures.append("'labels' should not be accepted")
        except TypeError:
            pass
        
        if failures:
            print(f"✗ FAILED: {failures}")
            return False
        
        print("✓ VERIFIED: All wrong parameter names are correctly rejected")
        return True
    except Exception as e:
        print(f"✗ FAILED: {e}")
        return False


def verify_defect_2_negative_values():
    """Verify Defect #2: Invalid negative values are rejected"""
    print("\n[VERIFY] Defect #2: Negative Values Are Rejected")
    try:
        mgr = ProductManager()
        
        # Test negative price
        try:
            mgr.add_product(name="Laptop", price=-1000)
            print("✗ FAILED: Negative price should be rejected")
            return False
        except ValueError as e:
            if "Price must be positive" not in str(e):
                print(f"✗ FAILED: Wrong error message: {e}")
                return False
        
        # Test negative stock
        try:
            mgr.add_product(name="Laptop", price=1000, stock=-5)
            print("✗ FAILED: Negative stock should be rejected")
            return False
        except ValueError as e:
            if "Stock cannot be negative" not in str(e):
                print(f"✗ FAILED: Wrong error message: {e}")
                return False
        
        print("✓ VERIFIED: Negative values are correctly rejected")
        return True
    except Exception as e:
        print(f"✗ FAILED: {e}")
        return False


def verify_defect_3_modify_stock_not_exists():
    """Verify Defect #3: modify_stock method doesn't exist"""
    print("\n[VERIFY] Defect #3: 'modify_stock' method doesn't exist")
    try:
        mgr = ProductManager()
        
        # Verify modify_stock doesn't exist
        if hasattr(mgr, 'modify_stock'):
            print("✗ FAILED: modify_stock should not exist")
            return False
        
        # Verify update_stock does exist
        if not hasattr(mgr, 'update_stock'):
            print("✗ FAILED: update_stock should exist")
            return False
        
        # Verify update_stock works with delta parameter
        pid = mgr.add_product(name="Item", price=50, stock=100)
        mgr.update_stock(pid, delta=10)
        
        if mgr.products[pid]["stock"] != 110:
            print("✗ FAILED: update_stock delta not working")
            return False
        
        print("✓ VERIFIED: modify_stock doesn't exist, update_stock exists")
        return True
    except Exception as e:
        print(f"✗ FAILED: {e}")
        return False


def verify_defect_4_available_only_parameter():
    """Verify Defect #4: available_only parameter doesn't exist"""
    print("\n[VERIFY] Defect #4: 'available_only' parameter doesn't exist")
    try:
        mgr = ProductManager()
        mgr.add_product(name="Item", price=50, stock=10)
        
        # Try available_only (should fail)
        try:
            mgr.list_products(available_only=True)
            print("✗ FAILED: available_only should not be accepted")
            return False
        except TypeError:
            pass
        
        # Verify include_out_of_stock exists and works
        products = mgr.list_products(include_out_of_stock=False)
        if not isinstance(products, list):
            print("✗ FAILED: include_out_of_stock not working")
            return False
        
        print("✓ VERIFIED: available_only doesn't exist, include_out_of_stock exists")
        return True
    except Exception as e:
        print(f"✗ FAILED: {e}")
        return False


def verify_defect_5_calculate_total_value_not_exists():
    """Verify Defect #5: calculate_total_value method doesn't exist"""
    print("\n[VERIFY] Defect #5: 'calculate_total_value' doesn't exist")
    try:
        mgr = ProductManager()
        
        # Verify calculate_total_value doesn't exist
        if hasattr(mgr, 'calculate_total_value'):
            print("✗ FAILED: calculate_total_value should not exist")
            return False
        
        # Verify get_total_value does exist
        if not hasattr(mgr, 'get_total_value'):
            print("✗ FAILED: get_total_value should exist")
            return False
        
        # Verify it works
        mgr.add_product(name="Item", price=100, stock=5)
        total = mgr.get_total_value()
        
        if total != 500.0:
            print(f"✗ FAILED: get_total_value returned {total}, expected 500.0")
            return False
        
        print("✓ VERIFIED: calculate_total_value doesn't exist, get_total_value exists")
        return True
    except Exception as e:
        print(f"✗ FAILED: {e}")
        return False


def verify_defect_6_export_inventory_to_csv():
    """Verify Defect #6: export_inventory_to_csv doesn't exist"""
    print("\n[VERIFY] Defect #6: 'export_inventory_to_csv' doesn't exist")
    try:
        mgr = ProductManager()
        
        # Verify export_inventory_to_csv doesn't exist
        if hasattr(mgr, 'export_inventory_to_csv'):
            print("✗ FAILED: export_inventory_to_csv should not exist")
            return False
        
        # Verify export_inventory does exist
        if not hasattr(mgr, 'export_inventory'):
            print("✗ FAILED: export_inventory should exist")
            return False
        
        # Verify it exports to JSON, not CSV
        import json
        import os
        
        mgr.add_product(name="Item", price=50)
        test_file = "test_export.json"
        mgr.export_inventory(test_file)
        
        with open(test_file, 'r') as f:
            data = json.load(f)
            if not isinstance(data, dict):
                print("✗ FAILED: export format is not JSON")
                return False
        
        os.remove(test_file)
        print("✓ VERIFIED: export_inventory_to_csv doesn't exist, exports to JSON")
        return True
    except Exception as e:
        print(f"✗ FAILED: {e}")
        return False


def verify_defect_8_activity_log_limit():
    """Verify Defect #8: get_activity_log limit parameter not documented"""
    print("\n[VERIFY] Defect #8: get_activity_log has undocumented 'limit' parameter")
    try:
        mgr = ProductManager()
        
        # Add 20 items to create logs
        for i in range(20):
            mgr.add_product(name=f"Item{i}", price=50)
        
        # Default limit (should be 10)
        default_logs = mgr.get_activity_log()
        if len(default_logs) != 10:
            print(f"✗ FAILED: Default limit should be 10, got {len(default_logs)}")
            return False
        
        # Custom limit
        custom_logs = mgr.get_activity_log(limit=5)
        if len(custom_logs) != 5:
            print(f"✗ FAILED: Custom limit 5 failed, got {len(custom_logs)}")
            return False
        
        print("✓ VERIFIED: get_activity_log has limit parameter (default=10)")
        return True
    except Exception as e:
        print(f"✗ FAILED: {e}")
        return False


def verify_defect_9_password_parameter():
    """Verify Defect #9: password parameter doesn't exist"""
    print("\n[VERIFY] Defect #9: 'password' parameter doesn't exist (outdated)")
    try:
        mgr = ProductManager()
        mgr.add_product(name="Item", price=50)
        
        # Try to use password parameter (should fail)
        try:
            mgr.export_inventory("test.json", password="mypwd")
            print("✗ FAILED: password parameter should not be accepted")
            return False
        except TypeError:
            pass
        
        print("✓ VERIFIED: password parameter doesn't exist")
        return True
    except Exception as e:
        print(f"✗ FAILED: {e}")
        return False


def verify_defect_10_tag_filter_parameter():
    """Verify Defect #10: tag_filter parameter exists but isn't documented well"""
    print("\n[VERIFY] Defect #10: 'tag_filter' parameter exists (undocumented)")
    try:
        mgr = ProductManager()
        mgr.add_product(name="Laptop", price=1000, tags=["electronics"])
        mgr.add_product(name="Book", price=20, tags=["books"])
        
        # Use tag_filter
        electronics = mgr.list_products(tag_filter="electronics")
        if len(electronics) != 1:
            print(f"✗ FAILED: tag_filter not working, got {len(electronics)} results")
            return False
        
        books = mgr.list_products(tag_filter="books")
        if len(books) != 1:
            print(f"✗ FAILED: tag_filter not working, got {len(books)} results")
            return False
        
        print("✓ VERIFIED: tag_filter parameter exists and works")
        return True
    except Exception as e:
        print(f"✗ FAILED: {e}")
        return False


def run_all_tests():
    """Run all defect verification tests"""
    print("\n" + "="*60)
    print("ProductManager v2.1 - Defects Verification Test Suite")
    print("="*60)
    
    tests = [
        verify_defect_1_wrong_parameter_names,
        verify_defect_2_negative_values,
        verify_defect_3_modify_stock_not_exists,
        verify_defect_4_available_only_parameter,
        verify_defect_5_calculate_total_value_not_exists,
        verify_defect_6_export_inventory_to_csv,
        verify_defect_8_activity_log_limit,
        verify_defect_9_password_parameter,
        verify_defect_10_tag_filter_parameter,
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
    print("DEFECTS VERIFICATION SUMMARY")
    print("="*60)
    passed = sum(results)
    total = len(results)
    print(f"Verified: {passed}/{total}")
    print(f"Failed: {total - passed}/{total}")
    
    if passed == total:
        print("\n✓ ALL DEFECTS VERIFIED!")
        return 0
    else:
        print(f"\n✗ {total - passed} defect(s) not verified")
        return 1


if __name__ == "__main__":
    exit(run_all_tests())
