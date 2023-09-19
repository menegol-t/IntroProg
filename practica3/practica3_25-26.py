print("\n Act 25)A)")
n = int(input("Ingresa un numero: "))
x = ""
for i in range(1, n+1) : 
    x = x + "*"
print(x)

print("\n Act 25)B)")
m = int(input("Ingresa un numero: "))
y = ""
for i in range(1, m+1) : 
    y = y + "*"
    print(y)

print("\n Act 25)C)")
o = int(input("Ingresa un numero: "))
z = ""
for i in range (1, o+1) :
    for j in range(1, (2*i-1)+1):
        z = z + "*"
    print(z)
    z = ""

print("\n Act 26)A)")
p = input("Ingresa una palabra: ")
a = (80 - len(p)) // 2
for i in range(1, a) :
    p = " " + p
print(p)

print("\n Act 26)B)")
q = input("Ingresa una palabra: ")
b = (80 - len(q))
for i in range(1, b) :
    q = " " + q
print(q)