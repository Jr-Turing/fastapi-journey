import json
from pathlib import Path
from typing import List, Dict
from uuid import UUID


DATA_FILE = Path(__file__).parent.parent / "data" / "products.json"


def load_products() -> List[Dict]:
    """Load all products from the JSON data file."""
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)

def get_all_products() -> List[Dict]:
    """Return the current product collection."""
    return load_products()


def save_products(all_products:List[Dict]) -> None:
    """Persist the complete product collection to the JSON data file."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(all_products, f, indent = 2, ensure_ascii = False)

def add_product(products: Dict) -> Dict:
    """Add a product after ensuring its SKU is unique."""
    all_products = get_all_products()

    if any(p["sku"] == products["sku"] for p in all_products):
        raise ValueError("SKU already exists")

    all_products.append(products)
    save_products(all_products)
    return products

def remove_product(id: str) -> str:
    """Remove a product by ID and return a confirmation payload."""
    products = get_all_products()
    for idx, p in enumerate(products):
        if p["id"] == str(id):
            deleted = products.pop(idx)
            save_products(products)
            return {"message": f"Product with id={id} deleted successfully", "data": deleted}

def change_product(id: str, updated_product: Dict) -> Dict:
    """Update a product by ID and return the saved product."""
    products = get_all_products()
    for idx, p in enumerate(products):
        if p["id"] == str(id):
            for key, value in updated_product.items():
                if value is None:
                    continue

            if isinstance(value, dict) and isinstance(p.get(key), dict):
                p[key].update(value)
            else:
                p[key] = value

        products[idx] = p
        save_products(products)
        return products[idx]
    
    raise ValueError(f"Product with id={id} not found")