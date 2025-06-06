import numpy as np
import matplotlib.pyplot as plt

def create_image(img_1, img_2, img_3, img_4, factor):
    '''
    Función que crea un fondo que al que se le añaden 4 imágenes recortadas y guarda la imágen
    '''
    ancho_inicio = 50
    ancho_final = 200
    largo_inicio = 50
    largo_final = 300
    
    size = [550, 650, 3]
    fondo = np.ones(size, dtype = np.uint8) * 255
    fondo[:, :] = fondo[:, :] * factor
    
    img_recorte_1 = img_1[ancho_inicio : ancho_final, largo_inicio : largo_final, :]
    img_recorte_2 = img_2[ancho_inicio : ancho_final, largo_inicio : largo_final, :]
    img_recorte_3 = img_3[ancho_inicio + 700 : ancho_final + 700, largo_inicio + 500 : largo_final + 500, :]
    img_recorte_4 = img_4[ancho_inicio : ancho_final, largo_inicio : largo_final, :]
    x, y = img_recorte_1.shape[ :2]
    
    for i in range(x):
        for j in range(y):
                fondo[i + 100, j + 50, :] = img_recorte_1[i, j, :]
                fondo[i + 300, j + 50, :] = img_recorte_2[i, j, :] 
                fondo[i + 100, j + 350, :] = img_recorte_3[i, j, :]
                fondo[i + 300, j + 350, :] = img_recorte_4[i, j, :]
    
    plt.imshow(fondo)
    plt.axis('off')
    plt.savefig('img_new.jpg')
    plt.show()

def join(img_5, img_n):
    '''
    Función que junta dos imágenes a partir del centro
    '''
    ancho, largo = img_5.shape[:2]
    x, y = img_n.shape[:2]
    
    x_centro = (x-ancho) // 2
    y_centro = (y-largo) // 2

    for i in range(ancho):
        for j in range(largo):
                img_n[x_centro + i, y_centro + j ] = (img_n[x_centro + i, y_centro + j ] * (1 - 0.5)) + img_5[i, j] * 0.5
    plt.imshow(img_n)
    plt.axis('off')
    plt.show()

def main():
    img_1 = np.array(plt.imread('aura.jpg'), dtype = np.uint8)
    img_2 = np.array(plt.imread('barcos.jpg'), dtype = np.uint8)
    img_3 = np.array(plt.imread('fondo.jpg'), dtype = np.uint8)
    img_4 = np.array(plt.imread('red.jpg'), dtype = np.uint8)
    img_5 = np.array(plt.imread('tux.jpg'), dtype = np.uint8)
    factor = float(input("Ingrese el factor para el color del fondo: "))
    create_image(img_1, img_2, img_3, img_4, factor)
    img_n = np.array(plt.imread('img_new.jpg'), dtype = np.uint8)
    join(img_5, img_n)
    
if __name__ == '__main__':
    main()
