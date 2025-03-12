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
    print("Que opcion desea realizar?")
    print("1. Array unidimensional")
    print("2. Array multidimensional")
    print("3. Operaciones básicas con arrays")
    print("4. Funciones matematicas")
    print("5. Indexación y segmentacion")
    print("6. Datos aleatorios")
    print("7. Agregación")
    print("8. Funciones de fábrica")
    print("9. Alineación y broadcasting")
    print("10. Transformaciones y redimensionamiento")
    print("11. Salir")
    
    
def main():
    while True:
        menu()
        opcion = int(input("Ingrese la opcion: "))
        if opcion == 1:
            Punto_1.crear_array_unidimensional()
        elif opcion == 2:
            Punto_2.array_multidimensional()
        elif opcion == 3:
            Punto_3.sumar_arrays()
        elif opcion == 4:
            Punto_4.exponencial()
        elif opcion == 5:
            Punto_5.array_pares()
        elif opcion == 6:
            Punto_6.array_aleatorio()
        elif opcion == 7:
            Punto_7.agregacion()
        elif opcion == 8:
            Punto_8.fabrica()
        elif opcion == 9:
            Punto_9.alineacion_broadcasting()
        elif opcion == 10:
            Punto_10.transformar_arrays()
        elif opcion == 11:
            break
        else:
            print("Opcion invalida")

if __name__ == "__main__":
    main()