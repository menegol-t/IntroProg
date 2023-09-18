print("Act 32)")
x = input("Ingresa tu nombre: ")
y = input("Ingresa tu apellido: ")
z = input("Ingresa solo los numeros de tu DNI: ")
legajo = ""
for char in z :
    if (len(legajo) < 3):
        legajo += char
legajo += "_"
for char in y :
    if(len(legajo) < 8) :
        legajo += char
for char in x :
    if(len(legajo) < 9) :
        print(char)
        legajo += char
i = 1
for char in x :
    if i == len(x):
        legajo += char
    else :
        i += 1
print(legajo)
