# main.py
# Menú principal - Taller colaborativo Git y GitHub

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
            print("Función Fibonacci (pendiente de integrar)")
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
