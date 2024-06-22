from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtOpenGLWidgets import QOpenGLWidget
from OpenGL import GL

class BasicCanvas(QOpenGLWidget):
    def initializeGL(self):
        # clear color is black
        GL.glClearColor(0.0, 0.0, 0.0, 1.0)

    def paintGL(self):
        # clear the screen
        GL.glClear(GL.GL_COLOR_BUFFER_BIT)
        
    def resizeGL(self, width, height):
        pass
    
    def sizeHint(self):
        return QtCore.QSize(400, 400)