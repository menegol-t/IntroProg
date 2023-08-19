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