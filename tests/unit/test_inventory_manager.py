#generate ID
def test_generate_id(manager):
    assert manager.generate_id() == 1

def test_add_item(manager):
    product = {
        "barcode": "123456789",
        "product_name": "Milk",
        "brand": "Brookside",
        "ingredients": "Milk",
        "category": "Dairy"
    }

    item = manager.add_item(product, 120, 10)

    assert item.product_name == "Milk"
    assert item.price == 120
    assert item.stock == 10
    assert manager.inventory_count() == 1

def test_get_item(manager):
    product = {
        "barcode": "123456789",
        "product_name": "Milk",
        "brand": "Brookside",
        "ingredients": "Milk",
        "category": "Dairy"
    }

    manager.add_item(product, 120, 10)

    item = manager.get_item(1)

    assert item is not None
    assert item.id == 1
    assert item.product_name == "Milk"

def test_update_item(manager):
    product = {
        "barcode": "123456789",
        "product_name": "Milk",
        "brand": "Brookside",
        "ingredients": "Milk",
        "category": "Dairy"
    }

    manager.add_item(product, 120, 10)

    updated = manager.update_item(
        1,
        {
            "price": 150,
            "stock": 20
        }
    )

    assert updated.price == 150
    assert updated.stock == 20

def test_delete_item(manager):
    product = {
        "barcode": "123456789",
        "product_name": "Milk",
        "brand": "Brookside",
        "ingredients": "Milk",
        "category": "Dairy"
    }

    manager.add_item(product, 120, 10)

    deleted = manager.delete_item(1)

    assert deleted is True
    assert manager.inventory_count() == 0