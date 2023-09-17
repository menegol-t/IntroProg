print("\n Act 17)A)")
cantidadDeIteraciones = int(input("Ingresa el numero de iteraciones a realizar: "))
acumulador = 0
contador = 0
for i in range(1, cantidadDeIteraciones + 1, 2) :
    if contador == 0 :
        acumulador = acumulador + 1/i
        contador = contador + 1
    else :       
        acumulador = acumulador - 1/i
        contador = contador - 1
print(acumulador)