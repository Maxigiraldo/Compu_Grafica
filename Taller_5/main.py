import numpy as np

# Punto 1 
vector_A = np.array([2,3,5,1,4,7,9,8,6,10])

# Punto 2
vector_B = np.arange(11,21)

# Punto 3
vector_C = np.concatenate((vector_A, vector_B))
print("Vector concatenado: ", vector_C)

# Punto 4
minimo = np.min(vector_C)
print("Minimo: ", minimo)

# Punto 5
maximo = np.max(vector_C)
print("Maximo: ", maximo)

# Punto 6
longitud = len(vector_C)
print("Longitud: ", longitud)

# Punto 7
suma = 0
for num in vector_C:
    suma += num
division = suma / longitud
print("Promedio: ", division)

# Punto 8
promedio = np.average(vector_C)
print("Promedio: ", promedio)

# Punto 9
media = np.mean(vector_C)
print("Media: ", media)

# Punto 10
suma_vector = np.sum(vector_C)
print("Suma elementos: ", suma_vector)

# Punto 11
vector_D = np.array(vector_C[vector_C > 5])
print("Mayores que 5:",vector_D)

# Punto 12
vector_E = np.array(vector_C[(vector_C > 5) & (vector_C < 15)])
print("Mayores que 5 y menores que 15", vector_E)

# Punto 13
vector_C[[4, 14]] = 7
print("Vector modificado: ", vector_C)

# Punto 14
moda = np.argmax(np.bincount(vector_C))
print("Moda: ", moda)

# Punto 15
vector_ordenado = np.sort(vector_C)
print("Vector ordenado: ", vector_ordenado)

# Punto 16
multiplicar_10 = vector_C * 10 
print("Multiplicar por 10: ", multiplicar_10)

# Punto 17
vector_C[5:8] = [60, 70, 80]
print("Vector modificado: ", vector_C)

# Punto 18
vector_C[13:16] = [140, 150, 160]
print("Vector modificado: ", vector_C)

