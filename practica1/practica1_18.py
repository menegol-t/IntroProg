tiempoEnSegundos = int(input("Ingrese los segundos: "))

diasEnSegundos = tiempoEnSegundos // (60 * 60 * 24)
restoDias = tiempoEnSegundos % (60 * 60 * 24)

horasEnSegundos = restoDias // (60 * 60)
restoHoras = restoDias % (60 * 60)

minutosEnSegundos = restoHoras // 60
restoMinutos = restoHoras % 60

print("Hay", diasEnSegundos, "dias,", horasEnSegundos, "horas,", minutosEnSegundos, "minutos,", restoMinutos, "segundos en ", tiempoEnSegundos, "segundos.")