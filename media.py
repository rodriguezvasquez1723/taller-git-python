# media.py
from typing import List

def calcular_media(numeros: List[float]) -> float:
    """
    Calcula la media aritmética (promedio) de una lista de números.
    """
    if not numeros:
        # Manejar el caso de una lista vacía para evitar división por cero
        raise ValueError("La lista de números no puede estar vacía para calcular la media.")

    suma = sum(numeros)
    cantidad = len(numeros)

    return suma / cantidad
