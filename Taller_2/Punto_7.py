def parentesis(cadena):
    parentesis = 0
    for i in cadena:
        if i == "(":
            parentesis += 1
        elif i == ")":
            parentesis -= 1
        if parentesis < 0:
            print("Secuencia invalida")
    if parentesis != 0:
        print("Secuencia invalida")
    else:
        print("Secuencia valida")
