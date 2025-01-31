import requests
import ipdb 

def get_location():
    url = "https://dummyjson.com/products"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    
    
    # Filtrar productos con ID 1 y 2
    products = data["products"]
    filtered_products = [product for product in products if product["id"] in [1, 2]]
    
    # Obtener títulos de los productos filtrados
    titles = {product["id"]: product["title"] for product in filtered_products}
    return titles
    
if __name__ == "__main__":
    product_titles = get_location()
    print(product_titles)
