#13) Suponga que una persona desea invertir su capital en un banco y quiere saber cuánto dinero tendrá en su cuenta si el banco incrementa el 6 % mensual(no acumulativo). Se le debe pedir al usuario el capital a invertir y la cantidad de meses. Por ejemplo, si invierte 500 mil pesos por 4 meses el banco debería devolverle 620 mil pesos.
print("\nact 13)")
capital = float(input("Ingrese el capital a invertir: $"))
months = int(input("Por cuantos meses lo va a invertir: "))
incremento = (capital * 0.06) * months
print("Devolucion: $", incremento + capital)

#14) Una empresa telefónica desea un programa para calcular el importe de sus clientes. Sabiendo que el costo por comunicación es de $12 y por cada segundo se cobra $1, 5 hacer dicho programa. Se deben ingresar la cantidad de llamadas realizadas y el tiempo total de comunicación, el programa debe devolver el precio a cobrar. Por ejemplo, si realizó 10 llamadas con un total de 4000 segundos el importe a pagar sería de $6120
print("\nact 14)")
totalLlamadas = int(input("Ingrese el total de llamadas realizadas: "))
segundosTotales = int(input("Ingrese el total de segundos que duraron las llamadas: "))
print("Importe a pagar es: $", (totalLlamadas * 12) + (segundosTotales * 1.5))

#15) Un vendedor recibe un sueldo base de $42000 más un 10 % extra del total de sus ventas, el vendedor desea saber cuánto dinero obtendrá en total en el mes si ha logrado realizar 3 ventas este mes. Tenga en cuenta el sueldo básico y la comisión por las ventas. Hacer un programa que solicite el monto de cada una de las ventas del mes e indique cuál será el sueldo nal del vendedor. Por ejemplo, si realizó una venta de $12000, otra de $6000 y una tercera de $22000 su sueldo será de $46000
print("\nact 15)")
venta1 = float(input("Valor de la primera venta: $")) * 0.10
venta2 = float(input("Valor de la segunda venta: $")) * 0.10
venta3 = float(input("Valor de la tercera venta: $")) * 0.10
base = 42000
sueldoFinal = base + venta1 + venta2 + venta3
print("Su sueldo sera: $", sueldoFinal)