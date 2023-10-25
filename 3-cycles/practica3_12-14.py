print("\n Act 12)")
n = int(input("Ingresa un numero: "))
for i in range(1, n + 1) : 
    print(i * n, "es la multiplicacion entre", i, "y", n)

print("\n Act 13)")
m = int(input("ingresa el valor de m: "))
sum = 0
i = 0
while sum < m :
    i = i + 1
    sum = sum + i
    if sum > m : 
        print(i)

print("\n Act 14)A)")
a = int(input("Ingresa un numero para la secuencia 2*a: "))
for i in range(1, a + 1) :
    print(2 * i)

print("\n Act 14)B)")
b = int(input("Ingresa un numero para secuencia: "))
for i in range(1, b + 1) :
    print((2 * i) - 1)    


print("\n Act 14)C)")
c = int(input("Ingresa un numero para secuencia: "))
for i in range(1, c + 1) :
    print(i**2)
    
print("\n Act 14)D)")
d = int(input("Ingresa un numero para secuencia: "))
for i in range(1, d + 1) :
    print((i**3) - (i**2))

print("\n Act 14)E)")
e = int(input("Ingresa un numero para secuencia: "))
for i in range(1, e + 1) :
    print(1/(i**2))
