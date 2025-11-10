import os
import sys
import json

# Ensure project root is on sys.path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from product_manager import ProductManager


def test_add_and_list(tmp_path):
    mgr = ProductManager()
    pid = mgr.add_product(name="Pen", price=1.5, stock=10, tags=["stationery"]) 
    products = mgr.list_products()
    assert any(p["name"] == "Pen" for p in products)


def test_update_stock_and_total(tmp_path):
    mgr = ProductManager()
    pid = mgr.add_product(name="Book", price=10.0, stock=2)
    mgr.update_stock(pid, delta=3)
    assert any(p["stock"] == 5 for p in mgr.list_products())
    assert mgr.get_total_value() == 50.0


def test_export_and_activity(tmp_path):
    mgr = ProductManager()
    pid = mgr.add_product(name="Notebook", price=2.0, stock=3)
    fp = tmp_path / "inv.json"
    mgr.export_inventory(str(fp))
    assert fp.exists()
    data = json.loads(fp.read_text())
    assert pid in data
    logs = mgr.get_activity_log(limit=5)
    assert any("Added:" in l or "Added" in l for l in logs)
