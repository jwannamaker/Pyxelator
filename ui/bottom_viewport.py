import numpy as np
from PySide6 import QtCore, QtGui, QtWidgets
from PIL import Image, ImageDraw, ImageQt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import proj3d, axes3d
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, PolyCollection


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
        
        self.setFixedSize(QtCore.QSize(320, 320))
        self.setLayout(layout)
    
    @QtCore.Slot(np.ndarray)
    def update_projection(self, proj_matrix):
        self.proj_matrix = proj_matrix
    
    def render(self, face_vertices, colors, azim, elev, roll):
        """ Note: PIL draws with (0, 0) in the upper left """
        pass

