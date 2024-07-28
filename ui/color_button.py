from PIL import Image, ImageQt
from PySide6 import QtCore, QtGui, QtWidgets

class ColorButton(QtWidgets.QPushButton):
    def __init__(self, parent=None, color=(255, 0, 0)):
        super().__init__(parent)
        self.setFixedSize(50, 50)
        self.setStyleSheet('dark')
        self.setIconSize(QtCore.QSize(32, 32))
        self.set_color(color)
    
    def update_icon(self):
        color_box = ImageQt.ImageQt(Image.new('RGB', (32, 32), self.color))
        self.setIcon(QtGui.QPixmap(color_box))
        
    def set_color(self, color):
        self.color = color
        self.setPalette(QtGui.QColor(*color))
        # self.setText(str(color))
        self.update_icon()
        
    def get_color(self):
        return self.color