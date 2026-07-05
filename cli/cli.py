import requests

BASE_URL = "http://127.0.0.1:5000"

def view_inventory():
    response = requests.get(f"{BASE_URL}/inventory")

    if response.status_code != 200:
        print("Failed to retrieve inventory.")
        return
    data = response.json()

    print("\n===INVENTORY ===")
    print("-" * 40)

    if data["count"] == 0:
            print("Inventory is empty.")
            return
        
    for item in data["inventory"]:
            print(f"ID: {item['id']}")
            print(f"Product: {item['product_name']}")
            print(f"Price: {item['price']}")
            print(f"Stock: {item['stock']}")
            print("-" * 40)
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
        print("Failed to retrieve inventory.")


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
        data["stock"] = int(stock)

    response = requests.patch(
        f"{BASE_URL}/inventory/{item_id}",
        json=data
    )

    if response.status_code == 200:
        print("\nProduct updated succesfully.")
    else:
        print(response.json()["error"])

def delete_product():
    item_id = input("Enter product ID to delete: ")

    response = requests.delete(f"{BASE_URL}/inventory/{item_id}")

    if response.status_code == 200:
        print(response.json()["message"])
    else:
        print(response.json()["error"])

def search_barcode():
    barcode = input("Enter barcode: ")

    response = requests.get(
        f"{BASE_URL}/openfood/barcode/{barcode}"
    )

    print(response.json())

def search_name():
    name = input("Enter product name: ")

    response = requests.get(
        f"{BASE_URL}/openfood/name/{name}"
    )

    print(response.json())

def menu():
    while True:
        print("\n==== Inventory Management System ====")
        print("1. View Inventory")
        print("2. View Product")
        print("3. Add Product")
        print("4. Update Product")
        print("5. Delete Product")
        print("6. Search Product By Barcode")
        print("7. Search Product by Name")
        print("8. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            view_inventory

        elif choice == "2":
            view_product()

        elif choice == "3":
            add_product()

        elif choice == "4":
            update_product()

        elif choice == "5":
            delete_product

        elif choice == "6":
            search_barcode()

        elif choice == "7":
            search_name

        elif choice == "8":
            print("\nGoodbye!")
            break

        else:
            print("\nInvalid option. Please try again.")

if __name__ == "__main__":
    menu()