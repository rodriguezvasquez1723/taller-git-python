# main.py
# Menú principal - Taller colaborativo Git y GitHub

from fibonacci import fibonacci
from factorial import factorial
from primos import es_primo # <-- NUEVA LÍNEA: Importar función

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
        print("3. Determinar si un número es primo") # <-- Nombre actualizado
        print("4. N números perfectos (pendiente)")
        print("5. Salir")

        opcion = input("Seleccione una opción (1-5): ")

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
            # <-- LÓGICA ACTUALIZADA DE PRIMOS
            try:
                n = leer_entero("Ingrese n (entero >=2) para verificar primo: ", 2)
                es_primo_val = es_primo(n)
                print(f"{n} es primo? -> {es_primo_val}")
            except Exception as e:
                print(f"Error al verificar primo: {e}")
            # FIN LÓGICA ACTUALIZADA -->
        elif opcion == "4":
            print("Función Números Perfectos (pendiente de integrar)")
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida, intente de nuevo.")


if __name__ == "__main__":
    menu()
