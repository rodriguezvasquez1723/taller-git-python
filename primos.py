# primos.py
import math

def es_primo(n: int) -> bool:
    """
    Retorna True si n es primo, False en caso contrario.
    Requiere n >= 2
    """
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False

    # Solo revisamos divisores impares hasta la raíz cuadrada de n
    limite = int(math.isqrt(n))
    for d in range(3, limite + 1, 2):
        if n % d == 0:
            return False
    return True
