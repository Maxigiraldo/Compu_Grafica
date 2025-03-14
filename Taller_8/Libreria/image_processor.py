import numpy as np
import matplotlib.pyplot as plt

def create_colors_image():
    '''
    Crea una matriz 3x3 y la rellena de colores
    '''
    matriz = np.ones((3,3,3))
    matriz[0,2,1] = matriz[0,2,2] = 0
    matriz[1,2,0] = matriz[1,2,2] = 0
    matriz[2,2,0] = matriz[2,2,1] = 0
    matriz[1,1,:] = 0.5
    matriz[2,1,:] = 0
    matriz[0,0,0] = 0
    matriz[1,0,1] = 0
    matriz[2,0,2] = 0

    plt.imshow(matriz)

    plt.show()
def create_image():    
    '''
    Crea una matriz de colores semejando al que se hace en la tv
    '''
    matriz=np.ones((8,11,3)) 
    matriz[:6,0,2]=0 
    matriz [:6,1:3,0]=0 
    matriz [:6,3:5,0]=matriz[:6,3:5,2]=0 
    matriz [:6,5:7,1]=0 
    matriz[:6,7:9,1]=matriz[:6,7:9,2]=0 
    matriz[:6,9:11,1]=matriz [:6,9:11,0]=0 
    matriz [6:8,1,:]=0.9 
    matriz [6:8,2,:]=0.7 
    matriz [6:8,3,:]=0.6 
    matriz [6:8,4,:]=0.5 
    matriz [6:8,5,:]=0.3 
    matriz [6:8,6,:]=0.2 
    matriz [6:8,7,:]=0.1 
    matriz [6:8,8,:]=0.1 
    matriz [6:8,9,:]=0.1 
    matriz [6:8,10,:]=0.1

    factor=0.6
    matriz=matriz*factor 

    plt.imshow(matriz) 

    plt.axis("off") 

    plt.show() 
    
def invert_color(path):
    '''
    Invierte los colores de una imagen
    '''
    imagen = np.array(plt.imread(path))

    imagen_invertida = 1 - (imagen/255)

    plt.imshow(imagen_invertida)
    plt.axis("off")
    plt.show()

def red_cape(path):
    '''
    Cambia los colores de una imagen a rojo
    '''
    imagen = np.array(plt.imread(path))/255 # Normalizar la imagen

    imagen[:,:,1] = imagen[:,:,2] = 0

    plt.imshow(imagen)
    plt.axis("off")
    plt.show()
    
def green_cape(path):
    '''
    Cambia los colores de una imagen a verde
    '''
    imagen = np.array(plt.imread(path))/255 # Normalizar la imagen

    imagen[:,:,0] = imagen[:,:,2] = 0

    plt.imshow(imagen)
    plt.axis("off")
    plt.show()

def blue_cape(path):
    '''
    Cambia los colores de una imagen a azul
    '''
    imagen = np.array(plt.imread(path))/255 # Normalizar la imagen

    imagen[:,:,1] = imagen[:,:,0] = 0

    plt.imshow(imagen)
    plt.axis("off")
    plt.show()
    
def magenta_cape(path):
    '''
    Cambia los colores de una imagen a magenta
    '''
    imagen = np.array(plt.imread(path))/255 # Normalizar la imagen

    imagen[:,:,1] = 0

    plt.imshow(imagen)
    plt.axis("off")
    plt.show()

def cyan_cape(path):
    '''
    Cambia los colores de una imagen a cyan
    '''
    imagen = np.array(plt.imread(path))/255 # Normalizar la imagen

    imagen[:,:,0] = 0

    plt.imshow(imagen)
    plt.axis("off")
    plt.show()
    
def yellow_cape(path):
    '''
    Cambia los colores de una imagen a amarillo
    '''
    imagen = np.array(plt.imread(path))/255 # Normalizar la imagen

    imagen[:,:,2] = 0

    plt.imshow(imagen)
    plt.axis("off")
    plt.show()
    
