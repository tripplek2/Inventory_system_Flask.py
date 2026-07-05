from models.inventory_item import InventoryItem

class InventoryManager:
    def __init__(self):
        self.inventory = []

    def generate_id(self):
         """Generate a unique ID for each inventory item."""
         if not self.inventory:
             return 1
         return max(item.id for item in self.inventory) + 1
    
    def get_all_items(self):
        """Return all inventory items."""
        return [item.to_dict() for item in self.inventory]

    def get_item(self, item_id):
        """Return one inventory item by ID."""
        for item in self.inventory:
            if item.id == item_id:
                return item
        return None 
    
    def add_item(self, product, price, stock):
        """Add a new inventory item."""
        item = InventoryItem(
            item_id=self.generate_id(),
            barcode=product["barcode"],
            product_name=product["product_name"],
            brand=product["brand"],
            ingredients=product["ingredients"],
            category=product["category"],
            price=price,
            stock=stock
        )

        self.inventory.append(item)
        return item
    
    def update_item(self, item_id, data):
        """Update an existing inventory item."""
        item = self.get_item(item_id)

        if item is None:
            return None
        
        if "price" in data:
            item.price = data["price"]

        if "stock" in data:
            item.stock = data["stock"]

        return item
    
    def delete_item(self, item_id):
        """Delete an inventory item."""
        item = self.get_item(item_id)

        if item is None:
            return False
        
        self.inventory.remove(item)
        return True
    

    def inventory_count(self):
        """Return the number of items in inventory."""
        return len(self.inventory)
    
    def clear_inventory(self):
        """Remove all items from inventory."""
        self.inventory.clear()
        
    def __repr__(self):
        return (
            f"InventoryItem("
            f"id={self.id}, "
            f"name='{self.product_name}', "
            f"stock={self.stock})"
        )
