import Libreria.Transformaciones as tr

def menu():
    print('Selecciona una opción:')
    print('1. Ajuste de brillo')
    print('2. Ajuste canal')
    print('3. Ajuste de contraste')
    print('4. Zoom imágen')
    print('5. Binarizar imágen')
    print('6. Rotar imágen')
    print('7. Histograma RGB')
    print('8. Traslación')
    print('9. Recorte de imágen')
    print('10. Salir')

def main():
    path = 'fondo.jpg'
    img = tr.create_img(path)
    img_n = tr.normalizar(img)
    img_gris = tr.gris(img)
    while True:
        menu()
        opcion = int(input())
        if opcion == 1:
            factor = float(input('Ingrese el factor de brillo en valores entre 0 y 1: '))
            tr.brightness_adjust(img_n, factor)
        elif opcion == 2:
            print('0. Rojo')
            print('1. Verde')
            print('2. Azul')
            cape = int(input('Ingrese el canal a ajustar (0, 1, 2): '))
            factor = float(input('Ingrese el factor de brillo en valores entre 0 y 1: '))
            tr.adjust_cape_brightness(img_n, factor, cape)
        elif opcion == 3:
            factor = float(input('Ingrese el factor de contraste en valores entre 0 y 1: '))
            tr.contrast_adjust(img_n, factor)
        elif opcion == 4:
            factor = float(input('Ingrese el factor de zoom: '))
            tr.zoom(img_n, factor)
        elif opcion == 5:
            umbral = float(input('Ingrese el umbral para binarizar la imágen: '))
            tr.binary(img_n, umbral)
        elif opcion == 6:
            ang = float(input('Ingrese el ángulo de rotación: '))
            tr.rotate(img_gris, ang)
        elif opcion == 7:
            tr.RGB_Histogram(img)
        elif opcion == 8:
            x = int(input('Ingrese el valor de traslación en x: '))
            y = int(input('Ingrese el valor de traslación en y: '))
            tr.translation(img, x, y)
        elif opcion == 9:
            x1 = int(input('Ingrese el punto x1: '))
            y1 = int(input('Ingrese el punto y1: '))
            x2 = int(input('Ingrese el punto x2: '))
            y2 = int(input('Ingrese el punto y2: '))
            tr.snip(img_n, x1, y1, x2, y2)
        elif opcion == 10:
            print('Adios')
            break
        else:
            print('Opción no válida')

if __name__ == '__main__':
    main()