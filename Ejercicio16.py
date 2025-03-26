#Ejercicio 16
# Fibonacci.  Escribe una función que genere los primeros N números de la secuencia de Fibonacci.

numero = int(input("Introduzca la cantidad de numeros de la secuencia de fibonacci que quiere ver: "))

def fibonacci(num):
    if num == 1:
        return 0
    elif num == 2:
        return 1
    elif num > 2:
        return (fibonacci(num - 1) + fibonacci(num - 2))

def serieFibo(num):
    serie = []

    for i in range(1, num + 1):
        serie.append(fibonacci(i))
    return serie

print(f"Los {numero} primeros números de la serie de fibonacci son: \n {serieFibo(numero)}")