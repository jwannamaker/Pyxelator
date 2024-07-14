import numpy as np
from PIL import Image, ImageDraw, ImageQt
from PySide6 import QtCore, QtGui, QtWidgets
from mpl_toolkits import mplot3d

def average_z(face):
    return np.mean([v[2] for v in face])

def get_isometric_projection(x:int, y:int, z:int):
    SQRT_2, SQRT_3, SQRT_6 = 2**0.5, 3**0.5, 6**0.5
    x_out = (x-y) / SQRT_2
    y_out = (x+y-2*z) / SQRT_6
    return x_out, y_out

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
    
    return round((width / 2) - point[0]), round((height / 2) - point[1])

def isometric_projection(x, y, z):
    # Convert degrees to radians
    angle_x = np.deg2rad(-30)
    angle_y = np.deg2rad(45)
    
    # Rotate around the X-axis
    x1 = x
    y1 = y * np.cos(angle_x) - z * np.sin(angle_x)
    z1 = y * np.sin(angle_x) + z * np.cos(angle_x)
    
    # Rotate around the Y-axis
    x2 = x1 * np.cos(angle_y) + z1 * np.sin(angle_y)
    y2 = y1
    
    print(f'point: {x, y, z} \tmapped to {x2, y2}' )
    return (x2, y2)

def scale(x, y):
    return (x + 1) * 150, (y + 1) * 150

def clearer(r, g, b):
    return r, g, b, 100

def lighter(r, g, b):
    return r + 32, g + 24, b + 12, 100

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
        # projected_faces = [[project(self.width, self.height, v) for v in face] for face in projected_faces] 
        projected_faces = [[scale(*isometric_projection(*v)) for v in face] for face in projected_faces] 
        # projected_faces = [[scale(*v) for v in face] for face in projected_faces]
        
        out = Image.new('RGBA', (self.width, self.height))
        drawing_context = ImageDraw.Draw(out)
        
        # print(f'projected_faces: {projected_faces}')
        for face, color in zip(projected_faces, colors):
            # print(f'face: {face}')
            drawing_context.polygon([v for v in face],
                                    fill=clearer(*color),
                                    outline=lighter(*color),
                                    width=5)
        out = ImageQt.ImageQt(out)
        out.scaled(QtCore.QSize(300, 300), QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.label.setPixmap(QtGui.QPixmap.fromImage(out))
        
        self.update()
        self.setVisible(True)
        

