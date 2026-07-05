import requests

BASE_URL = "https://world.openfoodfacts.org/api/v0/product"

def get_product_by_barcode(barcode):
    """Fetch product details from OpenFoodFacts using a barcode"""

    url = f"{BASE_URL}/{barcode}.json"

    try: 
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        if data.get("status") != 1:
            return None
        
        product = data.get("product", {})

        return {
            "barcode": barcode,
            "product_name": product.get("product_name"),
            "brand": product.get("brands"),
            "ingredients": product.get("ingredients_text"),
            "category": product.get("categories")
        }
    
    except requests.RequestException:
        return None
    

def search_product_by_name(name):
        url = f"https://world.openfoodfacts.org/cgi/search.pl"

        params = {
            "search_terms": name,
            "search_simple": 1,
            "action": "process",
            "json": 1
        }

        try:
            response = requests.json()
            response.raise_for_status()

            data = response.json()

            if not data.get("products"):
                return []

            products = []

            for product in data["products"][:5]:
                products.append({
                    "barcode": product.get("code"),
                    "product_name": product.get("product_name"),
                    "brand": product.get("brands"),
                    "category": product.get("categories")
                })

            return products
            
        except requests.RequestException:
            return []




   