import numpy as np

data = np.array([10, 20, 30, 40, 50])

np.save('mi_array.npy', data)

data_cargado = np.load('mi_array.npy')

print("Array original:\n", data)
print("\nArray cargado desde el archivo:\n", data_cargado)