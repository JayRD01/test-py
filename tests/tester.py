def calculate_total(products):
    total = 0
    for product in products:
        total += product["price"]  # Cambiado *= por +=
    return total

def test_calculate_total_with_empty_list():
    print("Prueba pasada exitosamente")
    assert calculate_total([]) == False  # Prueba para lista vacía



if __name__ == "__main__":
    test_calculate_total_with_empty_list()
    
