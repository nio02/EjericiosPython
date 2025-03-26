#4. Tabla de multiplicar
#Escribe un programa que imprima la tabla de multiplicar del 1 al 10 para un número ingresado por el usuario.

number = int(input("Introduzca un número : "))
inicio = 1

while inicio <= 10:
    multiplo = number * inicio
    print("Su numero", number, "x",inicio,"es igual a:",multiplo)
    inicio = inicio + 1