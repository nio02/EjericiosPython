#Ejercicio 9
#Adivina el número. Genera un número aleatorio entre 1 y 10 (usa random.randint) y permite al usuario  adivinarlo. 
#*Da pistas como "muy bajo" o "muy alto".

import random

randomNumber = random.randint(1, 10)

userNumber = int(input("Adivina el número de 1 a 10, escribe el número: "))

print(randomNumber)

while userNumber != randomNumber:
    userNumber = int(input("Lo siento, ese número no era. Ingresa el número nuevamente: "))
    if userNumber <= randomNumber - 5:
        print("Muy Bajo!")
    elif userNumber >= randomNumber + 5:
        print("Muy alto!")
    elif userNumber <= randomNumber - 2:
        print("Bajito...")
    elif userNumber >= randomNumber + 2:
        print("Altico...")
    elif userNumber <= randomNumber - 1:
        print("Un poquitito mas...")
    elif userNumber >= randomNumber + 1:
        print("Un poquitito menos...")
    elif userNumber == randomNumber:
        print("¡Adivinaste!. Es correcto")