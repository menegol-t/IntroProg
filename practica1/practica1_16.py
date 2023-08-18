#16)A)Determinar cuántos segundos tiene una hora, y cuántos tiene un día
print("\nact 16)A)")
segundosEnUnMinuto = 1 * 60
segundosPorHora = int(segundosEnUnMinuto * 60)
segundosPorDia = int(segundosPorHora * 24)
print("En una hora hay", segundosPorHora, "segundos. En un dia hay", segundosPorDia, "segundos.")
#16)B)Escribir una expresión matemática que transforme un lapso de tiempo expresado en segundos a uno expresado en minutos
print("\nact 16)B)")
tiempoEnSegundos = int(input("Ingrese los segundos: "))
tiempoEnMinutos = tiempoEnSegundos/60
print("Hay", tiempoEnMinutos, "minutos en", tiempoEnSegundos, "segundos.")
#16)C)Escribir otra para transformar a horas y una última que transforme a días.
print("\nact 16)C)")
tiempoEnHoras = tiempoEnMinutos/60
tiempoEnDias = tiempoEnHoras/24
print("Hay", tiempoEnHoras, "horas o", tiempoEnDias, "dias en", tiempoEnSegundos, "segundos.")