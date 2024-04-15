import numpy as np
import pandas as pd
import meshpy.tet as tet

# Crear un arreglo tridimensional de tamaño 10x10x10
# Cada celda contiene el valor de su suma de índices, por ejemplo, (i+j+k)
dimension = 10
array_3d = np.zeros((dimension, dimension, dimension))

# Llenar el arreglo con la suma de sus índices
for i in range(dimension):
    for j in range(dimension):
        for k in range(dimension):
            array_3d[i, j, k] = i + j + k

# Imprimir el arreglo
print("Arreglo tridimensional:")
print(array_3d)

"""
Puntos: Los puntos son las coordenadas de las esquinas de un cubo en este ejemplo. Están definidos en un espacio 3D.

Caras: Las caras son listas de índices de puntos que forman cada cara del cubo. En este caso, cada cara está definida por cuatro puntos, formando un cuadrilátero. MeshPy puede utilizar esta información para crear tetraedros dentro del volumen delimitado por estas caras.
"""

# Definir puntos y caras para un cubo
points = [
    (0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0),
    (0, 0, 1), (1, 0, 1), (1, 1, 1), (0, 1, 1)
]

facets = [
    [0, 1, 2, 3],  # cara inferior
    [4, 5, 6, 7],  # cara superior
    [0, 1, 5, 4],  # cara frontal
    [2, 3, 7, 6],  # cara trasera
    [0, 3, 7, 4],  # cara izquierda
    [1, 2, 6, 5]   # cara derecha
]

# Crear la información de la malla y construir la malla
mesh_info = tet.MeshInfo()
mesh_info.set_points(points)
mesh_info.set_facets(facets)
mesh = tet.build(mesh_info)

# Imprimir el resultado de la malla
print("Número de elementos en la malla:", len(mesh.elements))
