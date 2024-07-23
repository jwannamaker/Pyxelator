from PIL import Image, ImageQt
from PySide6 import QtCore, QtGui, QtWidgets

from ui.json_table_widget import JsonTableWidget


class FacesTable(JsonTableWidget):
    face_changed = QtCore.Signal(list)
    face_double_clicked = QtCore.Signal(int)
    
    def __init__(self, faces):
        super().__init__(1, ['Faces'])
        self.verticalHeader().setVisible(True)
        self.currentItemChanged.connect(self.on_current_index_changed)
        self.itemDoubleClicked.connect(self.on_face_double_clicked)
        
        self.faces = faces
        self.populate_table()

    def populate_table(self):
        self.setRowCount(len(self.faces))

        for i, v in enumerate(self.faces):
            default_color_box = ImageQt.ImageQt(Image.new('RGB', (100, 100), (96, 96, 96)))
            default_color_box = QtGui.QPixmap(default_color_box)
            text = '[ '
            for value in v:
                text += f'{value + 1:2d} '
            text += ']'
            self.setItem(i, 0, QtWidgets.QTableWidgetItem(default_color_box, text))
            self.item(i, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            self.setRowHeight(i, 50)
            
    def reset(self, faces):
        super()._reset()
        self.faces = faces
        self.populate_table()

    @QtCore.Slot(QtGui.QPixmap)
    def update_icon(self, color_box):
        self.currentItem().setIcon(color_box)

    def on_current_index_changed(self):
        self.face_changed.emit(self.faces[self.currentItem().row()])
        
    def on_face_double_clicked(self):
        self.face_double_clicked.emit(self.currentItem().row())