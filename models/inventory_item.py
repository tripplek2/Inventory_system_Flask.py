class InventoryItem:
    def __init__(
        self,
        item_id,
        barcode,
        product_name,
        brand,
        ingredients,
        category,
        price,
        stock
    ):
        self.id = item_id
        self.barcode = barcode
        self.product_name = product_name
        self.brand = brand
        self.ingredients = ingredients
        self.category = category
        self.price = price
        self.stock = stock

    def to_dict(self):
        return {
            "id": self.id,
            "barcode": self.barcode,
            "product_name": self.product_name,
            "brand": self.brand,
            "ingredients": self.ingredients,
            "category": self.category,
            "price": self.price,
            "stock": self.stock
        }