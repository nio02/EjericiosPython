#Ejericio 19
# Números perfectos. Escribe un programa que encuentre los números perfectos entre 1 y 1000. Un número perfecto es igual a la suma de sus divisores (excluyendo el propio número).

def divisoresNumero(numero):
    divisores = []
    #Divisores completos
    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores.append(i)
    #Sin contar con el numero propio
    for i in divisores:
        if i == numero:
            divisores.remove(i)
    
    return divisores

# def sumaLista(entrada):
#     suma = 0
#     for elem in entrada:
#         suma = suma + elem
#     return suma

def numerosPerfectos(numero):
    perfectos = []

    for i in range(1, numero + 1):
        divNum = divisoresNumero(i)
        if sum(divNum) == i:
            perfectos.append(i)

    return perfectos

print("Los números perfectos entre 1 y 1000 son los siguientes:")
print(numerosPerfectos(1000))