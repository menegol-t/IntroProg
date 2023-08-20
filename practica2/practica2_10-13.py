print("\nact 10)")
kwConsumidos = float(input("Ingresa los KW consumidos: "))
costoFijo = 480 + 78
kwExcedentes = kwConsumidos - 200
precioKwExcedente = kwExcedentes * 25.5
if kwConsumidos <= 200 :
    print("Tienes que pagar: $", costoFijo)
else : 
    print("Tienes que agar: $", costoFijo + precioKwExcedente)

print("\nact 11)")
x = int(input("El valor de X es: "))
y = int(input("El valor de Y es: "))
z = int(input("El valor de Z es: "))
if x > y and x > z :
    print(x)
if y > x and y > z :
    print(y)
if z > x and z > y :
    print(z)

print("\nact 12)A)")
a = float(input("Ingresa tu nota: "))
if a < 4 :
    print("reprobado")
if a >= 4 and a < 7 :
    print("debe rendir examen final")
if a >= 7 :
    print("eximido")

print("\nact 12)B)")
b = float(input("Ingresa tu primera nota: "))
c = float(input("Ingresa tu segunda nota: "))
d = float(input("Ingresa tu tercera nota: "))
e = (b + c + d)/3
if e < 4 :
    print("reprobado")
if e >= 4 and e < 7 :
    print("debe rendir examen final")
if e >= 7 :
    print("eximido")

print("\nact 13)")
f = int(input("Ingresa un numero: "))
g = int(input("Ingresa un numero: "))
if f > g : 
    print("El primer valor es mas grande.")
if g > f : 
    print ("El segundo valor es mas grande.")