def join_color(path):
    '''
    Une las capas de color de una imagen
    '''
    imagen = np.array(plt.imread(path))/255 # Normalizar la imagen

    capa_roja = np.copy(imagen)
    capa_roja[:,:,1] = capa_roja[:,:,2] = 0
    capa_verde = np.copy(imagen)
    capa_verde[:,:,0] = capa_verde[:,:,2] = 0
    capa_azul = np.copy(imagen)
    capa_azul[:,:,0] = capa_azul[:,:,1] = 0

    capa_original = capa_roja + capa_verde + capa_azul

    plt.subplot(1,4,1)
    plt.imshow(capa_roja)
    plt.axis("off")
    plt.subplot(1,4,2)
    plt.imshow(capa_verde)
    plt.axis("off")
    plt.subplot(1,4,3)
    plt.imshow(capa_azul)
    plt.axis("off")

    plt.subplot(1,4,4)
    plt.imshow(capa_original)
    plt.axis("off")

    plt.show()
    
def fusion_images(path1, path2):
    '''
    Ecualiza dos imagenes
    '''
    img_1 = np.array(plt.imread(path1))/255
    img_2 = np.array(plt.imread(path2))/255

    img_3 = img_1 + img_2

    plt.imshow(img_3)
    plt.axis("off")
    plt.show()
    
def fusion_images_fix(path1, path2):
    '''
    Fusiona dos imagenes
    '''
    
    img_1 = np.array(plt.imread(path1))/255
    img_2 = np.array(plt.imread(path2))/255

    factor = 0.3

    img_3 = img_1*factor + img_2*(1-factor)

    plt.imshow(img_3)
    plt.axis("off")
    plt.show()

def equalizate_image(path):
    '''
    Ecualiza una imagen
    '''
    img_1 = np.array(plt.imread("playa.jpg"))/255

    factor = 0.3

    img_ecualizada = img_1 * factor

    plt.subplot(1, 2, 1)
    plt.imshow(img_1)
    plt.axis("off")
    plt.title("Imagen original")

    plt.subplot(1, 2, 2)
    plt.imshow(img_ecualizada)
    plt.axis("off")
    plt.title("Imagen ecualizada")

    plt.axis("off")
    plt.show()

def average(path):
    '''
    Promedia los colores de una imagen
    '''
    imagen = np.array(plt.imread(path))/255 # Normalizar la imagen

    capa_grises = np.mean(imagen, axis=2) #average

    plt.imshow(capa_grises)
    plt.axis("off")

    plt.show()
    
def average_gray(path):
    '''
    Promedia los colores de una imagen y la convierte a escala de grises
    '''
    imagen = np.array(plt.imread(path))/255 # Normalizar la imagen

    capa_grises = np.mean(imagen, axis=2) #average

    plt.imshow(capa_grises, cmap="gray")
    plt.axis("off")

    plt.show()
    
def luminosity(path):
    '''
    Convierte una imagen a escala de grises con la tecnica luminosity
    '''
    imagen = np.array(plt.imread(path))/255 # Normalizar la imagen

    capa_grises =  0.2989*imagen[:,:,0] + 0.5870*imagen[:,:,1] + 0.1140*imagen[:,:,2] #luminosity

    plt.imshow(capa_grises, cmap="gray")
    plt.axis("off")

    plt.show()
    
def midgray(path):
    '''
    Convierte una imagen a escala de grises con la tecnica midgray
    '''
    imagen = np.array(plt.imread(path))/255 # Normalizar la imagen

    capa_grises = (np.maximum(imagen[:,:,0], imagen[:,:,1], imagen[:,:,2]) + np.minimum(imagen[:,:,0], imagen[:,:,1], imagen[:,:,2])) / 2 # midgray

    plt.imshow(capa_grises, cmap="gray")
    plt.axis("off")

    plt.show()