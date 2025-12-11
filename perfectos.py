# perfectos.py
from typing import List
import math

def suma_divisores_propios(n: int) -> int:
    """Calcula la suma de los divisores propios de n."""
    s = 1 if n > 1 else 0
    # Revisamos hasta la raíz cuadrada para optimizar la búsqueda de divisores
    for d in range(2, int(math.isqrt(n)) + 1):
        if n % d == 0:
            s += d
            otro = n // d
            if otro != d:
                s += otro
    return s

def es_perfecto(n: int) -> bool:
    """Verifica si un número es perfecto."""
    # Un número es perfecto si es mayor que 1 y la suma de sus divisores propios es igual a sí mismo
    return n > 1 and suma_divisores_propios(n) == n

def primeros_perfectos(N: int) -> List[int]:
    """
    Genera los primeros N números perfectos.
    (Advertencia: La búsqueda es computacionalmente costosa)
    """
    if N <= 0:
        raise ValueError("N debe ser un entero positivo (>= 1)")

    encontrados = []
    candidato = 2
    while len(encontrados) < N:
        if es_perfecto(candidato):
            encontrados.append(candidato)
        candidato += 1
    return encontrados
