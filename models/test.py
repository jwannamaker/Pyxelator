# # import numpy as np
# # from collections import deque
# # import matplotlib.pyplot as plt
# # from mpl_toolkits.mplot3d import Axes3D, proj3d
# # from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# # def depth(face):
# #     return np.mean([v[2] for v in face])

# # def print_details(list):
# #     print()
# #     for i, face in enumerate(list):
# #         print(f'Face {i}: {face}  Depth: {depth(face)}')

def x_axis_rotation(vertices, angle):
    theta = np.deg2rad(angle)
    rot_x = np.array([[1, 0, 0],
                      [0, np.cos(theta), -np.sin(theta)],
                      [0, np.sin(theta), np.cos(theta)]])
    return [np.matmul(rot_x, v) for v in vertices]

# # def y_axis_rotation(vertices, angle):
# #     theta = np.deg2rad(angle)
# #     rot_y = np.array([[np.cos(theta), 0, -np.sin(theta)],
# #                       [0, 1, 0],
# #                       [np.sin(theta), 0, np.cos(theta)]])
# #     return [np.matmul(rot_y, v) for v in vertices]

# # def z_axis_rotation(vertices, angle):
# #     theta = np.deg2rad(angle)
# #     rot_z = np.array([[np.cos(theta), -np.sin(theta), 0],
# #                       [np.sin(theta), np.cos(theta), 0],
# #                       [0, 0, 1]])
# #     return [np.matmul(rot_z, v) for v in vertices]

# # def pyxelate(ax3d, face_vertices, angles, colors):
# #     # Go through each face, ordering them so the lowest z values are drawn first
# #     draw_faces = deque(maxlen=len(face_vertices))
# #     elev, azim = np.deg2rad(angles[0]), np.deg2rad(angles[1])
    
# #     draw_faces = face_vertices
# #     print_details(draw_faces)
    
# #     draw_faces = sorted(face_vertices, key=depth)
# #     print_details(draw_faces)
    
# #     elev_t = np.array([[1, 0, 0],
# #                        [0, np.cos(elev), -np.sin(elev)],
# #                        [0, np.sin(elev), np.cos(elev)]])
# #     azim_t = np.array([[np.cos(azim), -np.sin(azim), 0],
# #                        [np.sin(azim), np.cos(azim), 0],
# #                        [0, 0, 1]])
# #     rot_t = np.dot(elev_t, azim_t)
    
# #     projected_faces = np.dot(face_vertices, rot_t.T)
    
# #     x, y, z = projected_faces.T
# #     x2d, y2d = proj3d.proj_transform(x, y, z, ax3d.get_proj())
    
# #     return np.column_stack((x2d, y2d))
    
# #     # Create and Apply the projection matrix 
# #     # Translate for the new box to be only positive (quadrant I)
# #     # Scale down all coordinates to pixelate the model
# #     # Create and save the image, then set the QPixmap to the saved image

    

# # if __name__ == '__main__':
# #     vertices = [
# #         [0, 0, 0],    # Vertex 0
# #         [1, 0, 0],    # Vertex 1
# #         [1, 1, 0],    # Vertex 2
# #         [0, 1, 0],    # Vertex 3
# #         [0, 0, 1],    # Vertex 4
# #         [1, 0, 1],    # Vertex 5
# #         [1, 1, 1],    # Vertex 6
# #         [0, 1, 1],    # Vertex 7
# #     ]
    
# #     faces = [
# #         [0, 1, 2, 3],  # Bottom face
# #         [4, 5, 6, 7],  # Top face
# #         [0, 1, 5, 4],  # Front face
# #         [2, 3, 7, 6],  # Back face
# #         [0, 3, 7, 4],  # Left face
# #         [1, 2, 6, 5],  # Right face
# #     ]
    
# #     # projection = np.array([
# #     #     [ 6.72755075e-01, -6.74770971e-01,  0.00000000e+00, -1.11022302e-16]
# #     #     [-6.01682947e-01, -5.99885404e-01,  4.31312401e-01,  6.66133815e-16]
# #     #     [ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00, -1.00000000e+01]
# #     #     [ 3.05439837e-01,  3.04527327e-01,  8.49638080e-01,  1.00000000e+01]
# #     # ])
    
# #     colors = [
# #         (1, 0, 0),   # Bottom face RED
# #         (0, 1, 0),   # Top face GREEN
# #         (0, 0, 1),   # Front face BLUE
# #         (1, 1, 0), # Back face RED+GREEN
# #         (0, 1, 1), # Left face GREEN+BLUE
# #         (1, 0, 1), # Right face RED+BLUE
# #     ]
    
# #     face_vertices = [[vertices[i] for i in face] for face in faces]
    
# #     fig = plt.figure('211')
# #     ax = fig.add_subplot('111', projection='3d')

# #     # Plot the vertices
# #     ax.add_collection3d(Poly3DCollection(face_vertices, color=colors))
    
# #     vertices_2d = pyxelate(ax,
# #                            face_vertices, 
# #                            (np.float64(-136.11428571428587), np.float64(66.5142857142857)), 
# #                            colors)

