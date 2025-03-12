import numpy as np

M = np.array([[1, 2, 3, 4, 5, 6]])

M_reshape = M.reshape(3, 2)

producto_punto = np.dot(M_reshape, M_reshape.T)

print("Matriz original M:\n", M)
print("\nMatriz M reshaped (3x2):\n", M_reshape)
print("\nProducto punto de M y su transpuesta:\n", producto_punto)