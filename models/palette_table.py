import json

import numpy as np
from PIL import Image, ImageQt, ImageColor, PaletteFile
from PySide6 import QtCore, QtGui, QtWidgets

class PaletteTable(QtWidgets.QTableWidget):
    def __init__(self):
        super().__init__()
        self.palette_data = {}
        
        self.setColumnCount(4)
        
        self.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.setHorizontalHeaderLabels(['', 'R', 'G', 'B'])
        self.verticalHeader().setVisible(False)
        self.setSelectionBehavior(QtWidgets.QTableWidget.SelectionBehavior.SelectRows)
    
    @QtCore.Slot(str)
    def load_png(self, palette_png):
        with Image.open(palette_png) as f:
            f.convert('RGB')
            palette = f.getpalette()
            palette = np.array_split(palette, len(palette) // 3)
            palette = [[int(i) for i in x] for x in palette]
            self.palette_data = {int(k): {'R': v[0], 'G': v[1], 'B': v[2]} for k, v in enumerate(palette)}
            
        if not self.palette_data:
            return
        self.populate_table()
        
    @QtCore.Slot(str)
    def load_json(self, palette_json):
        with open(palette_json) as f:
            self.palette_data = json.load(f)
        
        if not self.palette_data:
            return
        self.populate_table()
                
    def populate_table(self):
        self.setRowCount(len(self.palette_data))
        
        # populate the table
        for row, color in enumerate(self.palette_data.values()):
            color_box = ImageQt.ImageQt(Image.new('RGB', (100, 100), tuple(color.values())))
            color_box = QtWidgets.QTableWidgetItem(QtGui.QPixmap(color_box), '')
            
            self.setItem(row, 0, color_box)
            self.setItem(row, 1, QtWidgets.QTableWidgetItem(str(color['R'])))
            self.setItem(row, 2, QtWidgets.QTableWidgetItem(str(color['G'])))
            self.setItem(row, 3, QtWidgets.QTableWidgetItem(str(color['B'])))
        
        for i in self.items(QtCore.QMimeData()):
            i.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            
    @QtCore.Slot(str)
    def save_json(self, palette_json):
        with open(palette_json, 'w') as f:
            json.dump(self.palette_data, f)