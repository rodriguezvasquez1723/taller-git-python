# factorial.py

def factorial(n: int) -> int:
    """
    Calcula n! de forma iterativa.
    Acepta solo enteros no negativos (n >= 0).
    """
    if n < 0:
        raise ValueError("El factorial solo está definido para enteros no negativos (n >= 0)")

    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado
