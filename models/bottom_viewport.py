from collections import deque

import numpy as np
from PIL import Image, ImageDraw, ImageQt
from PySide6 import QtCore, QtGui, QtWidgets


def average_z(face):
    return np.mean([v[2] for v in face])

def project(width, height, point):
    """ 
    width: on-screen pixel width of a tile
    point: 3d coordinate [x, y, z]
    
    returns: 
    """
    a = -1 / 2
    b = -1 / (2 * np.sqrt(2))
    isometric_t = np.array([[1, a, b, 0],
                            [-1, a, b, 0],
                            [0, 1, b, 0]])
    isometric_t = (width / 4) * isometric_t
    point = np.matmul(isometric_t, np.array([*point, 1]))
    
    return round(point[0] + (width / 2)), round((height / 2) - point[1])

class BottomViewport(QtWidgets.QWidget):
    def __init__(self, width=300, height=300):
        super().__init__()
        layout = QtWidgets.QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(5)
        
        self.width = width
        self.height = height
        self.label = QtWidgets.QLabel()
        self.setFixedSize(QtCore.QSize(300, 300))
        layout.addWidget(self.label)
        self.setLayout(layout)
    
    def render(self, face_vertices, colors):
        # Remember: PIL draws with (0, 0) in the upper left
        projected_faces = sorted(face_vertices, key=average_z, reverse=True)
        projected_faces = [[project(self.width, self.height, v) for v in face] for face in projected_faces] 
        # projected_faces = [[(round(v[0], 2), round(v[1], 2)) for v in face] for face in projected_faces]
        
        out = Image.new('RGB', (self.width, self.height))
        drawing_context = ImageDraw.Draw(out)
        
        print(f'projected_faces: {projected_faces}')
        for face, color in zip(projected_faces, colors):
            print(f'face: {face}')
            drawing_context.polygon([v for v in face],
                                    fill=color)
        self.label.setPixmap(QtGui.QPixmap(ImageQt.ImageQt(out)))
        
        self.update()
        self.setVisible(True)
        

