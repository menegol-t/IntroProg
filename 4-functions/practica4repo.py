# print("\n actividad 3)A)")
def repe (cadena):
    print(cadena)
    print(cadena)
    print(cadena)
    
# print("\n actividad 4)A)")
def promedio2 (a, b): return (a + b)/2
    
# print("\n actividad 4)C)")
def promedio3 (a, b, c): return (a + b + c)/3

# print("\nAct 5)")
def modulo(n): return n if n >= 0 else -1 * n

# print("\nAct 6)A)")
def exclamar(unaCadena): return "¡" + unaCadena + "!"

# print("\nAct 6)C)")
def gritar(unaCadena): return exclamar(exclamar(exclamar(unaCadena)))

# print("\nAct 7)A)")
def elevarCubo(n): return n ** 3

# print("\nAct 8)A)B)D)")
def cantDivisores(n):
    if n >= 0 :
        return contDiv(n)
    else: 
        m = n * -1
        return contDiv(m)
    
def contDiv(n):
    cont = 0
    for i in range(1, n + 1):
        if n % i == 0 : 
            cont += 1
    return cont
    
def esPrimo(n): return True if cantDivisores(n) == 2 else False
    
def factoresPrimos(n):
    for i in range(1, n + 1):
        if n % i == 0 and esPrimo(i): 
            print(i)

# print("\nAct 9)A)")
def mayorDeDos(n, m): return n if n >= m else m

# print("\nAct 9)B)")
def mayorDeTres(n, m, o): 
    if (n >= m) and (n >= o):
        return n
    elif (m >= n) and (m >= o):
        return m
    elif(o >= n) and (o >= m):
        return o

# print("\nAct 10)")        
def potencia (a, b): return a ** b

# print("\n Act 11)A)")
def sumaDeDivisores(n): 
    acum = 0
    for i in range(1, n): #saco de los divisores a si mismo, porque si no nunca va a dar perfecto y siempre abundante
        if n % i == 0 : 
            acum += i
    return acum

# print("\n Act 11)B)")
def esPerfecto(n): return True if sumaDeDivisores(n) == n else False

# print("\n Act 11)C)")
def esAbundante(n): return True if sumaDeDivisores(n) > n else False

# print("\n Act 12)")
def esPoderoso(n):
    divPrimos = 0
    cuadradosDivisores = 0
    for i in range(1, n + 1):
        if n % i == 0 and esPrimo(i) : 
            divPrimos += 1
            if n % (i**2) == 0:
                cuadradosDivisores += 1
    return True if cuadradosDivisores == divPrimos else False

        
# print("\n Act 13)")
def esLibreDeCuadrado(n):
    for i in range(1, n + 1):
        if n % i == 0 and esPrimo(i) and n % (i**2) == 0: 
            return False
    return True

# print("\n Act 14)")
def siguienteNumeroPrimo(n):
    i = 0
    while i < 1 :
        if esPrimo(n + 1) :
            return n + 1
        else: n += 1

# print("\n Act 15)")
def palabraRecuadradaConAsterizcos(a) :
    newStr = ""
    caracteresMasDosEspaciosCadaLadoPorLinea = (len(a) + 4)

    for i in range(1, caracteresMasDosEspaciosCadaLadoPorLinea+1):
        if i < caracteresMasDosEspaciosCadaLadoPorLinea :
            newStr += "*"
        elif i == caracteresMasDosEspaciosCadaLadoPorLinea :
            newStr += "*\n"
    
    newStr += "* "
    
    for char in a:
        newStr += char
    
    newStr += " *\n"

    for i in range(caracteresMasDosEspaciosCadaLadoPorLinea):
        if i < caracteresMasDosEspaciosCadaLadoPorLinea :
            newStr += "*"
        elif i == caracteresMasDosEspaciosCadaLadoPorLinea :
            newStr += "*\n"
        
    print(newStr)