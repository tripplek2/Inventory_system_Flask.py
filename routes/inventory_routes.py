from flask import Blueprint, request
from data.inventory import inventory_manager
from services.openfoodfacts import (
    get_product_by_barcode,
    search_product_by_name
)

inventory_bp = Blueprint("inventory", __name__)

@inventory_bp.route("/inventory", methods=["GET"])
def get_inventory():
    items = inventory_manager.get_all_items()

    return {
        "count": len(items),
        "inventory": items
    }, 200

@inventory_bp.route("/inventory/<int:item_id>", methods=["GET"])
def get_inventory_item(item_id):
    item = inventory_manager.get_item(item_id)

    if not item:
        return {
        "error": "Product not found."
    }, 404

    return item.to_dict(), 200


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
    
    item = inventory_manager.add_item(
    product,
    price,
    stock
    )

    return {
    "message": "Product added successfully.",
    "product": item.to_dict()
}, 201


@inventory_bp.route("/inventory/<int:item_id>", methods=["PATCH"])
def update_inventory_item(item_id):
    data = request.get_json()

    if not data:
        return {
        "error": "No data provided."
    }, 400

    item = inventory_manager.update_item(item_id, data)

    if item is None:
        return {
            "error": "Product not found."
        }, 404

    return {
        "message": "Product updated successfully.",
        "product": item.to_dict()
    }, 200


@inventory_bp.route("/inventory/<int:item_id>", methods=["DELETE"])
def delete_inventory_item(item_id):
    deleted = inventory_manager.delete_item(item_id)
    
    if not deleted:
        return {
            "error": "Product not found."
        }, 404

    return {
        "message": "Product deleted successfully."
    }, 200


@inventory_bp.route("/openfood/barcode/<barcode>", methods=["GET"])
def search_by_barcode(barcode):
    product = get_product_by_barcode(barcode)

    if product is None:
        return {
            "error": "Product not found."
            
        }, 404
    
    return product, 200

@inventory_bp.route("/openfood/name/<name>", methods=["GET"])
def search_by_name(name):
    products = search_product_by_name(name)

    if not products:
        return {
            "error": "No products found."
        }, 404
    
    return {
        "count": len(products),
        "products": products
    }, 200
           


