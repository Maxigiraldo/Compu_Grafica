import numpy as np

data = np.array([1, 2, np.nan, 4, 5, np.nan, 7, 8, 9])

data_sin_nan = np.nan_to_num(data, nan=0)

media = np.mean(data_sin_nan)

print("Array original con NaN:\n", data)
print("\nArray después de reemplazar NaN por 0:\n", data_sin_nan)
print("\nMedia del array resultante:", media)