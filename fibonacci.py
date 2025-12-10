def fibonacci(n):
    if n <= 0:
        return "El número debe ser mayor que cero."
 
    serie = []
    a, b = 0, 1
 
    for i in range(n):
        serie.append(a)
        a, b = b, a + b
 
    return serie
 
 
# Prueba local rápida
if __name__ == "__main__":
    numero = int(input("Digite cuántos números Fibonacci quiere: "))
    print(fibonacci(numero))
