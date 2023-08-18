print("\nact 16)A)")
a = int(input("Ingrese un numero entero: "))
b = int(input("Ingrese un numero entero: "))
c = int(input("Ingrese un numero entero: "))
print("Usted ingresó los valores:", a, b, c)
if a > b :
    print(a, "es mayor que", b)
if a == b :
    print(a, "y", b, "son iguales")
if a > b and a > c : 
    print(a, "es el mayor de todos")
if b < a and b < c : 
    print(b, "es el menor de todos")
if a > b or a > c : 
    print(a, "es mayor que alguno de los otros dos")
if a <= b or a <= c : 
    print(a, "es menor o igual que alguno de los otros dos")
if a == b == c : 
    print("Los tres numeros son iguales")
if a != b != c != a : 
    print("Los tres numeros son distintos")
if (a % 2) == 0 : 
    print(a, "es par")
if (a % 2) == 0 or (b % 2) == 0 or (c % 2) == 0: 
    print("alguno es par")
if (a % 2) != 0 and (b % 2) != 0 and (c % 2) != 0: 
    print("ninguno es par")
if (a % 2) == 0 and (b % 2) == 0 and (c % 2) == 0: 
    print("todos son pares")
if (a % 3) == 0 : 
    print(a, "es multiplo de 3")
if (a % 3) == 0 and (a % 5) == 0: 
    print(a, "es multiplo de 3 y de 5")
if (a % 3) == 0 and (a % 2) == 0: 
    print(a, "es multiplo de 3 y par")
if (a - b) > 0: 
    print(a, "-", b, "da un numero positivo")
if (a - b) > 0 and (a % 2) == 0: 
    print(a, "-", b, "da un numero par positivo")

print("\nact 16)A)")
edad = int(input("ingresa tu edad: "))
distancia = int(input("ingresa tu distancia del centro de votacion en kilometros: "))

if (edad >= 18 and edad <= 70 and distancia <= 500) :
    print("tenes que ir a votar")
else :
    print("no vayas a votar")
