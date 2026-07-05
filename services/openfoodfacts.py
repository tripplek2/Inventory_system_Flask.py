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
   