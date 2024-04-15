import numpy as np
import pandas as pd

domain = np.zeros((10, 10, 10))  # Crea un dominio 3D de 10x10x10
print(domain)


df = pd.DataFrame({'x': [0, 1], 'y': [0, 1], 'z': [0, 1], 'pressure': [100, 150]})
df.to_csv('output.csv', index=False)