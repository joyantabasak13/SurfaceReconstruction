import os
import open3d as o3d
import numpy as np

if __name__ == '__main__':
    data_path = os.path.abspath("../data/bunny_normalized.ply")
    cloud_ply = o3d.io.read_point_cloud(data_path) # Read the point cloud
    print(cloud_ply)
    print(np.asarray(cloud_ply.points))
    #o3d.visualization.draw_geometries([cloud_ply], point_show_normal=True) # Visualize the point cloud
    mesh_obj = o3d.io.read_triangle_mesh("../data/shapenet_ex_2/model_normalized.obj")
    cloud_obj = o3d.geometry.PointCloud()
    cloud_obj.points = mesh_obj.vertices
    cloud_obj.normals = mesh_obj.vertex_normals
    cloud_obj.normalize_normals()
    o3d.visualization.draw_geometries([cloud_obj])