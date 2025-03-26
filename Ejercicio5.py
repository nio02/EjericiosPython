#5. Contar vocales
# Pide al usuario una palabra y usa un for para contar cuántas vocales tiene.

palabra = input("Escribe una palabra: ").lower()

vocales = ["a", "e", "i", "o", "u"]

vocalesPalabra = []

for letra in palabra: 
    if letra in vocales:
        vocalesPalabra.append(letra)

numeroVocales = len(vocalesPalabra)

print("Su palabra tiene", numeroVocales, "vocales")