"""
test_basic_operations.py
Tests basic ProductManager operations to verify corrected documentation examples.
"""

import sys
import json
import os
from pathlib import Path

# Add parent directory to path to import product_manager
sys.path.insert(0, str(Path(__file__).parent.parent))

from product_manager import ProductManager


def test_initialization():
    """Test 1: ProductManager initialization"""
    print("\n[TEST 1] ProductManager Initialization")
    try:
        mgr = ProductManager(currency="EUR")
        assert mgr.currency == "EUR", "Currency not set correctly"
        assert mgr.products == {}, "Products should be empty"
        assert mgr.activity_log == [], "Activity log should be empty"
        print("✓ PASSED: ProductManager initialized correctly")
        return True
    except Exception as e:
        print(f"✗ FAILED: {e}")
        return False


def test_add_product():
    """Test 2: Add product with correct parameters"""
    print("\n[TEST 2] Add Product with Correct Parameters")
    try:
        mgr = ProductManager()
        
        # Test correct parameter names
        pid = mgr.add_product(name="Laptop", price=1000, stock=5, tags=["electronics", "featured"])
        assert pid is not None, "Product ID should not be None"
        assert pid in mgr.products, "Product not added to products dict"
        
        product = mgr.products[pid]
        assert product["name"] == "Laptop", "Product name mismatch"
        assert product["price"] == 1000.0, "Product price mismatch"
        assert product["stock"] == 5, "Product stock mismatch"
        assert product["tags"] == ["electronics", "featured"], "Product tags mismatch"
        
        print("✓ PASSED: Product added with correct parameters")
        return True
    except Exception as e:
        print(f"✗ FAILED: {e}")
        return False


def test_invalid_price():
    """Test 3: Invalid negative price should raise ValueError"""
    print("\n[TEST 3] Invalid Negative Price")
    try:
        mgr = ProductManager()
        try:
            mgr.add_product(name="Invalid", price=-1000, stock=5)
            print("✗ FAILED: Should have raised ValueError for negative price")
            return False
        except ValueError as e:
            assert "Price must be positive" in str(e), "Incorrect error message"
            print(f"✓ PASSED: Correctly rejected negative price with error: {e}")
            return True
    except Exception as e:
        print(f"✗ FAILED: Unexpected error: {e}")
        return False


def test_invalid_stock():
    """Test 4: Invalid negative stock should raise ValueError"""
    print("\n[TEST 4] Invalid Negative Stock")
    try:
        mgr = ProductManager()
        try:
            mgr.add_product(name="Invalid", price=100, stock=-5)
            print("✗ FAILED: Should have raised ValueError for negative stock")
            return False
        except ValueError as e:
            assert "Stock cannot be negative" in str(e), "Incorrect error message"
            print(f"✓ PASSED: Correctly rejected negative stock with error: {e}")
            return True
    except Exception as e:
        print(f"✗ FAILED: Unexpected error: {e}")
        return False


def test_update_stock():
    """Test 5: Update stock with delta (not new_value)"""
    print("\n[TEST 5] Update Stock with Delta")
    try:
        mgr = ProductManager()
        pid = mgr.add_product(name="Widget", price=50, stock=100)
        
        # Test increasing stock
        mgr.update_stock(pid, delta=25)
        assert mgr.products[pid]["stock"] == 125, "Stock increase failed"
        
        # Test decreasing stock
        mgr.update_stock(pid, delta=-10)
        assert mgr.products[pid]["stock"] == 115, "Stock decrease failed"
        
        print("✓ PASSED: Stock updated correctly with delta")
        return True
    except Exception as e:
        print(f"✗ FAILED: {e}")
        return False


def test_stock_negative_boundary():
    """Test 6: Stock cannot go below zero"""
    print("\n[TEST 6] Stock Negative Boundary")
    try:
        mgr = ProductManager()
        pid = mgr.add_product(name="Item", price=50, stock=10)
        
        try:
            mgr.update_stock(pid, delta=-20)  # Would make stock negative
            print("✗ FAILED: Should have raised ValueError")
            return False
        except ValueError as e:
            assert "Stock cannot go below zero" in str(e)
            print(f"✓ PASSED: Correctly rejected stock going negative: {e}")
            return True
    except Exception as e:
        print(f"✗ FAILED: Unexpected error: {e}")
        return False


def test_list_products_all():
    """Test 7: List all products"""
    print("\n[TEST 7] List All Products")
    try:
        mgr = ProductManager()
        pid1 = mgr.add_product(name="Item1", price=50, stock=10)
        pid2 = mgr.add_product(name="Item2", price=100, stock=0)
        
        products = mgr.list_products()
        assert len(products) == 2, f"Expected 2 products, got {len(products)}"
        
        print("✓ PASSED: Listed all products correctly")
        return True
    except Exception as e:
        print(f"✗ FAILED: {e}")
        return False


def test_list_products_exclude_out_of_stock():
    """Test 8: List products excluding out of stock (include_out_of_stock=False)"""
    print("\n[TEST 8] List Products - Exclude Out of Stock")
    try:
        mgr = ProductManager()
        mgr.add_product(name="Available", price=50, stock=10)
        mgr.add_product(name="OutOfStock", price=100, stock=0)
        
        products = mgr.list_products(include_out_of_stock=False)
        assert len(products) == 1, f"Expected 1 product, got {len(products)}"
        assert products[0]["name"] == "Available", "Wrong product returned"
        
        print("✓ PASSED: Correctly excluded out of stock items")
        return True
    except Exception as e:
        print(f"✗ FAILED: {e}")
        return False


