import numpy as np

array = np.array(range(1, 11))

array_reshape = array.reshape(2, 5)

print("Array reshaped:\n", array_reshape)
print("Forma:", array_reshape.shape)
print("Tamaño:", array_reshape.size)
print("Dimensiones:", array_reshape.ndim)