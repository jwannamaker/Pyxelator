from PIL import Image, ImageQt
from PySide6 import QtCore, QtGui, QtWidgets

from ui.json_table_widget import JsonTableWidget
from ui.color_button import ColorButton

class FacesTable(JsonTableWidget):
    face_changed = QtCore.Signal(list)
    face_double_clicked = QtCore.Signal(int)
    color_chosen = QtCore.Signal(tuple)
    
    def __init__(self, faces):
        super().__init__(1, ['Face'])
        self.verticalHeader().setVisible(True)
        self.currentItemChanged.connect(self.on_current_index_changed)
        self.itemDoubleClicked.connect(self.on_face_double_clicked)
        
        self.faces = faces
        self.populate_table()

    def populate_table(self):
        self.setRowCount(len(self.faces))

        for i, v in enumerate(self.faces):
            text = '[ '
            for value in v:
                text += f'{value + 1:2d} '
            text += ']'
            self.setItem(i, 0, QtWidgets.QTableWidgetItem(text))
            self.item(i, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignVCenter | QtCore.Qt.AlignmentFlag.AlignRight)
            
    def reset(self, faces):
        super()._reset()
        self.faces = faces
        self.populate_table()

    @QtCore.Slot(tuple)
    def update_icon(self, color):
        color_box = ImageQt.ImageQt(Image.new('RGB', (100, 100), color))
        updated_item = QtWidgets.QTableWidgetItem(self.currentItem())
        updated_item.setIcon(QtGui.QPixmap(color_box))
        self.setItem(self.currentRow(), 0, updated_item)
        self.color_chosen.emit(color)

    def on_current_index_changed(self):
        self.face_changed.emit(self.faces[self.currentRow()])
        
    def on_face_double_clicked(self):
        """ Emits the int for the number, which face it is. """
        self.face_double_clicked.emit(self.currentRow())