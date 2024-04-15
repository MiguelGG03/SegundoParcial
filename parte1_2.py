import pandas as pd

# Datos ficticios de presiones y desplazamientos
data = {'x': [0, 1, 2], 'y': [0, 1, 2], 'z': [0, 1, 2], 'pressure': [100, 200, 150], 'displacement': [0.1, 0.2, 0.1]}
df = pd.DataFrame(data)

# Exportar a CSV
df.to_csv('output.csv', index=False)

# Comentario: El dataframe contiene coordenadas y variables físicas como presión y desplazamiento.
# Estos datos se exportan a CSV, formato que puede ser importado en Paraview para visualización.