# #     fig2d, ax2d = plt.subplots()
# #     ax2d.scatter(vertices_2d[:, 0], vertices_2d[:, 1])

# #     plt.show()
    
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D, proj3d
# import numpy as np

# # Step 1: Define the polyhedron vertices (example: a cube)
# vertices = np.array([
#     [1, 1, 1],
#     [1, 1, -1],
#     [1, -1, 1],
#     [1, -1, -1],
#     [-1, 1, 1],
#     [-1, 1, -1],
#     [-1, -1, 1],
#     [-1, -1, -1]
# ])

# # Step 3: Create a 3D plot and retrieve the viewing angles
# fig = plt.figure(figsize=(10, 5))
# ax = fig.add_subplot(121, projection='3d')

# # Plot the vertices
# ax.scatter(vertices[:, 0], vertices[:, 1], vertices[:, 2])

# # Retrieve the current viewing angles
# def get_current_angles():
#     return ax.azim, ax.elev

# # Step 4: Project 3D vertices to 2D
# def project_3d_to_2d(vertices, angles):
#     # Convert angles to radians
#     elev_rad = np.deg2rad(angles[0])
#     azim_rad = np.deg2rad(angles[1])
    
#     # Rotation matrices for elevation and azimuth
#     R_elev = np.array([
#         [1, 0, 0],
#         [0, np.cos(elev_rad), -np.sin(elev_rad)],
#         [0, np.sin(elev_rad), np.cos(elev_rad)]
#     ])
    
#     R_azim = np.array([
#         [np.cos(azim_rad), -np.sin(azim_rad), 0],
#         [np.sin(azim_rad), np.cos(azim_rad), 0],
#         [0, 0, 1]
#     ])
    
#     # Combined rotation matrix
#     R = np.dot(R_azim, R_elev)
    
#     # Apply the rotation to the vertices
#     transformed_vertices = np.dot(vertices, R.T)
    
#     # Project the 3D points to 2D
#     x, y, z = transformed_vertices.T
#     x2d, y2d, _ = proj3d.proj_transform(x, y, z, ax.get_proj())
    
#     return np.column_stack((x2d, y2d))

# # Get the 2D projected points
# vertices_2d = project_3d_to_2d(vertices, get_current_angles())

# # Step 5: Plot the 2D projection
# fig2d, ax2d = plt.subplots()
# ax2d.scatter(vertices_2d[:, 0], vertices_2d[:, 1])

# # Display the plot
# plt.show()

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D, proj3d
import numpy as np

# Define the polyhedron vertices (example: a cube)
vertices = np.array([
    [1, 1, 1],
    [1, 1, -1],
    [1, -1, 1],
    [1, -1, -1],
    [-1, 1, 1],
    [-1, 1, -1],
    [-1, -1, 1],
    [-1, -1, -1]
])

# Function to project 3D vertices to 2D
def project_3d_to_2d(vertices, ax3d):
    # Retrieve the current viewing angles
    azim = ax3d.azim
    elev = ax3d.elev

    # Convert angles to radians
    elev_rad = np.deg2rad(elev)
    azim_rad = np.deg2rad(azim)
    
    # Rotation matrices for elevation and azimuth
    R_elev = np.array([
        [1, 0, 0],
        [0, np.cos(elev_rad), -np.sin(elev_rad)],
        [0, np.sin(elev_rad), np.cos(elev_rad)]
    ])
    
    R_azim = np.array([
        [np.cos(azim_rad), -np.sin(azim_rad), 0],
        [np.sin(azim_rad), np.cos(azim_rad), 0],
        [0, 0, 1]
    ])
    
    # Combined rotation matrix
    R = np.dot(R_azim, R_elev)
    
    # Apply the rotation to the vertices
    transformed_vertices = np.dot(vertices, R.T)
    
    # Project the 3D points to 2D
    x, y, z = transformed_vertices.T
    x2d, y2d, _ = proj3d.proj_transform(x, y, z, ax3d.get_proj())
    
    # return np.column_stack((x2d, y2d))
    return transformed_vertices

# Function to update the 2D plot
def update_projection(event):
    vertices_2d = project_3d_to_2d(vertices, ax3d)
    ax2d.cla()
    ax2d.scatter(vertices_2d[:, 0], vertices_2d[:, 1])
    ax2d.set_title('2D Projection')
    ax2d.set_aspect('equal')
    fig.canvas.draw_idle()

# Create a figure with two subplots
fig = plt.figure(figsize=(10, 5))

# Create the 3D subplot
ax3d = fig.add_subplot(121, projection='3d')
ax3d.scatter(vertices[:, 0], vertices[:, 1], vertices[:, 2])
ax3d.set_title('3D Plot')

# Create the 2D subplot
ax2d = fig.add_subplot(122)
vertices_2d = project_3d_to_2d(vertices, ax3d)
ax2d.scatter(vertices_2d[:, 0], vertices_2d[:, 1])
ax2d.set_title('2D Projection')
ax2d.set_aspect('equal')

# Connect the update function to the 3D plot's events
fig.canvas.mpl_connect('motion_notify_event', update_projection)
fig.canvas.mpl_connect('button_release_event', update_projection)

# Display the plots
plt.show()
