def calificaciones(lista):
    calificaciones = []
    for calificacion in lista:
        if calificacion >= 0 and calificacion <= 2.9:
            calificaciones.append("F")
        elif calificacion >= 3 and calificacion <= 3.4:
            calificaciones.append("D")
        elif calificacion >= 3.5 and calificacion <= 3.9:
            calificaciones.append("C")
        elif calificacion >= 4 and calificacion <= 4.4:
            calificaciones.append("B")
        elif calificacion >= 4.5 and calificacion <= 5:
            calificaciones.append("A")
    return calificaciones