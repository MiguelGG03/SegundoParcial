import numpy as np

def tensor_deformacion(desplazamientos):
    # Supongamos que `desplazamientos` es un arreglo numpy con las dimensiones adecuadas
    grad = np.gradient(desplazamientos)
    return grad

# Ejemplo de uso
desplazamientos = np.random.rand(10, 10, 10)
tensor = tensor_deformacion(desplazamientos)
print("Tensor de deformaciones:", tensor)
