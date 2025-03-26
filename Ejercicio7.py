# 7. Factorial
# Escribe un programa que calcule el factorial de un número usando un for.

numero = int(input("Escriba un número: "))

factorial = numero

for i in range(1, numero):
    factorial = factorial * (numero - i)

print("El factorial es:", factorial)