# print("Act 1)\n")
# animales = ["elefante", "jirafa", "mono"]
# nuevoAnimal = input("Ingresa un nuevo animal: ")
# animales.append(nuevoAnimal)
# print(animales[3])

# print("Act 2)\n")
# listaEnteros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# def mostrarEnUnaLinea(listaEnteros) :
#     for el in listaEnteros :
#         print(el, end=" ")
#     print("\n")

# mostrarEnUnaLinea(listaEnteros)

# print("Act 3)\n")
# def divisores(entero):
#     divisoresDelEntero = []
#     for i in range(1, entero+1):
#         if entero % i == 0 :
#             divisoresDelEntero.append(i)
#     return divisoresDelEntero
# print(divisores(360))

# print("Act 4)\n")
# def laMasCorta(primeraLista,segundaLista):
#     if len(primeraLista) <= len(segundaLista):
#         return primeraLista
#     else:
#         return segundaLista

print("Act 5)\n")
def sonFactores(n, listN):
    contadorDeDivisores = 0
    for el in listN:
        if el % n == 0:
            contadorDeDivisores +=1
    if contadorDeDivisores == len(listN):
        return True
    else: return False

print(sonFactores(2, [2, 4, 15]))

print("Act 6)\n")
def tieneRepetidos(list):
    repeticiones = 0
    for elem in list:
        for i in range(1, len(list)):
            if elem == list[i] :
                repeticiones+=1
    if repeticiones > 1 :
        return True