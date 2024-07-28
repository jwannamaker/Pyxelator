import numpy as np
from PySide6 import QtWidgets, QtGui, QtCore
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.backend_bases import FigureCanvasBase, MouseEvent
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import axes3d
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

class TopViewport(QtWidgets.QWidget):
    projection_changed = QtCore.Signal(np.ndarray)
    angle_changed = QtCore.Signal(float, float, float)
    
    def __init__(self):
        super().__init__()
        layout = QtWidgets.QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(5)
        
        self.figure = Figure()
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.figure.canvas.mpl_connect('motion_notify_event', self.on_motion_notify_event)
        layout.addWidget(self.canvas)

        self.ax: axes3d.Axes3D = self.canvas.figure.add_subplot(projection='3d')
        self.ax.set_proj_type('ortho')
        self.ax.set_box_aspect((1, 1, 1), zoom=1)
        self.ax.set_axis_off()
        self.canvas.figure.tight_layout(rect=(0, 0, 1, 1))
        
        self.setFixedSize(QtCore.QSize(320, 320))
        self.setLayout(layout)
    
    def draw_figure(self, vertices, faces):
        self.ax.clear()
        colors = [(0, 0, 0, 0.25) for _ in range(len(faces))]
        
        self.face_vertices = [[vertices[v] for v in f] for f in faces]
        self.shape_collection = self.ax.add_collection3d(Poly3DCollection(self.face_vertices, color=colors))
        
        xlims = min(vertices, key=lambda v: v[0])[0], max(vertices, key=lambda v: v[0])[0]
        ylims = min(vertices, key=lambda v: v[1])[1], max(vertices, key=lambda v: v[1])[1]
        zlims = min(vertices, key=lambda v: v[2])[2], max(vertices, key=lambda v: v[2])[2]
        self.ax.set(xlim=xlims, ylim=ylims, zlim=zlims)
        
        self.ax.set_proj_type('ortho')
        self.ax.set_box_aspect((1, 1, 1), zoom=1)
        self.ax.set_axis_off()
        self.canvas.figure.tight_layout(rect=(0, 0, 1, 1))
        self.figure.set_canvas(self.canvas)
        self.canvas.draw()

    @QtCore.Slot(int)
    def isolate_face(self, face):
        self.shape_collection.set_facecolor((0, 0, 0, 0.05))
        
        # Adding the isolated face to the axis
        self.ax.add_collection3d(Poly3DCollection([self.face_vertices[face]], color=(0.6, 0, 0.3, 0.3)))
        self.canvas.draw()
        
    def on_motion_notify_event(self, event: MouseEvent):
        self.projection_changed.emit(self.ax.get_proj())
        self.angle_changed.emit(*self.get_camera_angles())
        
    def get_camera_angles(self):
        return self.ax.azim, self.ax.elev, self.ax.roll
