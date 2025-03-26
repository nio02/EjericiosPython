#Ejercicio 18
# Frecuencia de letras. Escribe un programa que cuente la cantidad de veces que aparece cada letra en una palabra dada por el usuario.

palabra = input("Escribe una palabra: ").lower()

def contarLetras(entrada):
    totalLetras = {}
    for letra in entrada:
        totalLetras[letra] = entrada.count(letra)
    
    return totalLetras

letras = contarLetras(palabra)

print("\nLas letras de su palabra y las veces que se repiten son las siguientes: \n")

for clave, valor in letras.items():
    print(f"Letra: {clave}  -  Repeticiones: {valor}")