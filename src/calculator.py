def sum(a, b):
    """
    >>> sum(1, 1)
    2
    """
    return a + b

def subtract(a, b):
    return a - b

def multiplay(a, b):
    return a * b

def divide(a, b):
    """
    >>> divide(10, 0)
    Traceback (most recent call last):
    ValueError: La division por 0 no esta permitida
    """
    if b == 0:
        raise ValueError("La division por 0 no esta permitida")
    return a / b

