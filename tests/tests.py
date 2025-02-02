def calculate_total(products):
    total = 0
    for product in products:
        total += product["price"]  # Cambiado *= por +=
    return total

def test_calculate_total_with_empty_list():
    print("Prueba pasada exitosamente")
    assert calculate_total([]) == False  # Prueba para lista vacía

def test_calculate_total_with_single_products():
    products = [
        {
            "name": "Notebook", "price": 5
        }
    ]
    print(calculate_total(products))
    assert calculate_total(products) == 5


def test_calculate_total_with_multiple_products():
    products = [
        {
            "name": "pen", "price": 2
        },
        {
            "name": "watch", "price": 8
        }
    ]
    print(calculate_total(products))
    assert calculate_total(products) == 10

if __name__ == "__main__":
    test_calculate_total_with_empty_list()
    test_calculate_total_with_single_products()
    test_calculate_total_with_multiple_products()
    
