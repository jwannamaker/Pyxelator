import numpy as np
from PySide6 import QtWidgets
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import axes3d
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

class TopViewport(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        layout = QtWidgets.QVBoxLayout()
        
        self.figure = Figure()
        self.canvas = FigureCanvasQTAgg(self.figure)
        # self.figure.canvas.mpl_connect("button_release_event", self.on_click)
        layout.addWidget(NavigationToolbar2QT(self.canvas))
        layout.addWidget(self.canvas)

        self.ax = self.canvas.figure.add_subplot(projection='3d')
        self.ax.set(xlim=(-1.0, 1.0), ylim=(-1.0, 1.0), zlim=(-1.0, 1.0))

        self.ax.set_aspect('equal')
        self.canvas.figure.tight_layout()
        self.setLayout(layout)

    def draw_figure(self, vertices, faces, colors):
        self.ax.clear()

        # use the faces to create the vertices list
        faced_vertices = [[vertices[i-1] for i in face] for face in faces]
        colors = [colors[0], colors[0], colors[1], colors[2]]    # 4 faces

        # self.ax.set_axis_off()
        # self.ax.set_visible(False)
        self.ax.set(xlim=(-1.0, 1.0), ylim=(-1.0, 1.0), zlim=(-1.0, 1.0))
        self.shape_collection = self.ax.add_collection3d(Poly3DCollection(faced_vertices, color=colors))
        
        self.ax.set_aspect('equal')
        self.canvas.figure.tight_layout()
        self.figure.set_canvas(self.canvas)
        self.canvas.draw()

    def get_plot_data(self):
        return Poly3DCollection(self.ax.collections) 