def test_tag_filtering():
    """Test 9: Filter products by tag"""
    print("\n[TEST 9] Tag-Based Filtering")
    try:
        mgr = ProductManager()
        mgr.add_product(name="Laptop", price=1000, tags=["electronics", "computers"])
        mgr.add_product(name="Monitor", price=300, tags=["electronics", "peripherals"])
        mgr.add_product(name="Desk", price=200, tags=["furniture"])
        
        electronics = mgr.list_products(tag_filter="electronics")
        assert len(electronics) == 2, f"Expected 2 electronics, got {len(electronics)}"
        
        furniture = mgr.list_products(tag_filter="furniture")
        assert len(furniture) == 1, f"Expected 1 furniture, got {len(furniture)}"
        
        print("✓ PASSED: Tag filtering works correctly")
        return True
    except Exception as e:
        print(f"✗ FAILED: {e}")
        return False


def test_combined_filtering():
    """Test 10: Combine include_out_of_stock and tag_filter"""
    print("\n[TEST 10] Combined Filtering (Stock + Tag)")
    try:
        mgr = ProductManager()
        mgr.add_product(name="Laptop", price=1000, stock=5, tags=["electronics"])
        mgr.add_product(name="Monitor", price=300, stock=0, tags=["electronics"])
        mgr.add_product(name="Desk", price=200, stock=3, tags=["furniture"])
        
        # In-stock electronics only
        result = mgr.list_products(include_out_of_stock=False, tag_filter="electronics")
        assert len(result) == 1, f"Expected 1 in-stock electronic, got {len(result)}"
        assert result[0]["name"] == "Laptop", "Wrong product"
        
        print("✓ PASSED: Combined filtering works correctly")
        return True
    except Exception as e:
        print(f"✗ FAILED: {e}")
        return False


def test_get_total_value():
    """Test 11: Calculate total inventory value"""
    print("\n[TEST 11] Get Total Value")
    try:
        mgr = ProductManager()
        mgr.add_product(name="Item1", price=100, stock=5)   # 500
        mgr.add_product(name="Item2", price=50, stock=10)   # 500
        
        total = mgr.get_total_value()
        assert total == 1000.0, f"Expected 1000.0, got {total}"
        
        print("✓ PASSED: Total value calculated correctly")
        return True
    except Exception as e:
        print(f"✗ FAILED: {e}")
        return False


def test_export_inventory():
    """Test 12: Export inventory to JSON"""
    print("\n[TEST 12] Export Inventory")
    try:
        mgr = ProductManager()
        mgr.add_product(name="Laptop", price=1000, stock=5)
        
        # Use current directory for cross-platform compatibility
        export_file = "test_inventory.json"
        mgr.export_inventory(export_file)
        
        assert os.path.exists(export_file), "Export file not created"
        
        with open(export_file, 'r') as f:
            data = json.load(f)
            assert isinstance(data, dict), "Exported data should be a dictionary"
            assert len(data) == 1, "Should have 1 product"
        
        os.remove(export_file)
        print("✓ PASSED: Inventory exported successfully to JSON")
        return True
    except Exception as e:
        print(f"✗ FAILED: {e}")
        return False


def test_activity_log_default_limit():
    """Test 13: Activity log returns last 10 entries by default"""
    print("\n[TEST 13] Activity Log - Default Limit")
    try:
        mgr = ProductManager()
        
        # Add 15 products to create 15 log entries
        for i in range(15):
            mgr.add_product(name=f"Product{i}", price=100)
        
        logs = mgr.get_activity_log()
        assert len(logs) == 10, f"Expected 10 logs (default), got {len(logs)}"
        
        print("✓ PASSED: Activity log returns last 10 entries by default")
        return True
    except Exception as e:
        print(f"✗ FAILED: {e}")
        return False


def test_activity_log_custom_limit():
    """Test 14: Activity log with custom limit"""
    print("\n[TEST 14] Activity Log - Custom Limit")
    try:
        mgr = ProductManager()
        
        # Add 20 products
        for i in range(20):
            mgr.add_product(name=f"Product{i}", price=100)
        
        # Request last 5
        logs = mgr.get_activity_log(limit=5)
        assert len(logs) == 5, f"Expected 5 logs, got {len(logs)}"
        
        # Request last 50 (more than exist)
        logs = mgr.get_activity_log(limit=50)
        assert len(logs) == 20, f"Expected 20 logs (all available), got {len(logs)}"
        
        print("✓ PASSED: Activity log custom limit works correctly")
        return True
    except Exception as e:
        print(f"✗ FAILED: {e}")
        return False


def test_product_not_found():
    """Test 15: Handling product not found"""
    print("\n[TEST 15] Product Not Found Error")
    try:
        mgr = ProductManager()
        
        try:
            mgr.update_stock("nonexistent_id", delta=10)
            print("✗ FAILED: Should have raised KeyError")
            return False
        except KeyError as e:
            assert "Product not found" in str(e)
            print(f"✓ PASSED: Correctly raised KeyError: {e}")
            return True
    except Exception as e:
        print(f"✗ FAILED: Unexpected error: {e}")
        return False


def run_all_tests():
    """Run all tests and return summary"""
    print("\n" + "="*60)
    print("ProductManager v2.1 - Test Suite")
    print("="*60)
    
    tests = [
        test_initialization,
        test_add_product,
        test_invalid_price,
        test_invalid_stock,
        test_update_stock,
        test_stock_negative_boundary,
        test_list_products_all,
        test_list_products_exclude_out_of_stock,
        test_tag_filtering,
        test_combined_filtering,
        test_get_total_value,
        test_export_inventory,
        test_activity_log_default_limit,
        test_activity_log_custom_limit,
        test_product_not_found,
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
        print("\n✓ ALL TESTS PASSED!")
        return 0
    else:
        print(f"\n✗ {total - passed} test(s) failed")
        return 1


if __name__ == "__main__":
    exit(run_all_tests())
