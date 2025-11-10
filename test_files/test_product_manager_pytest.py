import pytest
from product_manager import ProductManager


def test_add_and_value():
    mgr = ProductManager(currency="USD")
    pid = mgr.add_product(name="Item", price=10.0, stock=2, tags=["t"]) 
    assert pid in mgr.products
    assert mgr.get_total_value() == 20.0


def test_update_stock_and_list():
    mgr = ProductManager(currency="USD")
    pid = mgr.add_product(name="Item2", price=3.0, stock=0)
    mgr.update_stock(pid, 5)
    listed = mgr.list_products(include_out_of_stock=False)
    assert any(p["id"] == pid for p in listed)
