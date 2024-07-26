import json

import numpy as np
from PIL import Image, ImageQt
from PySide6 import QtCore, QtGui, QtWidgets

from ui.json_table_widget import JsonTableWidget


class PaletteTable(JsonTableWidget):
    color_selected = QtCore.Signal(tuple)
    
    def __init__(self):
        super().__init__(1, ['Palette'])
        
        # self.horizontalHeader().sectionPressed.connect(self.on_color_selected)
        
        self.setDragEnabled(True)
        
    
    def get_normalized_color(self):
        """ Returns a tuple of 3 floats in range [0, 1]. """
        i = self.currentIndex().row()
        return self.data[i][0] / 255, self.data[i][1] / 255, self.data[i][2] / 255
    
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
    
    def on_color_selected(self):
        color = tuple(int(i) for i in self.currentItem().text().split())
        self.color_selected.emit(color)