#3. Mayor de tres números
# Pide tres números al usuario e imprime cuál es el mayor.

first_number = float(input("Introduzca el primer número: "))
second_number = float(input("Introduzca el segundo número: "))
third_number = float(input("Introduzca el tercer número: "))

numbers = [first_number, second_number, third_number]

max_number = max(numbers)

print("El número mayor es: ", max_number)
