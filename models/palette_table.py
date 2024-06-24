import json

import numpy as np
from PIL import Image, ImageQt, ImageColor, PaletteFile
from PySide6 import QtCore, QtGui, QtWidgets

class PaletteTable(QtWidgets.QTableWidget):
    def __init__(self):
        super().__init__()
        self.palette_data = {}
    
    @QtCore.Slot(str)
    def load_palette(self, palette_png):
        with Image.open(palette_png) as f:
            f.convert('RGB')
            palette = f.getpalette()
            palette = np.reshape(palette, (-1, 3))
            self.palette_data = {k: v for k, v in enumerate(palette)}
            
        if not self.palette_data:
            return
        
        self.setRowCount(len(self.palette_data))
        self.setColumnCount(4)
        
        self.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.setHorizontalHeaderLabels(['', 'R', 'G', 'B'])
        self.verticalHeader().setVisible(False)
        self.setSelectionBehavior(QtWidgets.QTableWidget.SelectionBehavior.SelectRows)
        
        # populate the table
        for index, value in self.palette_data.items():
            color_box = ImageQt.ImageQt(Image.new('RGB', (100, 100), tuple(value)))
            color_box = QtWidgets.QTableWidgetItem(QtGui.QPixmap(color_box), '')
            self.setItem(index, 0, color_box)
            self.setItem(index, 1, QtWidgets.QTableWidgetItem(str(value[0])))
            self.setItem(index, 2, QtWidgets.QTableWidgetItem(str(value[1])))
            self.setItem(index, 3, QtWidgets.QTableWidgetItem(str(value[2])))
        
        for i in self.items(QtCore.QMimeData()):
            i.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            
    @QtCore.Slot(str)
    def save_palette(self, palette_json):
        with open(palette_json, 'w') as f:
            json.dump(self.palette_data, f)
        