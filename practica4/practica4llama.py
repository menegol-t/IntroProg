from practica4repo import repe, promedio2, promedio3, modulo, gritar, elevarCubo, cantDivisores, esPrimo, factoresPrimos, mayorDeDos, mayorDeTres
import math
# a = input("Ingresa una cadena: ")
x = float(input("Ingresa un numero decimal: "))
y = float(input("Ingresa un numero decimal: "))
z = float(input("Ingresa un numero decimal: "))

# print("\n Act 1) A)B)C)D)\n", math.sqrt(x), abs(x), abs(x-3), math.sqrt(abs(x-5)))
# print("\n Act 3)A)\n")
# repe(a)
# print("\n Act 4)A)\n", promedio2(x, y))
# print("\n Act 4)C)\n", promedio3(x, y, z))
# print("\nAct5\n", modulo(x))
# print("\nAct 6)C)\n", gritar("Ouch"))
# print("\nAct 7)C)\n")
# print(0, "al cubo:", elevarCubo(0))
# print(1, "al cubo:", elevarCubo(1))
# print(2, "al cubo:", elevarCubo(2))
# print(3, "al cubo:", elevarCubo(3))
# print(4, "al cubo:", elevarCubo(4))
# print(5, "al cubo:", elevarCubo(5))
# print(6, "al cubo:", elevarCubo(6))
# print(-1, "al cubo:", elevarCubo(-1))
# print(-2, "al cubo:", elevarCubo(-2))
# print(-3, "al cubo:", elevarCubo(-3))
# print(-4, "al cubo:", elevarCubo(-4))
# print(-5, "al cubo:", elevarCubo(-5))
#print("\nAct 8)A)\n", x, "tiene", cantDivisores(x), "divisores")
# print("\nAct 8)B)\n", x, "es primo.") if esPrimo(x) else print("\nAct 8)B)\n", x, "no es primo. ")
# print("\nAct 8)D)\n", x, "tiene los siguientes factores primos:")
# factoresPrimos(x)
# print("\nAct 9)A)\n", "el mayor entre", x, "y", y, "es", mayorDeDos(x, y))
# print("\nAct 9)B)\n", "el mayor entre", x, ",", z, "y", y, "es", mayorDeTres(x, y, z))
# print("\nAct 10)\n", potencia(x, y))
# print("\nAct 11)A)\n", sumaDeDivisores(x))
# print("\nAct 11)B)\n", x, "es perfecto.") if esPerfecto(x) else print("\nAct 11)B)\n", x, "no es perfecto.")
print("\nAct 11)C)\n", x, "es abundante.") if esAbundante(x) else print("\nAct 11)B)\n", x, "no es abundante.")
