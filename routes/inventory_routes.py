from flask import Blueprint, request
from data.inventory import inventory
from services.openfoodfacts import get_product_by_barcode

inventory_bp = Blueprint("inventory", __name__)


@inventory_bp.route("/inventory", methods=["POST"])
def add_inventory_item():
    data = request.get_json()

    barcode = data.get("barcode")
    price = data.get("price")
    stock = data.get("stock")

    if not barcode or price is None or stock is None:
        return {
            "error": "Barcode,price and stock are required."
        }, 404
    
    product = get_product_by_barcode(barcode)

    if not product:
        return {
            "error": "Product not found in OpenFoodFacts."
        }
    
    new_item = {
        "id": len(inventory) + 1,**product,
        "price": price,
        "stock": stock
    }

    inventory.append(new_item)
        
    return {
        "message": "product added succesfully.",
        "product": new_item
    }, 201