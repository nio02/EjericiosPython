# Ejercicio 17
# Invertir una cadena. Crea una función que reciba una cadena y devuelva la cadena invertida (por ejemplo, "hola" -> "aloh").

def invertir(entrada):
    inverso = ""
    for letra in entrada:
        inverso = letra + inverso
    
    return inverso

palabra = input("Ingrese una palabra: ")

print(invertir(palabra))