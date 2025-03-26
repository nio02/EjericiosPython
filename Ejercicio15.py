#Ejercicio 15
# Es palíndromo
#  Crea una función que determine si una palabra es un palíndromo (se lee igual al derecho y al revés). Da un mensaje, si no lo es.

def invertirPalindromo(entrada):
    inverso = ""
    for letra in entrada:
        inverso = letra + inverso

    if inverso != entrada:
        return "NO es palindromo"
    elif inverso == entrada:
        return "SI es palindromo"

palabra = input("Ingresa una palabra: ").lower()

print(invertirPalindromo(palabra))