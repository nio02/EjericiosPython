#Ejercicio 10
#Número primo. Pide un número al usuario y determina si es primo (divisible solo por 1 y por sí mismo).

userNumber = int(input("Ingresa un número: "))

divisores = []

for i in range(1, userNumber + 1):
    if userNumber % i == 0:
        divisores.append(i)

if len(divisores) >= 3:
    print("Su número NO es primo")
else:
    print("Su número ES primo")