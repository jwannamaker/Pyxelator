"""
Disclaimer: The following file was provided by Chat-GPT 4o
"""

import numpy as np

def write_obj(filename, vertices, faces):
    with open(filename, 'w') as file:
        for v in vertices:
            file.write(f"v {v[0]} {v[1]} {v[2]}\n")
        for f in faces:
            file.write(f"f {' '.join(str(i + 1) for i in f)}\n")

def create_dodecahedron():
    phi = (1 + np.sqrt(5)) / 2  # golden ratio
    vertices = np.array([
        [-1, -1, -1],      [-1, -1, 1],      [-1, 1, -1],      [-1, 1, 1],
        [1, -1, -1],       [1, -1, 1],       [1, 1, -1],       [1, 1, 1],
        [0, -1/phi, -phi], [0, -1/phi, phi], [0, 1/phi, -phi], [0, 1/phi, phi],
        [-1/phi, -phi, 0], [-1/phi, phi, 0], [1/phi, -phi, 0], [1/phi, phi, 0],
        [-phi, 0, -1/phi], [-phi, 0, 1/phi], [phi, 0, -1/phi], [phi, 0, 1/phi]
    ])
    faces = np.array([
        [0, 8, 10, 2, 16],  [0, 16, 18, 4, 12], [0, 12, 14, 1, 8],  [1, 9, 11, 3, 17],
        [1, 17, 19, 5, 9],  [2, 10, 11, 3, 13], [2, 13, 15, 6, 16], [3, 11, 9, 5, 19],
        [4, 18, 16, 6, 14], [4, 14, 12, 8, 0],  [5, 19, 17, 1, 14], [6, 15, 13, 2, 16],
        [7, 15, 13, 3, 11], [7, 13, 10, 2, 12], [7, 11, 19, 5, 17], [7, 17, 9, 1, 8]
    ])

    return vertices, faces

def create_cube():
    vertices = np.array([
        [-1, -1, -1], [-1, -1, 1], [-1, 1, -1], [-1, 1, 1],
        [1, -1, -1],  [1, -1, 1],  [1, 1, -1],  [1, 1, 1]
    ])
    faces = np.array([
        [0, 1, 3, 2], [4, 5, 7, 6], [0, 1, 5, 4],
        [2, 3, 7, 6], [0, 2, 6, 4], [1, 3, 7, 5]
    ])
    return vertices, faces

def create_icosahedron():
    phi = (1 + np.sqrt(5)) / 2  # golden ratio
    vertices = np.array([
        [-1, phi, 0], [1, phi, 0], [-1, -phi, 0], [1, -phi, 0],
        [0, -1, phi], [0, 1, phi], [0, -1, -phi], [0, 1, -phi],
        [phi, 0, -1], [phi, 0, 1], [-phi, 0, -1], [-phi, 0, 1]
    ])
    faces = np.array([
        [0, 11, 5], [0, 5, 1],  [0, 1, 7],   [0, 7, 10], [0, 10, 11],
        [1, 5, 9],  [5, 11, 4], [11, 10, 2], [10, 7, 6], [7, 1, 8],
        [3, 9, 4],  [3, 4, 2],  [3, 2, 6],   [3, 6, 8],  [3, 8, 9],
        [4, 9, 5],  [2, 4, 11], [6, 2, 10],  [8, 6, 7],  [9, 8, 1]
    ])
    return vertices, faces

def create_tetrahedron():
    vertices = np.array([
        [1, 1, 1], [-1, -1, 1], [-1, 1, -1], [1, -1, -1]
    ])
    faces = np.array([
        [0, 1, 2], [0, 2, 3], [0, 3, 1], [1, 3, 2]
    ])
    return vertices, faces

def create_pentagonal_bipyramid():
    phi = (1 + np.sqrt(5)) / 2  # golden ratio
    vertices = np.array([
        [0, 0, phi], [0, 0, -phi], 
        [1, 0, 0],   [-1, 0, 0], 
        [0, 1, 0],   [0, -1, 0]
    ])
    faces = np.array([
        [0, 2, 4], [0, 4, 3], [0, 3, 5], [0, 5, 2], [2, 4, 1],
        [4, 3, 1], [3, 5, 1], [5, 2, 1]
    ])
    return vertices, faces

