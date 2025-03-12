import numpy as np
import matplotlib.pyplot as plt

def normalizar(img):
    img_n = img/255
    return img_n

def brightness_adjust(img, factor):
    img_ab = img + factor
    plt.imshow(img_ab)
    plt.title('Aumentar brillo')
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
    img_ac = (img_acd) + (img_acl)
    # plt.imshow(img_ac)
    plt.subplot(1, 2, 1)
    plt.imshow(img_acd)
    plt.title('Ajustar contraste')
    plt.axis('off')
    plt.subplot(1, 2, 2)
    plt.imshow(img_acl)
    plt.title('Ajustar contraste')
    plt.axis('off')
    plt.show()

img = np.array(plt.imread('../fondo.jpg'))
img_n = normalizar(img)

contrast_adjust(img_n, 0.8)

