from flask import Blueprint, request
from data.inventory import inventory
from services.openfoodfacts import get_product_by_barcode

inventory_bp = Blueprint("inventory", __name__)

@inventory_bp.route("/inventory", methods=["GET"])
def get_inventory():
    return {
        "count": len(inventory),
        "inventory": inventory
    }, 200

@inventory_bp.route("/inventory/<int:item_id>", methods=["GET"])
def get_inventory_item(item_id):
    for item in inventory:
        if item["id"] == item_id:
            return item, 200

    return {
        "error": "Product not found."
    }, 404


@inventory_bp.route("/inventory", methods=["POST"])
def add_inventory_item():
    data = request.get_json()

    barcode = data.get("barcode")
    price = data.get("price")
    stock = data.get("stock")

    if not barcode or price is None or stock is None:
        return {
            "error": "Barcode, price and stock are required."
        }, 400
    
    product = get_product_by_barcode(barcode)

    if not product:
        return {
            "error": "Product not found in OpenFoodFacts."
        }, 404
    
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


@inventory_bp.route("/inventory/<int:item_id>", methods=["PATCH"])
def update_inventory_item(item_id):
    data = request.get_json()

    if not data:
        return {
        "error": "No data provided."
    }, 400

    for item in inventory:
        if item["id"] == item_id:

            if "price" in data:
                item["price"] = data["price"]

            if "stock" in data:
                item["stock"] = data["stock"]

            return {
                "message": "product updated succesfully.",
                "product": item
            }, 200

    return {
        "error": "product not found"
    }, 404

@inventory_bp.route("/inventory/<int:item_id>", methods=["DELETE"])
def delete_inventory_item(item_id):
    for item in inventory:
        if item["id"] == item_id:
            inventory.remove(item)

            return {
                "message": "Product deleted succesfully"
            }, 200
        
        return {
            "eroor": "product not found."
        }, 404


@inventory_bp.route("/openfood/barcode/<barcode>", methods=["GET"])
def search_by_barcode(barcode):
    product = get_product_by_barcode(barcode)

    if not product:
        return {
            "error": "Product not found."
            
        }, 404
    
    return product, 200
           


