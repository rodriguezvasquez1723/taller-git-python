# main.py
# Menú principal - Taller colaborativo Git y GitHub

from fibonacci import fibonacci
from factorial import factorial
from primos import es_primo
from perfectos import primeros_perfectos
from media import calcular_media # <-- INTEGRACIÓN DE MEDIA

def leer_entero(prompt: str, minimo: int = None) -> int:
    """Función de utilidad para leer un entero con validación."""
    while True:
        try:
            val = int(input(prompt))
            if minimo is not None and val < minimo:
                print(f"Error: ingrese un entero >= {minimo}.")
                continue
            return val
        except ValueError:
            print("Entrada inválida. Ingrese un número entero.")

def leer_numeros(prompt: str) -> List[float]:
    """Función auxiliar para leer una lista de números flotantes."""
    while True:
        try:
            entrada = input(prompt)
            # Divide la entrada por comas y convierte cada elemento a float
            return [float(x.strip()) for x in entrada.split(',')]
        except ValueError:
            print("Entrada inválida. Ingrese números separados por comas (ej: 10, 5.5, 20).")

def menu():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Fibonacci")
        print("2. Factorial")
        print("3. Determinar si un número es primo")
        print("4. N números perfectos")
        print("5. Calcular Media (Promedio)") # <-- NUEVA OPCIÓN 5
        print("6. Salir")                     # <-- Mover Salir a 6

        opcion = input("Seleccione una opción (1-6): ")

        if opcion == "1":
            # ... (Lógica de Fibonacci sin cambios)
            try:
                n = leer_entero("Ingrese N (cantidad de términos de Fibonacci, >=0): ", 0)
                resultado = fibonacci(n)
                print(f"Fibonacci({n}): {resultado}")
            except Exception as e:
                 print(f"Error al calcular Fibonacci: {e}")
        elif opcion == "2":
            # ... (Lógica de Factorial sin cambios)
            try:
                n = leer_entero("Ingrese n (entero >=0) para factorial: ", 0)
                resultado = factorial(n)
                print(f"{n}! = {resultado}")
            except Exception as e:
                print(f"Error al calcular Factorial: {e}")
        elif opcion == "3":
            # ... (Lógica de Primos sin cambios)
            try:
                n = leer_entero("Ingrese n (entero >=2) para verificar primo: ", 2)
                es_primo_val = es_primo(n)
                print(f"{n} es primo? -> {es_primo_val}")
            except Exception as e:
                print(f"Error al verificar primo: {e}")
        elif opcion == "4":
            # ... (Lógica de Perfectos sin cambios)
            try:
                N = leer_entero("Ingrese N (cantidad de números perfectos a generar, 1, 2 o 3): ", 1)
                print(f"Generando {N} números perfectos. Esto puede tardar...")
                resultado = primeros_perfectos(N)
                print(f"Primeros {N} números perfectos: {resultado}")
            except Exception as e:
                print(f"Error al generar números perfectos: {e}")
        elif opcion == "5":
            # <-- LÓGICA DE LA NUEVA OPCIÓN MEDIA
            try:
                numeros = leer_numeros("Ingrese números separados por comas (ej: 10, 5, 15): ")
                media = calcular_media(numeros)
                print(f"La media de los números ingresados es: {media:.2f}")
            except ValueError as e:
                 print(f"Error: {e}")
            except Exception as e:
                print(f"Error al calcular la media: {e}")
            # FIN LÓGICA NUEVA -->
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida, intente de nuevo.")


if __name__ == "__main__":
    # Importar el tipo List para la función auxiliar leer_numeros
    from typing import List 
    menu()
