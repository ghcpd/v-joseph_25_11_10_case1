import os
import json
import sys
import pytest

# Add repo root to sys.path so tests can import product_manager.py as a module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from product_manager import ProductManager


def test_add_product_valid_and_invalid():
    mgr = ProductManager(currency="EUR")
    # Valid product add
    pid = mgr.add_product(name="Laptop", price=1000.0, stock=5, tags=["electronics", "featured"])
    assert pid in {p['id'] for p in mgr.list_products()}

    # Invalid price should raise
    with pytest.raises(ValueError):
        mgr.add_product(name="Broken", price=-100.0, stock=1)

    # Invalid stock should raise
    with pytest.raises(ValueError):
        mgr.add_product(name="NoStock", price=50.0, stock=-2)


def test_update_stock_and_listing():
    mgr = ProductManager()
    pid = mgr.add_product(name="Mouse", price=10.0, stock=0, tags=["accessory"])  # initial zero stock
    # increase stock using update_stock (delta)
    mgr.update_stock(pid, 10)
    p = [x for x in mgr.list_products() if x['id'] == pid][0]
    assert p['stock'] == 10

    # decrease below zero should raise
    with pytest.raises(ValueError):
        mgr.update_stock(pid, -20)

    # list_products include_out_of_stock behavior
    mgr2 = ProductManager()
    pid2 = mgr2.add_product(name="Test", price=5.0, stock=0)
    assert len(mgr2.list_products(include_out_of_stock=True)) >= 1
    assert len(mgr2.list_products(include_out_of_stock=False)) == 0


def test_total_value_and_export_and_logs(tmp_path):
    mgr = ProductManager()
    p1 = mgr.add_product(name="A", price=1.0, stock=3)
    p2 = mgr.add_product(name="B", price=2.0, stock=2)
    assert mgr.get_total_value() == 3*1.0 + 2*2.0

    # Export to json (export_inventory writes JSON)
    out = tmp_path / "inventory.json"
    mgr.export_inventory(str(out))
    assert out.exists()
    with open(out, "r", encoding="utf-8") as f:
        data = json.load(f)
    assert isinstance(data, dict)

    # get_activity_log default limit
    logs = mgr.get_activity_log()
    assert isinstance(logs, list)


def test_tag_filter_and_nonexistent_product_errors():
    mgr = ProductManager()
    pid = mgr.add_product(name="Tagged", price=5.0, stock=1, tags=["sale"]) 
    # tag filtering
    res = mgr.list_products(tag_filter="sale")
    assert len(res) == 1

    # KeyError for missing product on update
    with pytest.raises(KeyError):
        mgr.update_stock("nonexist", 1)
