print("act 1)A)")
x = 1
while x <= 5 :
    print(x)
    x = 1 + x

print("\nact 1)B)")
y = 1
num = int(input("Ingresa un numero hacia el que contar: "))
while y <= num :
    print(y)
    y = 1 + y

print("\nact 2)A)")
z = 4
while z <= 7 :
    print(z)
    z = 1 + z

print("\nact 2)B)")
n = int(input("Ingresa el numero desde el que contar: "))
m = int(input("Ingresa el numero hasta el que contar: "))
#Si N es menor que M, el programa corta automaticamente sin contar. 
while n <= m :
    print(n)
    n = n + 1

print("\nact 3)A)")
X = 10
Y = X + 5
while X <= Y :
    print(X)
    X = 1 + X

print("\nact 3)B)")
N = int(input("Elegir un numero para añadirle 5: "))
M = N + 5
while N <= M :
    print(N)
    N = 1 + N

#NO ENTIENDO LA CORRECCION DE ESTE PUNTO:
print("\nact 3)C)")
a = int(input("Elige un numero: "))
b = int(input("Elige la cantidad de numeros que contar desde el numero anterior: "))
c = a + b
while a <= c :
    print(a)
    a = a + 1
#CORREGIDO QUEDA ASI:
# n=int (input("Ingrese un numero"))
# c=int (input("Ingrese otro numero"))
# for i in range(n,n+c+1,1):
#     print (i) #uno debajo del otro

print("\nact 4)A)")
for i in range(5, 12, 2) :
    print(i)

print("\nact 4)B)")
A = int(input("Numero desde el que empezar a contar: "))
B = int(input("Numero hasta el que contar: "))
for i in range(A, B + 1, 3) :
    print(i)

print("\nact 4)C)")
C = int(input("Numero desde el que empezar a contar: "))
D = int(input("Numero hasta el que contar: "))
E = int(input("Numero de saltos: "))
for i in range(C, D + 1, E) :
    print(i)