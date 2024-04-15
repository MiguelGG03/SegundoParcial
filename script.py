import numpy as np
import pandas as pd

# Crear un arreglo tridimensional de tamaño 5x5x5
# Cada celda contiene el valor de su suma de índices, por ejemplo, (i+j+k)
dimension = 5
array_3d = np.zeros((dimension, dimension, dimension))

# Llenar el arreglo con la suma de sus índices
for i in range(dimension):
    for j in range(dimension):
        for k in range(dimension):
            array_3d[i, j, k] = i + j + k

# Imprimir el arreglo
print("Arreglo tridimensional:")
print(array_3d)
