print("Act en clase, dar vuelta una oracion. ")
pal = input("Ingresa una frase de dos palabras: ")
primera = ""
ultima = ""

for char in pal :
    primera +=char
    if (char == " "):
        primeraPalabra = primera

for char in pal : 
    ultima += char
    if (char == " "):
        ultima = ""

print(ultima + " " + primeraPalabra)
