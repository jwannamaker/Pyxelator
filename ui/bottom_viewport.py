import numpy as np
from PySide6 import QtCore, QtGui, QtWidgets
from PIL import Image, ImageDraw, ImageQt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import proj3d, axes3d
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, PolyCollection

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

def isometric_projection(azim, elev, x, y, z):
    """ Differently trash. """
    # Convert degrees to radians
    angle_x = np.deg2rad(azim)
    angle_y = np.deg2rad(elev)
    
    # Rotate around the X-axis
    x1 = x
    y1 = y * np.cos(angle_x) - z * np.sin(angle_x)
    z1 = y * np.sin(angle_x) + z * np.cos(angle_x)
    
    # Rotate around the Y-axis
    x2 = x1 * np.cos(angle_y) + z1 * np.sin(angle_y)
    y2 = y1
    
    return x2, y2

def scale(x, y):
    return (x + 1) * 150, (y + 1) * 150

def clearer(r, g, b):
    return r, g, b, 0.5

def lighter(r, g, b):
    return r + 32, g + 24, b + 12, 0.5

class BottomViewport(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        layout = QtWidgets.QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(5)
        
        self.figure = Figure()
        self.canvas = FigureCanvasQTAgg(self.figure)
        layout.addWidget(self.canvas)
        
        self.ax = self.canvas.figure.add_subplot()
        self.ax.set_aspect('equal')
        self.ax.set_axis_off()
        self.canvas.figure.tight_layout(rect=(0, 0, 1, 1))
        
        self.proj_matrix = np.array([])
        
        self.setFixedSize(QtCore.QSize(300, 300))
        self.setLayout(layout)
    
    @QtCore.Slot(np.ndarray)
    def update_projection(self, proj_matrix):
        self.proj_matrix = proj_matrix
    
    def render(self, face_vertices, colors, azim, elev, roll):
        """ Note: PIL draws with (0, 0) in the upper left """
        
        print(f'From BottomViewport \n{self.proj_matrix}')
        
        self.ax.add_collection()
        
        
        projected_faces = []
        
        # out = Image.new('RGBA', (self.width, self.height))
        # drawing_context = ImageDraw.Draw(out)
        
        # # print(f'projected_faces: {projected_faces}')
        # for face, color in zip(projected_faces, colors):
        #     # print(f'face: {face}')
        #     drawing_context.polygon([v for v in face],
        #                             fill=clearer(*color),
        #                             outline=lighter(*color),
        #                             width=5)
        # out = ImageQt.ImageQt(out)
        # out.scaled(QtCore.QSize(300, 300), QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        # self.label.setPixmap(QtGui.QPixmap.fromImage(out))
        
        self.update()
        

