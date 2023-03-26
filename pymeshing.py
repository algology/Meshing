import matplotlib.pyplot as plt
from pymesh import load_mesh
import os

# Load the CAD file and convert it to a mesh
cad_file = 'example.stl'
mesh = pymesh.load_mesh(cad_file)

# Preprocess the mesh
mesh, _ = pymesh.remove_duplicate_vertices(mesh)
mesh, _ = pymesh.remove_degenerated_faces(mesh)
mesh, _ = pymesh.fill_holes(mesh)
mesh, _ = pymesh.compute_outer_hull(mesh)

# Create a mesh object
vertices = mesh.vertices
faces = mesh.faces
boundary_faces = mesh.boundary_faces
mesh_obj = {'vertices': vertices, 'faces': faces, 'boundary_faces': boundary_faces}

# Plot the mesh
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_trisurf(vertices[:, 0], vertices[:, 1], vertices[:, 2], triangles=faces, linewidth=0.2, edgecolor='black')
plt.show()

