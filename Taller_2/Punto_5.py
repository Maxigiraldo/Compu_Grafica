def conteo_palabras(texto):
    palabras = texto.split()
    diccionario = {}
    for palabra in palabras:
        palabra = palabra.lower().strip(".,")  # Limpia la palabra antes de procesarla
        if palabra in diccionario:
            diccionario[palabra] += 1
        else:
            diccionario[palabra] = 1
    return diccionario