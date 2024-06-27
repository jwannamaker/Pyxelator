import json

import numpy as np
from PIL import Image, ImageQt
from PySide6 import QtCore, QtGui, QtWidgets

from models.json_widget import JsonTableWidget

class PaletteTable(JsonTableWidget):
    def __init__(self):
        super().__init__(4, ['', 'R', 'G', 'B'])
                
    def populate_table(self):
        self.setRowCount(len(self.data))
        
        for row, color in self.data.items():
            color_box = ImageQt.ImageQt(Image.new('RGB', (100, 100), tuple(color)))
            color_box = QtWidgets.QTableWidgetItem(QtGui.QPixmap(color_box), '')
            
            self.setItem(row, 0, color_box)
            self.setItem(row, 1, QtWidgets.QTableWidgetItem(str(color[0])))
            self.setItem(row, 2, QtWidgets.QTableWidgetItem(str(color[1])))
            self.setItem(row, 3, QtWidgets.QTableWidgetItem(str(color[2])))
    
    @QtCore.Slot()
    def open_file_dialog(self):
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open', 'resources')
        if filename:
            if filename.endswith('.json'):
                self.load_json(filename)
            if filename.endswith('.png'):
                self.load_png(filename)
            self.populate_table()
        # self.file = filename
    
    @QtCore.Slot()
    def save_file_dialog(self):
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(self, 'Save', 'resources', ('Text file (*.json)'))
        if filename:
            self.save_json(filename)
        # self.file = filename

    def load_png(self, palette_png):
        with Image.open(palette_png) as f:
            f.convert('RGB')
            palette = f.getpalette()
            palette = np.array_split(palette, len(palette) // 3)
            palette = [[int(i) for i in x] for x in palette]
            self.data = {k: v for k, v in enumerate(palette)}
            
        if not self.data:
            return