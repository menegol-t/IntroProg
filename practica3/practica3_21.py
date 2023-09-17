print("\n Act 21)A)")
m = int(input("Ingresa un numero mas chico: "))
n = int(input("Ingresa un numero mas grande: "))
for i in range(m, n+1) :
    for j in range(m, n+1) :
        if j >= i :
            print(i, j)

print("\n Act 21)B)")
limiteIzq = int(input("Ingresa un numero mas chico: "))
limiteDer = int(input("Ingresa un numero mas grande: "))
s = 0
izq = limiteIzq
der = izq
while s < 1 :
    print(izq, der)
    if (der < limiteDer and der >= izq) : 
        der = der + 1
    else :
        izq = izq + 1
        der = izq
    if izq == limiteDer and der == limiteDer : 
        s = 1
        print(izq, der)