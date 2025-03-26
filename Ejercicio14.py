#Ejercicio 14
# Suma de una lista
#  Escribe una función que reciba una lista de números y devuelva la suma de todos ellos.

def sumNumbers(entrada):
    suma = sum(entrada)
    return suma

userNumbers = input("Ingrese los numeros separados por espacios: ").split()
userNumbers = [float(n) for n in userNumbers]

print("La suma de sus numeros es: ")
print(sumNumbers(userNumbers))