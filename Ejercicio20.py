#Ejercicio 20
#Menú interactivo
#  Diseña un programa que muestre un menú al usuario con opciones como:
#  1. Calcular el cuadrado de un número.
#  2. Mostrar números pares entre dos valores.
#  3. Salir del programa.
#  Usa un bucle while para mantener el menú activo hasta que el usuario elija 
# salir.

def cuadradoNum(numero):
    cuadrado = numero * numero
    return cuadrado

def paresIntervalo(a, b):
    listaPares = []
    for i in range (a, b + 1):
        if i % 2 == 0:
            listaPares.append(i)
    return listaPares

print("\n ¡Bienvenido a la calculadora!\n")

while True:
    try:
        print("Elija una se las siguientes opciones escribiendo un número:\n 1. Calcular el cuadrado de un número\n 2. Mostrar números pares entre dos valores.\n 3. Salir del programa.")

        opcionUsuario = int(input())

        if opcionUsuario == 1:
            numUsuario = float(input("Escriba el número del cual quiere calcular el cuadrado: "))
            print(f"\nEl cuadrado de su numero es: {cuadradoNum(numUsuario)}\n")
        elif opcionUsuario == 2:
            limInf = int(input("Escriba el límite inferior de su intervalo: "))
            limSup = int(input("Escriba el límite superior de su intervalo: "))
            print(f"\nLos números pares de su intervalo son:\n {paresIntervalo(limInf, limSup)}\n")
        elif opcionUsuario == 3:
            print("\nGracias por preferir esta calculadora. ¡Hasta luego!")
            break
        else:
            print("\nIngrese un valor válido!\n")
    except:
        print("\nIngrese un valor válido!\n")