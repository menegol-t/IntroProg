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

print("\n Act 17)A)")
cantidadDeIteracion = int(input("Ingresa el numero de iteraciones a realizar: "))
acc = 0
contador = 0
for i in range(1, cantidadDeIteracion + 1, 2) :
    if contador == 0 :
        acc = acc + 1/i
        contador = contador + 1
    else :       
        acc = acc - 1/i
        contador = contador - 1
print(acc)

print("\n Act 18)")
cantDeIteraciones = int(input("Ingresa el numero de iteraciones a realizar: "))
acumula = 1
factorial = 1
for i in range(1, cantDeIteraciones + 1) :
    while i > 0 : 
        factorial = factorial * i
        i = i - 1
    acumula = acumula + 1/factorial
    factorial = 1
print(acumula)

print("\n Act 19)A)")
m = int(input("Ingresa un numero mas chico: "))
n = int(input("Ingresa un numero mas grande: "))
for i in range(m, n+1) :
    print(i, n)
    n = n - 1

print("\n Act 19)B)")
r = int(input("Ingresa un numero mas chico: "))
s = int(input("Ingresa un numero mas grande: "))
while r < s :
    print(r, s)
    r = r + 1
    s = s - 1

# print("\n Act 19)B)")
# r = int(input("Ingresa un numero mas chico: "))
# s = int(input("Ingresa un numero mas grande: "))
# t = s
# while r < s :
#     print(r, t)
#     r = r + 1
#     t = t - 1
#     if (r > t) :
#         print(r, t)
#         r = s