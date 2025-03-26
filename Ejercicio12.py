#Ejercicio 12
# Número mayor
#  Escribe una función que reciba tres números y devuelva el mayor de ellos.

first_number = float(input("Introduzca el primer número: "))
second_number = float(input("Introduzca el segundo número: "))
third_number = float(input("Introduzca el tercer número: "))

numbers = [first_number, second_number, third_number]

max_number = max(numbers)

print("El número mayor es: ", max_number)