import requests

BASE_URL = "http://127.0.0.1:5000"

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