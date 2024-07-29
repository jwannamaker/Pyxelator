from PIL import Image, ImageQt
from PySide6 import QtCore, QtGui, QtWidgets

class ColorButton(QtWidgets.QPushButton):
    def __init__(self, parent=None, color=(255, 0, 0)):
        super().__init__(parent)
        # self.layout().setSpacing(5)
        # self.setFixedSize(100, 50)
        self.setLayout(QtWidgets.QHBoxLayout())
        self.layout().setSpacing(5)
        # self.setIconSize(QtCore.QSize(32, 32))
        self.set_color(color)
    
    # def update_icon(self):
        # self.setIcon(QtGui.QPixmap(color_box))
        
    def set_color(self, color):
        self.color = color
        color_box = ImageQt.ImageQt(Image.new('RGB', (32, 32), self.color))
        color_box_label = QtWidgets.QLabel()
        color_box_label.setPixmap(QtGui.QPixmap(color_box))
        self.layout().addWidget(color_box_label, 
                                QtCore.Qt.AlignmentFlag.AlignLeft)
        self.layout().addWidget(QtWidgets.QLabel(str(color)),
                                QtCore.Qt.AlignmentFlag.AlignRight)
        # self.update_icon()
        
    def get_color(self):
        return self.color