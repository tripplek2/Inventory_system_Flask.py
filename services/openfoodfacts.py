import requests

BASE_URL = "https://world.openfoodfacts.org/api/v0/product"
SEARCH_URL = "https://world.openfoodfacts.org/cgi/search.pl"

HEADERS = {
    "User-Agent": "InventoryFlaskApp/1.0 (student project; contact: example@example.com)"
}

def get_product_by_barcode(barcode):
    """Fetch product details from OpenFoodFacts using a barcode"""

    url = f"{BASE_URL}/{barcode}.json"

    try:
        response = requests.get(url, headers=HEADERS)

        if response.status_code != 200:
            return None

        data = response.json()

        if data.get("status") != 1:
            return None

        product = data["product"]

        return {
            "barcode": barcode,
            "product_name": product.get("product_name", "Unknown"),
            "brand": product.get("brands", "Unknown"),
            "ingredients": product.get("ingredients_text", "Not available"),
            "category": product.get("categories", "Unknown")
        }

    except requests.RequestException:
        return None
    

def search_product_by_name(name):
    """
    Search OpenFoodFacts products by name.
    """
    params = {
        "search_terms": name,
        "search_simple": 1,
        "action": "process",
        "json": 1
    }

    try:
            response = requests.get(SEARCH_URL, params=params, headers=HEADERS,timeout=10)

            print("Status:", response.status_code)
            print("URL:", response.url)

            if response.status_code != 200:
                 return []

            data = response.json()
            print(data.keys())

            if not data.get("products"):
                return []

            products = []

            for product in data.get("products", [])[:5]:
                products.append({
                    "barcode": product.get("code"),
                    "product_name": product.get("product_name", "Unknown"),
                    "brand": product.get("brands", "Unknown"),
                    "ingredients": product.get("ingredients_text", "Not available"),
                    "category": product.get("categories", "Unknown")
                })

            return products
            
    except requests.RequestException:
            return []




   