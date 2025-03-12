import Punto_1
import Punto_2
import Punto_3
import Punto_4
import Punto_5
import Punto_6
import Punto_7
import Punto_8
import Punto_9
import Punto_10

def menu():
    print("Seleccione una opción:")
    print("1. Operaciones básicas")
    print("2. Filtrado por pares")
    print("3. Convertir de Celsius a Fahrenheit")
    print("4. Sistema de calificaciones a letras")
    print("5. Conteo de palabras en una cadena")
    print("6. Busqueda de elemntos en una lista")
    print("7 Validacion de secuencias de parentesis")
    print("8. Ordenamiento de tuplas")
    print("9. Generador de contraseñas aleatorias")
    print("10. Agenda de contactos")
    print("11. Salir")

def main():
    while True:
        menu()
        opcion = int(input("Ingrese una opción: "))
        if opcion == 1:
            Punto_1.menu()
        elif opcion == 2:
            lista = list(map(int, input("Ingrese una lista de números separados por espacios: ").split()))
            print(Punto_2.filtrado(lista))
        elif opcion == 3:
            lista_celsius = list(map(float, input("Ingrese una lista de temperaturas en celsius separados por espacios: ").split()))            
            print(Punto_3.celsius_fahrenheit(lista_celsius))
        elif opcion == 4:
            lista_calificaciones = list(map(float, input("Ingrese una lista de calificaciones separados por espacios: ").split()))
            print(Punto_4.calificaciones(lista_calificaciones))
        elif opcion == 5:
            cadena = input("Ingrese una cadena de texto: ")
            print(Punto_5.conteo_palabras(cadena))
        elif opcion == 6:
            lista = input("Ingrese una lista de elementos separados por espacios: ").split()
            elemento = input("Ingrese el elemento a buscar: ")
            print(f"El elemento se encuentra en el indice: {Punto_6.buscar_elemento(lista, elemento)}")
        elif opcion == 7:
            secuencia = input("Ingrese una secuencia de parentesis: ")
            Punto_7.parentesis(secuencia)
        elif opcion == 8:
            lista_tuplas = Punto_8.ingresar_tuplas()
            print(Punto_8.ordenar_personas(lista_tuplas))
        elif opcion == 9:
            longitud = int(input("Ingrese la longitud de la contraseña: "))
            print(Punto_9.generar_contrasena(longitud))
        elif opcion == 10:
            Punto_10.main()
        elif opcion == 11:
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    main()