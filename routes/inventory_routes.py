from flask import Blueprint
from data.inventory import inventory

inventory_bp = Blueprint("inventory", __name__)


@inventory_bp.route("/inventory", methods=["GET"])
def get_inventory_item(item_id):
    for item in inventory:
        if item["id"] == item_id:
            return item, 200
        
    return {
        "error": "product not found"
    }, 404