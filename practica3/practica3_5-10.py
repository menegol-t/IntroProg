print("\nact 5)")
for i in range (8,2,-1):
    print(i)

print("\nact 6")
for i in range(15, 5, -3):
    print(i)

print("\nact 8)")
for i in range(-99, 100, 1) : 
    s = i ** ((i + 2)*(i + 3))
    if s == 1 :
        print(i, "es solucion.")

print("\nact 9)")
x = int(input("Ingresa un numero: "))
y = 0
while x != 1 :
    if x % 2 == 0 :
        x = x/2
        print("Valor par", x)
        y = y+1
    else :
        x = 3 * x + 1
        print("Valor inpar", x)
        y = y+1
print("Iteraciones:", y)

print("\nact 10)A)")
a = int(input("Ingresa un numero: "))
b = 1
c = 1
while b < a : 
    print(b)
    b = 2 ** c
    c = c + 1

print("\nact 10)B)")
z = int(input("Ingresa un numero: "))
for i in range(0, z) :
    print(2 ** i)

print("\nact 10)C)")
Z = int(input("Ingresa un numero: "))
for i in range(1, Z + 1) : 
    print ( i ** i )