def producto_escalar(v1, v2):
    if len(v1) == len(v2):
        return sum([v1[i] * v2[i] for i in range(len(v1))])
    else:
        return 'Los vectores deben tener la misma longitud'
