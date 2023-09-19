import math
precio_de_la_unidad = float(input("Ingrese el valor de la unidad: $"))
cantidad_de_la_unidad = int(input("Ingrese la cantidad de unidades: "))
precio_final = precio_de_la_unidad * cantidad_de_la_unidad
print(precio_final)

notaA = int(input("Primera nota: "))
notaB = int(input("Segunda nota: "))
notaC = int(input("Trcera nota: "))
print((notaA + notaB + notaC) // 3)

R = int(input("Ingresa el radio: "))
longitud = 2 * math.pi * R
area = math.pi * (R ** 2)
print("area:", area, "longitud:", longitud)