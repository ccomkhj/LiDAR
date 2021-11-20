# examples/Python/Basic/mesh.py

import copy
import numpy as np
import open3d as o3d
from shapely.geometry import Polygon

def PolyArea(triangle):
    x = triangle[0]
    y = triangle[1]
    z = triangle[2]
    pgon = Polygon(zip(x, y, z))
    return pgon.area

if __name__ == "__main__":

    print("Testing mesh in open3d ...")
    mesh = o3d.io.read_triangle_mesh("data\plant_on_cup_textual.ply")
    print(mesh)
    print(np.asarray(mesh.vertices))
    print(np.asarray(mesh.triangles))
    print("")

    print("Try to render a mesh with normals (exist: " +
          str(mesh.has_vertex_normals()) + ") and colors (exist: " +
          str(mesh.has_vertex_colors()) + ")")
    o3d.visualization.draw_geometries([mesh])
    print("A mesh with no normals and no colors does not seem good.")

    print("Computing normal and rendering it.")
    mesh.compute_vertex_normals()
    print(np.asarray(mesh.triangle_normals))
    o3d.visualization.draw_geometries([mesh])


    '''  Generate triangles with its spatial coord.   '''
    triangles_indexs = np.asarray(mesh.triangles)
    vertices = np.asarray(mesh.vertices)
    triangles = list()
    for index in triangles_indexs:
        triangles.append(vertices[index])

    area = 0    
    for triangle in triangles:
        area += PolyArea(triangle)

    print(f"Total Area of Polygon: {area}")

    print("Painting the mesh")
    mesh.paint_uniform_color([1, 0.706, 0])
    o3d.visualization.draw_geometries([mesh])