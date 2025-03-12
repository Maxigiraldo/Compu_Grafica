import os

def ejecutar_ejercicio(nombre_archivo):
    """Ejecuta un script de ejercicio dado su nombre de archivo."""
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, encoding="utf-8") as f:
            exec(f.read())
    else:
        print(f"El archivo {nombre_archivo} no existe.")

def menu():
    while True:
        print("\n--- MENÚ DE EJERCICIOS ---")
        print("1. Creación y Propiedades de Arrays")
        print("2. Operaciones Básicas")
        print("3. Indexación y Slicing")
        print("4. Broadcasting y Funciones Universales")
        print("5. Manipulación de Formas y Álgebra Lineal")
        print("6. Trabajo con Datos Faltantes")
        print("7. Guardar y Cargar Arrays")
        print("8. Salir")
        
        opcion = input("Selecciona una opción (1-8): ")

        if opcion == "1":
            ejecutar_ejercicio("Punto_1.py")
        elif opcion == "2":
            ejecutar_ejercicio("Punto_2.py")
        elif opcion == "3":
            ejecutar_ejercicio("Punto_3.py")
        elif opcion == "4":
            ejecutar_ejercicio("Punto_4.py")
        elif opcion == "5":
            ejecutar_ejercicio("Punto_5.py")
        elif opcion == "6":
            ejecutar_ejercicio("Punto_6.py")
        elif opcion == "7":
            ejecutar_ejercicio("Punto_7.py")
        elif opcion == "8":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intenta nuevamente.")

if __name__ == "__main__":
    menu()
