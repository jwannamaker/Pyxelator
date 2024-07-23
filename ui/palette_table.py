import json

import numpy as np
from PIL import Image, ImageQt
from PySide6 import QtCore, QtGui, QtWidgets

from ui.json_table_widget import JsonTableWidget

class LimitedSelectionModel(QtCore.QItemSelectionModel):
    """ DISCLAIMER: The following class utilizes Chat-GPT. """
    def __init__(self, model, max_selection, parent=None):
        super().__init__(model, parent)
        self.max_selection = max_selection

    def select(self, selection, flags):
        selected_rows = set(index.row() for index in self.selectedRows())
        new_selected_rows = set(index.row() for index in selection.indexes())
        combined_selection = selected_rows.union(new_selected_rows)
        
        if len(combined_selection) > self.max_selection:
            return  

        super().select(selection, flags)

class PaletteTable(JsonTableWidget):
    def __init__(self):
        super().__init__(1, ['Colors'])
        # self.setMaximumWidth(120)
    
    def set_num_selectable(self, num):
        self.setSelectionMode(QtWidgets.QTableWidget.SelectionMode.MultiSelection)
        self.setSelectionModel(LimitedSelectionModel(self.model(), num))
    
    def get_colors(self):
        return [tuple(self.data[i.row()]) for i in self.selectionModel().selectedRows()]
    
    def populate_table(self):
        self.setRowCount(len(self.data))
        
        for row, color in self.data.items():
            color_box = ImageQt.ImageQt(Image.new('RGB', (100, 100), color))
            text = f'{color[0]:3d} {color[1]:3d} {color[2]:3d}'
            self.setItem(row, 0, QtWidgets.QTableWidgetItem(QtGui.QPixmap(color_box), text))
            self.item(row, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
    
    @QtCore.Slot()
    def open_file_dialog(self, file_choice):
        if file_choice and str(file_choice).endswith('.png'):
            self.load_png(file_choice)
            return
        if file_choice and str(file_choice).endswith('.json'):
            self.load_json(file_choice)
            return
        
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open', 'resources')
        if filename and filename.endswith('.png'):
            self.load_png(filename)
        if filename and filename.endswith('.json'):
            self.load_json(filename)
    
    @QtCore.Slot()
    def save_file_dialog(self):
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(self, 'Save', 'resources', ('Text file (*.json)'))
        if filename:
            self.save_json(filename)
            
    def load_png(self, palette_png):
        with Image.open(palette_png) as f:
            f.convert('RGB')
            palette = f.getpalette()
            palette = np.array_split(palette, len(palette) // 3)
            palette = [tuple([int(i) for i in x]) for x in palette]
            self.data = {k: v for k, v in enumerate(palette)}
            
        if not self.data:
            return
        
        self.file_changed.emit(palette_png)
        self.populate_table()