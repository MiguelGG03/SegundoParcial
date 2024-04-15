from paraview.simple import *

# Cargar el archivo VTU
archivo_vtu = 'viga.vtu'
datos = XMLUnstructuredGridReader(FileName=archivo_vtu)

# Crear una representación para visualizar los datos
representacion = Show(datos)
ColorBy(representacion, 'AlgunCampoDeDatos')  # Especifica el campo para el coloreado

# Configurar la vista
vista = GetActiveView()
vista.Interaction = 1  # Permite interactuar con la visualización
vista.ResetCamera()    # Ajusta la cámara para ver todos los datos

# Renderizar la vista
Render()
