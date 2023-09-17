print("act 18)")
cantidadDeIteraciones = int(input("Ingresa el numero de iteraciones a realizar: "))
acumulador = 1
factorial = 1
for i in range(1, cantidadDeIteraciones + 1) :
    while i > 0 : 
        factorial = factorial * i
        i = i - 1
    acumulador = acumulador + 1/factorial
    factorial = 1
print(acumulador)