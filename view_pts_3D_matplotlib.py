import os
import glob
import pymeshlab as ml
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--mode', type=str, default='output', help='For After: output for Before: bunny')
args = parser.parse_args()

# Replace the wildcard with the appropriate folder path containing PTS files
folder_path = "./{}".format(args.mode)
pts_files = glob.glob(os.path.join(folder_path, "*.pts"))

# Create a 3D plot using Matplotlib
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Load and plot the paired PTS and XF files
for pts_file_path in pts_files:
    # Check if the corresponding XF file exists
    xf_file_path = pts_file_path.replace(".pts", ".xf")
    if not os.path.exists(xf_file_path):
        print(f"XF file not found for {pts_file_path}. Skipping...")
        continue

    # Create a MeshLab project
    ms = ml.MeshSet()

    # Load the current PTS file
    ms.load_new_mesh(pts_file_path)

    # Get the vertex coordinates
    vertices = ms.current_mesh().vertex_matrix()

    # Check if the vertices array is empty
    if vertices.size == 0:
        print(f"Failed to load {pts_file_path}. Skipping...")
        continue

    # Read the corresponding XF file
    with open(xf_file_path, 'r') as file:
        lines = file.readlines()
    transformation_matrix = np.array([list(map(float, line.split())) for line in lines])

    # Apply the transformation to the vertices
    homogeneous_coords = np.hstack((vertices, np.ones((vertices.shape[0], 1))))
    transformed_vertices = np.dot(homogeneous_coords, transformation_matrix.T)[:, :3]

    # Plot the transformed point cloud
    ax.scatter(transformed_vertices[:, 0], transformed_vertices[:, 1], transformed_vertices[:, 2], s=1, label=pts_file_path)

# Set plot title and labels
ax.set_title('3D Scatter Plot of Meshes')

ax.set_axis_off()  # Hide the axes

# Show the plot
plt.show()


