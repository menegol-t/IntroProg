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
        for i in range(len(list)):
            if elem == list[i] :
                repeticiones+=1
    if repeticiones > len(lista) :
        return True

print("Act 7\n")
def dondeAparece(lista, blanco):
    for i in range(len(lista)):
        if lista[i] == blanco:
            return 1
    return -1
    
codigo = int(input("Ingresa un codigo: "))
codigosDeProductos = [32, 578, 49]
productos = ["azucar", "yerba", "arroz"]
precios = ["1000$", "2500$", "800$"]

elemento = dondeAparece(codigosDeProductos, codigo)
if elemento == -1 :
    print("Elemento inexistente")
else: 
    print(codigo, productos[elemento], precios[elemento])

print("Act24)\n")
def pagara(nCli, localidad):
    cobro = 0
    if usados(nCli) > 5 and cobertura(ncli)=="Plata":
        if radioCobertura(nCli, localidad):
            cobro+=50
        else: 
            cobro+=80
    else:
        if not radioCobertura(nCli, localidad) :
            cobro +=30
    return cobro
        
print("Act25)\n")
for patente in darPatentes(8):
    if controlVelocidad(patente) > 100:
        if reincidente(patente):
            enviarMulta(patente, costoActual()*2)
        else: enviarMulta(patente, costoActual())
