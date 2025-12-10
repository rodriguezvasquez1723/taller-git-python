# main.py
# Menú principal - Taller colaborativo Git y GitHub

from fibonacci import fibonacci  # <-- NUEVA LÍNEA: Importar función

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
        print("3. Número primo")
        print("4. N números perfectos")
        print("5. Salir")

        opcion = input("Seleccione una opción (1-5): ")

        if opcion == "1":
            # <-- LÓGICA ACTUALIZADA DE FIBONACCI
            try:
                n = leer_entero("Ingrese N (cantidad de términos de Fibonacci, >=0): ", 0)
                resultado = fibonacci(n)
                print(f"Fibonacci({n}): {resultado}")
            except Exception as e:
                 print(f"Error al calcular Fibonacci: {e}")
            # FIN LÓGICA ACTUALIZADA -->
        elif opcion == "2":
            print("Función Factorial (pendiente de integrar)")
        elif opcion == "3":
            print("Función Primos (pendiente de integrar)")
        elif opcion == "4":
            print("Función Números Perfectos (pendiente de integrar)")
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida, intente de nuevo.")


if __name__ == "__main__":
    menu()
