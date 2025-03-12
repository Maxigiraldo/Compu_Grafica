def ingresar_tuplas():
    lista_tuplas = []
    n = int(input("Ingrese la cantidad de personas: "))
    
    for _ in range(n):
        nombre = input("Ingrese el nombre: ").strip()
        edad = int(input("Ingrese la edad: ").strip())
        lista_tuplas.append((nombre, edad))

    return lista_tuplas

def ordenar_personas(lista):
    return sorted(lista, key=lambda persona: (persona[1], persona[0]))