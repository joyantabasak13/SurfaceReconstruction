import os
import open3d as o3d

if __name__ == '__main__':
    data_path = os.path.abspath("../data/bunny_normalized.ply")
    cloud = o3d.io.read_point_cloud(data_path) # Read the point cloud
    o3d.visualization.draw_geometries([cloud]) # Visualize the point cloud
