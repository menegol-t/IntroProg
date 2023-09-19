print("Act en clase, dar vuelta una oracion de dos palabras. Ex: Hola Mundo -> Mundo Hola. ")
pal = input("Ingresa una frase de dos palabras: ")
primera = ""
ultima = ""

for char in pal :
    primera +=char
    ultima +=char
    if (char == " "):
        primeraPalabra = primera
        ultima = ""

print(ultima, primeraPalabra)