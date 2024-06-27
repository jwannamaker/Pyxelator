import numpy as np
from PySide6 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT
# from matplotlib.backends.qt_compat import QtWidgets
from matplotlib.figure import Figure
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

class Viewport(QtWidgets.QWidget):
    def __init__(self, vertices, faces, colors):
        super().__init__()
        layout = QtWidgets.QVBoxLayout()
        
        canvas = FigureCanvasQTAgg(Figure(figsize=(1, 1)))
        layout.addWidget(canvas)
        layout.addWidget(NavigationToolbar2QT(canvas, self))
        
        

        ax = canvas.figure.subplots()
        ax.set(xlim=(-1.5,1.5), ylim=(-1.5,1.5), zlim=(-1.5,1.5))
        ax.add_collection3d(Poly3DCollection(vertices, color=colors))

        self.setLayout(layout)
        