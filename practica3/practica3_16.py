import math
print("\n Act 16)A)")
cantidadDeIteraciones = int(input("Ingresa el numero de iteraciones a realizar: "))
acumulador = 0
for i in range(1, cantidadDeIteraciones + 1) :
    if i % 2 == 0 :
        acumulador = acumulador - 1/i
    else :       
        acumulador = acumulador + 1/i
print(acumulador)
logaritmo = math.log(2)
print(logaritmo)

# print("\n Act 16)B)")
#A partir de la 10ma iteracion se acerca al primer decimal. (0.6)

# print("\nAct 16)C)")
#A partir de 155 iteraciones se acerca al segundo decimal. (0.69)