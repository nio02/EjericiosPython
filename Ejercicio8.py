#Ejercicio 8
#Sumar números pares. Usa un for para sumar todos los números pares entre 1 y 100.

suma = 0

for i in range (1, 100 + 1):
    if i % 2 == 0:
        suma = suma + i

print("La usma de los pares es:", suma)