import sys
import random

from PySide6 import QtCore, QtGui, QtWidgets

from models.basic_canvas import BasicCanvas
from models.vertices_table import JsonTable

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Pyxelator')
        self.file_choice = 'resources/tetrahedron_vertices.json'
        
        self.grid_layout = QtWidgets.QGridLayout()
        
        self._setup_left_side()
        self.grid_layout.setColumnMinimumWidth(1, 25)
        self._setup_right_side()
        
        self.setLayout(self.grid_layout)
        self.show()

    def _setup_left_side(self):
        self.canvas_label = QtWidgets.QLabel('Display', self)
        self.grid_layout.addWidget(self.canvas_label, 0, 0)
        
        self.isometric_canvas = BasicCanvas()
        self.grid_layout.addWidget(self.isometric_canvas, 1, 0)
        
    def _setup_right_side(self):
        self.table = JsonTable()
        self.grid_layout.addWidget(self.table, 1, 2)
        
        self.button_layout = QtWidgets.QHBoxLayout()
        
        self.load_table_button = QtWidgets.QPushButton('Load')
        self.load_table_button.clicked.connect(lambda: self.table.load_json(self.file_choice))
        self.button_layout.addWidget(self.load_table_button)
        
        self.button_layout.addSpacerItem(QtWidgets.QSpacerItem(200, 25))
                
        self.save_table_button = QtWidgets.QPushButton('Save')
        self.save_table_button.clicked.connect(lambda: self.table.save_json(self.file_choice))
        self.button_layout.addWidget(self.save_table_button)
        
        self.grid_layout.addLayout(self.button_layout, 0, 2)