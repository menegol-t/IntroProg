print("\nAct 15)A)")
a = int(input("Ingresa un numero para la secuencia: "))
resultadoAnterior = 0
for i in range(1, a + 1) :
    print((2 * i) + resultadoAnterior)
    resultadoAnterior = (2 * i) + resultadoAnterior

print("\nAct 15)B)")
b = int(input("Ingresa un numero para la secuencia: "))
resultadoAnterior = 0
for i in range(1, b + 1) :
    print((i ** 2) + resultadoAnterior)
    resultadoAnterior = (i ** 2) + resultadoAnterior


print("\nAct 15)C)")
c = int(input("Ingresa un numero para la secuencia: "))
resultadoAnterior = 0
for i in range(1, c + 1) :
    print((i ** 3 - i ** 2) + resultadoAnterior)
    resultadoAnterior = (i ** 3 - i ** 2) + resultadoAnterior

print("\nAct 15)D)")
d = int(input("Ingresa un numero para la secuencia: "))
resultadoAnterior = 0
for i in range(1, d + 1) :
    print((1/(i ** 2)) + resultadoAnterior)
    resultadoAnterior = (1/(i ** 2)) + resultadoAnterior

# x = input("Tu contraseña es: ")
# while x != "misuperpassword" : 
#     x = input("Tu contraseña es incorrecta, ingresa otra vez: ")
# print("Bienvenido!")
