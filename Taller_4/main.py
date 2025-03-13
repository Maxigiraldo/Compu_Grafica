import numpy as np

# Punto 1
array_unidimensional = np.arange(1, 11)
print(array_unidimensional)

# Punto 2
matriz_2d = np.arange(1, 10).reshape(3, 3)
print(matriz_2d)

# Punto 3
array1 = np.arange(1, 6)
array2 = np.arange(1, 6)
resultado = array1 + array2
print(resultado)

# Punto 4
array_exp = np.arange(1, 6)
exponencial = np.exp(array_exp)
print(exponencial)

# Punto 5
array = np.arange(1, 11)
pares = array[array % 2 == 0]
print(pares)

# Punto 6
array_aleatorio = np.random.rand(10)
print(array_aleatorio)

# Punto 7
array = np.arange(1, 6)
media = np.mean(array)
print(media)

# Punto 8
array_sietes = np.full(5, 7)
print(array_sietes)

# Punto 9
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
resultado = array1 + array2
print(resultado)

# Punto 10
array = np.arange(1, 7)
matriz = array.reshape(2, 3)
print(matriz)