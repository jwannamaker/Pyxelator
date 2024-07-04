import numpy as np
from PySide6 import QtWidgets
import matplotlib as mpl
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
        layout.addWidget(self.canvas)

        self.ax: axes3d.Axes3D = self.canvas.figure.add_subplot(projection='3d')
        self.ax.set_box_aspect((1, 1, 1), zoom=1)
        self.ax.set_axis_off()
        self.canvas.figure.tight_layout(rect=(0, 0, 1, 1))
        self.setLayout(layout)
    
    def draw_figure(self, vertices, faces):
        self.ax.clear()

        # List of vertices for each face: 
        #
        # face 0:
        #   [v_0[x, y, z], v_1[x, y, z], ...], 
        # face 1:
        #   [v_0[x, y, z], v_1[x, y, z], ...], 
        # ...
        # face N:
        #   [v_0[x, y, z], v_1[x, y, z], ...], 
        faced_vertices = [[vertices[i-1] for i in face] for face in faces]
        colors = [(0, 0, 0, 0.25) for _ in range(len(faces))]
        self.shape_collection = self.ax.add_collection3d(Poly3DCollection(faced_vertices, color=colors))
        
        x = [v[0] for v in vertices]
        y = [v[1] for v in vertices]
        z = [v[2] for v in vertices]
        self.ax.set(xlim=(min(x), max(x)),
                    ylim=(min(y), max(y)),
                    zlim=(min(z), max(z)))
        
        self.ax.set_box_aspect((1, 1, 1), zoom=1)
        self.ax.set_axis_off()
        self.canvas.figure.tight_layout(rect=(0, 0, 1, 1))
        self.figure.set_canvas(self.canvas)
        self.canvas.draw()

    def get_render_data(self):
        return self.ax.get_proj()