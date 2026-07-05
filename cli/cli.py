import requests

BASE_URL = "https://world.openfoodfacts.org/api/v0/product"

def view_inventory():
    response = requests.get(f"{BASE_URL}/inventory")

    if response.status_code == 200:
        data = response.json()

        print("\n===INVENTORY ===")

        if data["count"] == 0:
            print("Inventory is empty.")
            return
        
        for item in data["inventory"]:
            print(f"""
ID: {item['id']}
Product: {item['product_name']}
Brand: {item['brand']}
Price: {item['price']}
Stock: {item['stock']}
-------------------------
""")
    else:
        print("Failed to retrieve inventory.")


def view_product():
    item_id = input("Enter product ID: ")

    response = requests.get(f"{BASE_URL}/inventory/{item_id}")

    if response.status_code == 200:
        item = response.json()

        print("\n===== PRODUCT DETAILS =====")
        print(f"ID: {item['id']}")
        print(f"Barcode: {item['barcode']}")
        print(f"Product: {item['product_name']}")
        print(f"Brand: {item['brand']}")
        print(f"Ingredients: {item['ingredients']}")
        print(f"Category: {item['category']}")
        print(f"Price: {item['price']}")
        print(f"Stock: {item['stock']}")

    else:
        print(response.json()["error"])


def add_product():
    barcode = input("Enter barcode: ")
    price = float(input("Enter price: "))
    stock = int(input("Enter stock quantity: "))

    data = {
        "barcode": barcode,
        "price": price,
        "stock": stock
    }

    response = requests.post(f"{BASE_URL}/inventory", json=data)

    if response.status_code == 201:
        print("\nProduct added sucessfully.")
    else:
        print(response.json()["error"])


def update_product():
    item_id = input("Enter product ID: ")

    price = input("New price (leave blank to skip): ")
    stock = input("New stock (leave blank to skip): ")

    data = {}

    if price:
        data["price"] = float(price)

    if stock:
        data["price"] = int(stock)

    response = requests.patch(
        f"{BASE_URL}/inventory/{item_id}",
        json=data
    )

    if response.status_code == 200:
        print("\nProduct updated succesfully.")
    else:
        print(response.json(["error"]))

def delete_product():
    item_id = input("Enter product ID to delete")

    response = requests.delete(f"{BASE_URL}/inventory/{item_id}")

    if response.status_code == 200:
        print(response.json()["message"])
    else:
        print(response.json()["error"])

