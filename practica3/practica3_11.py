print("Act 11 A)")
# a) Hacer un programa que permita al usuario elegir un número positivo n y luego muestre en pantalla todos los divisores de n.
x = int(input("Elige un numero positivo: "))
for i in range(1, x + 1):
    if x % i == 0 :
        print(i, "es divisor de", x)

print("\nAct 11 B)")
# b) Hacer un programa que permita al usuario elegir un número positivo n y luego muestre en pantalla todos los divisores pares de n.
y = int(input("Elige un numero positivo: "))
for i in range(1, y + 1):
    if y % i == 0 and i % 2 == 0 :
        print(i, "es divisor par de", y)

print("\nAct 11 C)")
# c) Hacer un programa que permita al usuario elegir un número positivo n y luego muestre en pantalla la cantidad de divisores de n.
z = int(input("Elige un numero positivo: "))
numeroDeDivisores = 0
for i in range(1, z + 1):
    if z % i == 0 :
        numeroDeDivisores = numeroDeDivisores + 1
        print(i, "es divisor de", z)
print("Numero de divisores: ", numeroDeDivisores)

print("\nAct 11 D)")
# d) Hacer un programa que permita al usuario elegir un número positivo n y luego # muestre en pantalla la suma de los divisores de n.
a = int(input("Elige un numero positivo: "))
sumaDeDivisores = 0
for i in range(1, a + 1):
    if a % i == 0 :
        sumaDeDivisores = sumaDeDivisores + i
        print(i, "es divisor de", a)
print("Los divisores de", a, "suman", sumaDeDivisores)

print("\nAct 11 E)")
# e) Hacer un programa que permita al usuario elegir dos números positivos c y n y luego muestre en pantalla los primeros c divisores de n.
c = int(input("Elige cuantos primeros divisores quieres mostrar: "))
n = int(input("Ingresa el numero al que calcularle los divisores: "))
iteracion = 1
stop = 0
while iteracion <= n :
    if n % iteracion == 0 :
        stop = stop + 1
        print(iteracion, "es divisor de", n)
        if stop >= c : iteracion =  n + 1
        else : iteracion = iteracion + 1
    else : iteracion = iteracion + 1

print("\nAct 11 F)")
# f) Hacer un programa que permita al usuario elegir dos números positivos c y n y luego muestre en pantalla los últimos c divisores de n.
b = int(input("Elige cuantos ultimos divisores quieres mostrar: "))
m = int(input("Ingresa el numero al que calcularle los divisores: "))
iteracion = m
stop = 0
while iteracion <= m and iteracion > 0:
    if m % iteracion == 0 :
        stop = stop + 1
        print(iteracion, "es divisor de", m)
        if stop >= b : iteracion = m + 1
        else : iteracion = iteracion - 1
    else : iteracion = iteracion - 1
