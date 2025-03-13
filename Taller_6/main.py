import numpy as np
import matplotlib.pyplot as plt

# Punto 1
array_A = np.arange(1, 16)
array_A = array_A.reshape(3, 5)

# Punto 2
suma = np.sum(array_A)
media = np.mean(array_A)
producto = np.prod(array_A)
print(f"Suma: {suma}\nMedia: {media}\nProducto: {producto}")

# Punto 3
print(array_A[1, 1:3])

# Punto 4
array_B = array_A[array_A > 7]
print(array_B)

# Punto 5
array_C = np.array([[4, 26, 17], [3, 10, 7], [11, 3, 2]])
determinante = np.linalg.det(array_C)
print(f"Determinante: {determinante}")
inversa = np.linalg.inv(array_C)
print(f"Inversa:\n{inversa}")

# Punto 6
array_D = np.random.randint(1, 50, 100)
max = np.max(array_D, axis=0)
min = np.min(array_D, axis=0)
media = np.mean(array_D)
desviacion = np.std(array_D)
print(f"Max: {max}\nMin: {min}\nMedia: {media}\nDesviación estándar: {desviacion}")

# Punto 7
x1 = np.linspace(-2*np.pi, 2*np.pi, 100)
y1 = np.sin(x1)

x2 = np.linspace(-2*np.pi, 2*np.pi, 100)
y2 = np.cos(x2)

plt.plot(x1, y1, label="y = sin(x)")
plt.plot(x2, y2, label="y = cos(x)")
plt.title("Funciones seno y coseno")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

# Punto 8
x = np.arange(1, 101)
y = array_D
plt.scatter(x, y)
plt.title("Gráfico de dispersión")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

# Punto 9
plt.hist(array_D, bins=50)
plt.title("Histograma")
plt.show()

# Punto 10
img = np.array(plt.imread("Playa.jpg"))
img_gray = np.mean(img, axis=2)
plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title("Imagen original")
plt.axis("off")
plt.subplot(1, 2, 2)
plt.imshow(img_gray, cmap="gray")
plt.title("Imagen en escala de grises")
plt.axis("off")
plt.show()
