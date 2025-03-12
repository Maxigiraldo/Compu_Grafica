def suma_vectorial(v1, v2):
    if len(v1) == len(v2):
        return [v1[i] + v2[i] for i in range(len(v1))]
    else:
        return 'Los vectores deben tener la misma longitud'