#Ejercicio 13
# Contar palabras
#  Crea una función que reciba una cadena y devuelva cuántas palabras contiene.

palabra = input("Escribe una frase: ")

def contarPalabras(lista):
    espacios = []
    for letras in lista:
        if letras == " ":
            espacios.append(letras)
    
    return f"Su frase tiene {len(espacios) + 1} palabras"

print(contarPalabras(palabra))