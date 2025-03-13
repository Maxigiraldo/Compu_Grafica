import numpy as np

# Punto 1
array = np.array(range(1, 11))
array_reshape = array.reshape(2, 5)

print("Array reshaped:\n", array_reshape)
print("Forma:", array_reshape.shape)
print("Tamaño:", array_reshape.size)
print("Dimensiones:", array_reshape.ndim)

# Punto 2
a = np.array([1, 2, 3, 4, 5])
b = np.array([10, 20, 30, 40, 50])

suma = a + b
resta = a - b
producto = a * b
suma_total = np.sum(a)

print("Suma elemento a elemento:", suma)
print("Resta elemento a elemento:", resta)
print("Producto elemento a elemento:", producto)
print("Suma total de los elementos de 'a':", suma_total)

# Punto 3
data = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
quinto_elemento = data[4]
subseccion = data[2:7]

print("Quinto elemento:", quinto_elemento)
print("Subsección (índices 2 a 6):", subseccion)

# Punto 4
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
A_suma = A + 10
A_sqrt = np.sqrt(A)

print("Matriz original A:\n", A)
print("\nMatriz A + 10:\n", A_suma)
print("\nRaíz cuadrada de A:\n", A_sqrt)

# Punto 5
M = np.array([[1, 2, 3, 4, 5, 6]])
M_reshape = M.reshape(3, 2)
producto_punto = np.dot(M_reshape, M_reshape.T)

print("Matriz original M:\n", M)
print("\nMatriz M reshaped (3x2):\n", M_reshape)
print("\nProducto punto de M y su transpuesta:\n", producto_punto)

# Punto 6
data = np.array([1, 2, np.nan, 4, 5, np.nan, 7, 8, 9])
data_sin_nan = np.nan_to_num(data, nan=0)
media = np.mean(data_sin_nan)

print("Array original con NaN:\n", data)
print("\nArray después de reemplazar NaN por 0:\n", data_sin_nan)
print("\nMedia del array resultante:", media)

# Punto 7
data = np.array([10, 20, 30, 40, 50])
np.save('mi_array.npy', data)
data_cargado = np.load('mi_array.npy')

print("Array original:\n", data)
print("\nArray cargado desde el archivo:\n", data_cargado)