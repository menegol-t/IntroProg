print("\nact 14)")
x = int(input("El valor de x es: "))
y = int(input("El valor de y es: "))
if y > x :
    x, y = y, x
print(x, y)

print("\nact 15)")
a = int(input("El valor de a es: "))
b = int(input("El valor de b es: "))
c = int(input("El valor de c es: "))
if a > b :
    a, b = b, a
if a > c :
    a, c = c, a
if b > c :
    b, c = c, b
print(a, b, c)

print("\nact 16)")
z = int(input("Ingresa el año: "))
multiploDe4 = z % 4
multiploDe100 = z % 100
multiploDe400 = z % 400
if multiploDe4 == 0 :
    if multiploDe100 == 0 and multiploDe400 != 0 : print ("No es bisiesto")
    else : print("Es bisiesto")
else : print("No es bisiesto")

print("\nact 17) a.x + b = 0")
d = int(input("El valor A de la ecuacion lineal es: "))
e = int(input("El valor B de la ecuacion lineal es: "))
resultado = (-1*d)/e
if (d == 0) :
    print("Solucion: Todos los reales")
else : print("la solucion es: ", resultado)

print("\nact 18)")
f = int(input("El valor A de la ecuacion cuadratca es: "))
g = int(input("El valor B de la ecuacion cuadratca es: "))
h = int(input("El valor C de la ecuacion cuadratca es: "))
discriminante = (g ** 2) - (4 * f * h)
raizSuma = (- g - (discriminante ** 0.5)) / (2 * f)
raizResta = (- g + (discriminante ** 0.5)) / (2 * f)
if discriminante < 0 :
    print("No tiene raices.")
if discriminante == 0 :
    print(raizSuma)
if discriminante > 0 :
    print(raizSuma, raizResta)