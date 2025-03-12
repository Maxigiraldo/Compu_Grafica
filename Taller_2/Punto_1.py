def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a / b

def menu():
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    op = int(input("Ingrese la operación que desea realizar: "))
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))
    if op == 1:
        print(suma(a, b))
    elif op == 2:
        print(resta(a, b))
    elif op == 3:
        print(multiplicacion(a, b))
    elif op == 4:
        print(division(a, b))
    else:
        print("Operación no válida")