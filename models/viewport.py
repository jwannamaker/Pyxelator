from PySide6 import Qt3DCore, QtCore, QtWidgets, QtGui


class Viewport(QtWidgets.QWidget):
    def __init__(self, obj_file):
        self.load_obj(obj_file)
        
    @QtCore.Slot(str)
    def load_obj(self, obj_file):
        pass