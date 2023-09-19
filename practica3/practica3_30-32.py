print("Act 30)")
a = input("Ingresa una palabra: ")
b = input("Ingresa una letra: ")
newA = ""
for char in a :
    if char == b :
        newA+="*"
    else:
        newA+=char
print(newA)

print("\nAct 32)")
x = input("Ingresa tu nombre: ")
y = input("Ingresa tu apellido: ")
z = input("Ingresa solo los numeros de tu DNI: ")
legajo = ""
for char in z :
    if (len(legajo) < 3):
        legajo += char
legajo += "_"
for char in y :
    if(len(legajo) < 7) :
        legajo += char
i = 1
for char in x :
    if(len(legajo) < 8 or i == len(x)) :
        legajo += char
    i += 1

print(legajo)