#La empresa que administra los cajeros automáticos lo contrata para que programen la entrega de billetes, el usuario ingresa la cantidad de dinero que desea y usted debe indicar cuantos billetes de cada denominación se debe entregar. Es importante entregar siempre la menor cantidad de billetes. Ayuda: El operador % da el resto de la división a/b, y el operador // da la parte entera del cociente de a/b.
cantDinero = int(input("Cuanto dinero quiere retirar: $"))
billetesDe2000 = cantDinero // 2000
restoDe2000 = cantDinero % 2000

billetesDe1000 = restoDe2000 // 1000
restoDe1000 = restoDe2000 % 1000

billetesDe500 = restoDe1000 // 500
restoDe500 = restoDe1000 % 500

billetesDe200 = restoDe500 // 200
restoDe200 = restoDe500 % 200

billetesDe100 = restoDe200 // 100
restoDe100 = restoDe200 % 100

billetesDe50 = restoDe100 // 50
restoDe50 = restoDe100 % 50

billetesDe20 = restoDe50 // 20
restoDe20 = restoDe50 % 20

billetesDe10 = restoDe20 // 10
restoDe10 = restoDe20 % 10

billetesDe5 = restoDe10 // 5
restoDe5 = restoDe10 % 5

billetesDe2 = restoDe5 // 2
restoDe2 = restoDe5 % 2

print("Cantidad de billetes a entregar: \n$2000:", billetesDe2000, "\n$1000:", billetesDe1000, "\n$500:", billetesDe500, "\n$200:", billetesDe200, "\n$100:", billetesDe100, "\n$50:", billetesDe50, "\n$20:", billetesDe20, "\n$10:", billetesDe20, "\n$5:", billetesDe5, "\n$2:", billetesDe2)