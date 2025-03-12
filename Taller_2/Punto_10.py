def agregar_contacto(agenda, nombre, telefono):
    agenda[nombre] = telefono
    return agenda

def eliminar_contacto(agenda, nombre):
    agenda.pop(nombre)
    return agenda

def buscar_contacto(agenda, nombre):
    if nombre in agenda:
        return agenda[nombre]
    else:
        return "El contacto no existe"
    
def mostrar_contactos(agenda):
    for nombre, telefono in agenda.items():
        print(f"Nombre: {nombre}, Telefono: {telefono}")
    return

def main():
    agenda = {}
    print("Bienvenido a la agenda")
    while True:
        print("1. Agregar contacto")
        print("2. Eliminar contacto")
        print("3. Buscar contacto")
        print("4. Mostrar contactos")
        print("5. Salir")
        opcion = int(input("Ingrese una opción: "))
        if opcion == 1:
            nombre = input("Ingrese el nombre: ")
            telefono = input("Ingrese el telefono: ")
            agenda = agregar_contacto(agenda, nombre, telefono)
        elif opcion == 2:
            nombre = input("Ingrese el nombre: ")
            agenda = eliminar_contacto(agenda, nombre)
        elif opcion == 3:
            nombre = input("Ingrese el nombre: ")
            print(buscar_contacto(agenda, nombre))
        elif opcion == 4:
            mostrar_contactos(agenda)
        elif opcion == 5:
            break
        else:
            print("Opción inválida")