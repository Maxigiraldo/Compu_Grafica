import numpy as np

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