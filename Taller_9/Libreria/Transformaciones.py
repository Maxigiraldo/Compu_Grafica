import numpy as np
import matplotlib.pyplot as plt

def create_img(path):
    return np.array(plt.imread(path))

def normalizar(img):
    img_n = img/255
    return img_n

def gris(img):
    img_gris = np.mean(img, axis=2)
    return img_gris

def brightness_adjust(img, factor):
    img_ab = img + factor # Ajuste brillo
    plt.imshow(img_ab)
    plt.title('Ajuste brillo')
    plt.axis('off')
    plt.show()

def adjust_cape_brightness(img, factor, cape):
    img_ab = img + factor
    img_acb = np.copy(img)
    img_acb[:,:,cape] = img_ab[:,:,cape]
    plt.imshow(img_acb)
    plt.title('Ajustar brillo de canal')
    plt.axis('off')
    plt.show()

def contrast_adjust(img, factor):
    img_acd = factor * np.log10(1 + img) 
    img_acl = factor * np.exp(img - 1) 
    plt.subplot(1, 2, 1)
    plt.imshow(img_acd)
    plt.title('Ajustar contraste')
    plt.axis('off')
    plt.subplot(1, 2, 2)
    plt.imshow(img_acl)
    plt.title('Ajustar contraste')
    plt.axis('off')
    plt.show()


def binary(img, umbral):
    img_gris = gris(img)
    img_bin = img_gris > umbral # Binarización
    plt.imshow(img_bin, cmap='gray')
    plt.title('Imagen binarizada')
    plt.axis('off')
    plt.show()

def snip(img, x1, y1, x2, y2):
    img_snip = img[x1:x2, y1:y2]
    plt.imshow(img_snip)
    plt.title('Recorte de imagen')
    plt.axis('off')
    plt.show()

def rotate(img, ang):
    rad = np.radians(ang)
    img_rot = np.zeros_like(img)
    x, y = img.shape[:2] # Dimensiones de la imagen
    x_c, y_c = x//2, y//2 # Centro de la imagen
    for i in range(x):
        for j in range(y):
            x_r = int((i - x_c) * np.cos(rad) - (j - y_c) * np.sin(rad) + x_c) # Rotación
            y_r = int((i - x_c) * np.sin(rad) + (j - y_c) * np.cos(rad) + y_c) 
            if x_r >= 0 and x_r < x and y_r >= 0 and y_r < y:
                img_rot[x_r, y_r] = img[i, j]
    plt.imshow(img_rot, cmap='gray')
    plt.title('Rotar imagen')
    plt.axis('off')
    plt.show()

def RGB_Histogram(img):
    R = img[:,:,0] # Capa roja
    G = img[:,:,1] # Capa verde
    B = img[:,:,2] # Capa azul
    plt.subplot(1, 3, 1)
    plt.hist(R.ravel(), bins=256, color='red', alpha=0.5)
    plt.title('Rojo')
    plt.subplot(1, 3, 2)
    plt.hist(G.ravel(), bins=256, color='green', alpha=0.5)
    plt.title('Verde')
    plt.subplot(1, 3, 3)
    plt.hist(B.ravel(), bins=256, color='blue', alpha=0.5)
    plt.title('Azul')
    plt.show()

def translation(img, x, y):
    img_tr = np.zeros_like(img)
    i, j = img.shape[:2] # Dimensiones de la imagen
    img_tr[x:, y:] = img[:i-x, :j-y]
    plt.imshow(img_tr)
    plt.title('Traslación')
    plt.axis('off')
    plt.show()

def zoom(img, factor):
    x, y = img.shape[:2]
    x_c, y_c = x//2, y//2 # Centro de la imagen
    x_start, x_end = x_c - int(x_c * factor), x_c + int(x_c * factor)
    y_start, y_end = y_c - int(y_c * factor), y_c + int(y_c * factor)
    img_z = img[x_start:x_end, y_start:y_end]
    plt.imshow(img_z)
    plt.title('Zoom')
    plt.axis('off')
    plt.show()

