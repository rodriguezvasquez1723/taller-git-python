# main.py
# Menú principal - Taller colaborativo Git y GitHub

from fibonacci import fibonacci
from factorial import factorial
from primos import es_primo
from perfectos import primeros_perfectos # <-- INTEGRACIÓN FINAL

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

def menu():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Fibonacci")
        print("2. Factorial")
        print("3. Determinar si un número es primo")
        print("4. N números perfectos")
        print("5. Salir")

        opcion = input("Seleccione una opción (1-5): ")

        if opcion == "1":
            try:
                n = leer_entero("Ingrese N (cantidad de términos de Fibonacci, >=0): ", 0)
                resultado = fibonacci(n)
                print(f"Fibonacci({n}): {resultado}")
            except Exception as e:
                 print(f"Error al calcular Fibonacci: {e}")
        elif opcion == "2":
            try:
                n = leer_entero("Ingrese n (entero >=0) para factorial: ", 0)
                resultado = factorial(n)
                print(f"{n}! = {resultado}")
            except Exception as e:
                print(f"Error al calcular Factorial: {e}")
        elif opcion == "3":
            try:
                n = leer_entero("Ingrese n (entero >=2) para verificar primo: ", 2)
                es_primo_val = es_primo(n)
                print(f"{n} es primo? -> {es_primo_val}")
            except Exception as e:
                print(f"Error al verificar primo: {e}")
        elif opcion == "4":
            # <-- LÓGICA FINAL DE PERFECTOS
            try:
                N = leer_entero("Ingrese N (cantidad de números perfectos a generar, 1, 2 o 3): ", 1)
                print(f"Generando {N} números perfectos. Esto puede tardar...")
                resultado = primeros_perfectos(N)
                print(f"Primeros {N} números perfectos: {resultado}")
            except Exception as e:
                print(f"Error al generar números perfectos: {e}")
            # FIN LÓGICA ACTUALIZADA -->
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida, intente de nuevo.")


if __name__ == "__main__":
    menu()
