import meshpy.tet as tet

# Definir puntos y caras del tetraedro
points = [(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1)]
facets = [(0, 1, 2), (0, 1, 3), (1, 2, 3), (0, 2, 3)]

# Configurar la malla
mesh_info = tet.MeshInfo()
mesh_info.set_points(points)
mesh_info.set_facets(facets)
mesh = tet.build(mesh_info)

# Comentario: Se definen puntos y caras para un tetraedro simple. Luego, se utiliza meshpy para crear una malla.
