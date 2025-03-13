import Libreria.image_processor as ip

def menu():
    print("Elija una opcion: ")
    print("1. Matriz de colores")
    print("2. Matriz de colores con filtro")
    print("3. Invertir colores de una imágen")
    print("4. Capa roja de una imágen")
    print("5. Capa verde de una imágen")
    print("6. Capa azul de una imágen") 
    print("7. Capa magenta de una imágen")
    print("8. Capa cyan de una imágen")
    print("9. Capa amarilla de una imágen")
    print("10. Sumar capas de una imágen")
    print("11. Fusionar imágenes")
    print("12. Ecualizar imágenes")
    print("13. Ecualizar imágen individual")
    print("14. Promediar imágen")
    print("15. Escala de grises por average")
    print("16. Escala de grises por luminosity")
    print("17. Escala de grises por midgray")
    print("18. Salir")

def main():
    path_avion = "Imagenes/avion.jpg"
    path_playa = "Imagenes/playa.jpg"
    path_pista = "Imagenes/pista.jpg"
    path_fondo = "Imagenes/fondo.jpg"
    path_utp = "Imagenes/utp.jpg"
    
    while True:
        menu()
        op = int(input("Opcion: "))
        if op == 1:
            ip.create_colors_image()
        elif op == 2:
            ip.create_image()
        elif op == 3:
            ip.invert_color(path_utp)
        elif op == 4:
            ip.red_cape(path_utp)
        elif op == 5:
            ip.green_cape(path_utp)
        elif op == 6:
            ip.blue_cape(path_utp)
        elif op == 7:
            ip.magenta_cape(path_utp)
        elif op == 8:
            ip.cyan_cape(path_utp)
        elif op == 9:
            ip.yellow_cape(path_utp)
        elif op == 10:
            ip.join_color(path_utp)
        elif op == 11:
            ip.fusion_images(path_avion, path_pista)
        elif op == 12:
            ip.fusion_images_fix(path_avion, path_pista)
        elif op == 13:
            ip.equalizate_image(path_playa)
        elif op == 14:
            ip.average(path_fondo)
        elif op == 15:
            ip.average_gray(path_fondo)
        elif op == 16:
            ip.luminosity(path_fondo)
        elif op == 17:
            ip.midgray(path_fondo)
        elif op == 18:
            print("Adios")
            break

if __name__ == '__main__':
    main()