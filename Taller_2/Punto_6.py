def buscar_elemento(lista, elemento):
    len_lista = len(lista)
    for i in range(len_lista):
        if lista[i] == elemento:
            return i + 1
    return -1