def create_hexagonal_bipyramid():
    vertices = np.array([
        [0, 0, 1],               [0, 0, -1], 
        [1, 0, 0],               [-1, 0, 0], 
        [0.5, np.sqrt(3)/2, 0],  [-0.5, np.sqrt(3)/2, 0],
        [0.5, -np.sqrt(3)/2, 0], [-0.5, -np.sqrt(3)/2, 0]
    ])
    faces = np.array([
        [0, 2, 4], [0, 4, 3], [0, 3, 6], [0, 6, 2], [0, 2, 5], [0, 5, 7],
        [1, 4, 2], [1, 3, 4], [1, 6, 3], [1, 2, 6], [1, 5, 2], [1, 7, 5]
    ])
    return vertices, faces

def create_elongated_pentagonal_bipyramid():
    phi = (1 + np.sqrt(5)) / 2  # golden ratio
    vertices = np.array([
        [0, 0, phi],    [0, 0, -phi], 
        [1, 0, 0],      [-1, 0, 0], 
        [0, 1, 0],      [0, -1, 0], 
        [0.5, 0.5, 0],  [-0.5, 0.5, 0],
        [0.5, -0.5, 0], [-0.5, -0.5, 0]
    ])
    faces = np.array([
        [0, 2, 6], [0, 6, 4], [0, 4, 7], [0, 7, 3], [0, 3, 8], [0, 8, 2], 
        [2, 6, 4], [2, 4, 7], [2, 7, 3], [2, 3, 8], [2, 8, 6],
        [1, 2, 6], [1, 6, 4], [1, 4, 7], [1, 7, 3], [1, 3, 8], [1, 8, 2]
    ])
    return vertices, faces

def create_elongated_hexagonal_bipyramid():
    vertices = np.array([
        [0, 0, 1],               [0, 0, -1], 
        [1, 0, 0],               [-1, 0, 0], 
        [0.5, np.sqrt(3)/2, 0],  [-0.5, np.sqrt(3)/2, 0],
        [0.5, -np.sqrt(3)/2, 0], [-0.5, -np.sqrt(3)/2, 0],
        [0, 1.5, 0],             [0, -1.5, 0]
    ])
    faces = np.array([
        [0, 2, 4], [0, 4, 3], [0, 3, 6], [0, 6, 2], [0, 2, 5], [0, 5, 7],
        [1, 4, 2], [1, 3, 4], [1, 6, 3], [1, 2, 6], [1, 5, 2], [1, 7, 5],
        [2, 4, 8], [4, 3, 8], [3, 6, 8], [6, 2, 8], [5, 7, 9], [7, 6, 9],
        [6, 2, 9], [2, 5, 9]
    ])
    return vertices, faces

def create_triangular_frustum():
    vertices = np.array([
        [1, 0, 0],   [-1, 0, 0],   [0, np.sqrt(3), 0], 
        [0.5, 0, 1], [-0.5, 0, 1], [0, np.sqrt(3)/2, 1]
    ])
    faces = [
        [0, 1, 2], [3, 4, 5], [0, 1, 4, 3], [1, 2, 5, 4], [2, 0, 3, 5]
    ]
    return vertices, faces

if __name__ == '__main__':
    write_obj('resources/dodecahedron.obj', *create_dodecahedron())
    write_obj('resources/cube.obj', *create_cube())
    write_obj('resources/icosahedron.obj', *create_icosahedron())
    write_obj('resources/tetrahedron.obj', *create_tetrahedron())
    write_obj('resources/pentagonal_bipyramid.obj', *create_pentagonal_bipyramid())
    write_obj('resources/elongated_pentagonal_bipyramid.obj', *create_elongated_pentagonal_bipyramid())
    write_obj('resources/hexagonal_bipyramid.obj', *create_hexagonal_bipyramid())
    write_obj('resources/elongated_hexagonal_bipyramid.obj', *create_elongated_hexagonal_bipyramid())
    write_obj('resources/triangular_frustum.obj', *create_triangular_frustum())
