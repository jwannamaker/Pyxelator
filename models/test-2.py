import sys
import numpy as np
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel
from PySide6.QtGui import QImage, QPixmap
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PIL import Image, ImageDraw
from PIL.ImageQt import ImageQt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("3D Model Viewer and Pixelator")

        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
        self.setCentralWidget(central_widget)

        # Top part for 3D model rendering using Matplotlib
        self.fig = Figure()
        self.canvas = FigureCanvas(self.fig)
        layout.addWidget(self.canvas)
        self.ax = self.fig.add_subplot(111, projection='3d')

        # Bottom part for pixelated image using PIL
        self.pixel_label = QLabel()
        layout.addWidget(self.pixel_label)

        self.vertices = np.array([[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]])
        self.faces = [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]
        self.palette = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]

        self.render_3d_model()
        self.render_pixelated_image()

    def render_3d_model(self):
        self.ax.clear()
        for face in self.faces:
            face_vertices = self.vertices[list(face)]
            self.ax.add_collection3d(
                Poly3DCollection([face_vertices], color=np.random.rand(3,), alpha=0.5)
            )
        self.ax.auto_scale_xyz([-1, 1], [-1, 1], [-1, 1])
        self.canvas.draw()

    def render_pixelated_image(self):
        projected_vertices = self.project_vertices(self.vertices)
        image = self.rasterize_faces(projected_vertices, self.faces, self.palette, (200, 200))

        qim = ImageQt(image)
        pixmap = QPixmap.fromImage(QImage(qim))
        self.pixel_label.setPixmap(pixmap)

    def project_vertices(self, vertices):
        projected = []
        for vert in vertices:
            x, y, z = vert
            # Simple orthographic projection
            projected.append((x, y))
        return projected

    def rasterize_faces(self, vertices, faces, palette, image_size):
        img = Image.new('RGB', image_size, (255, 255, 255))
        draw = ImageDraw.Draw(img)
        
        for i, face in enumerate(faces):
            projected_face = [vertices[v] for v in face]
            color = palette[i % len(palette)]
            draw.polygon(projected_face, fill=color)
        
        return img

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
