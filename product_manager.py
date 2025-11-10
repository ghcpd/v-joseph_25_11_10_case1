import uuid
from typing import List, Dict, Optional
from datetime import datetime

class ProductManager:
    def __init__(self, currency: str = "USD"):
        self.currency = currency
        self.products: Dict[str, Dict] = {}
        self.activity_log: List[str] = []

    def add_product(self, name: str, price: float, stock: int = 0, tags: Optional[List[str]] = None) -> str:
        if price <= 0:
            raise ValueError("Price must be positive.")
        if stock < 0:
            raise ValueError("Stock cannot be negative.")
        pid = str(uuid.uuid4())[:8]
        self.products[pid] = {
            "name": name,
            "price": round(price, 2),
            "stock": stock,
            "tags": tags or [],
            "created": datetime.utcnow(),
        }
        self.activity_log.append(f"[{datetime.utcnow()}] Added: {name} (${price})")
        return pid

    def update_stock(self, product_id: str, delta: int):
        if product_id not in self.products:
            raise KeyError("Product not found.")
        new_stock = self.products[product_id]["stock"] + delta
        if new_stock < 0:
            raise ValueError("Stock cannot go below zero.")
        self.products[product_id]["stock"] = new_stock
        self.activity_log.append(f"[{datetime.utcnow()}] Stock updated: {product_id} -> {new_stock}")

    def list_products(self, include_out_of_stock: bool = True, tag_filter: Optional[str] = None):
        results = []
        for pid, p in self.products.items():
            if not include_out_of_stock and p["stock"] == 0:
                continue
            if tag_filter and tag_filter not in p["tags"]:
                continue
            results.append({**p, "id": pid})
        return results

    def get_total_value(self) -> float:
        total = sum(p["price"] * p["stock"] for p in self.products.values())
        return round(total, 2)

    def export_inventory(self, filepath: str):
        import json
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(self.products, f, default=str, indent=2)
        self.activity_log.append(f"[{datetime.utcnow()}] Exported inventory to {filepath}")

    def get_activity_log(self, limit: int = 10) -> List[str]:
        return self.activity_log[-limit:]
