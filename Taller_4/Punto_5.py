import numpy as np

def array_pares():
    array = np.arange(1, 11)

    pares = array[array % 2 == 0]

    print(pares)
