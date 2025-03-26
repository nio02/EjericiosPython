#Ejercicio 11
# Área de un triángulo
#  Crea una función que calcule el área de un triángulo dados su base y altura.

def areaTriangulo(b, a):
    area = (b * a) / 2
    return area

base = float(input("Introduzca la base del triangulo: "))
altura = float(input("Introduzca la altura del triangulo: "))

print(f"El área es: {areaTriangulo(base, altura)}")