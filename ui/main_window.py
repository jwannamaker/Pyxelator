import sys
import random

from PySide6 import QtCore, QtGui, QtWidgets

from models.basic_canvas import BasicCanvas
from models.vertices_table import JsonTable

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Pyxelator')
        
        # MenuBar
        self.menu = QtWidgets.QMenuBar()
        self.file_menu = self.menu.addMenu('File')
        
        self.exit_action = QtGui.QAction('Exit', self)
        self.exit_action.setShortcut(QtGui.QKeySequence.Quit)
        self.exit_action.triggered.connect(self.close)
        
        self.file_menu.addSeparator()
        self.file_menu.addAction(self.exit_action)
        self.menu.show()
        
        # GUI
        self.isometric_canvas = BasicCanvas(self)
        
        self.info_group = QtWidgets.QGroupBox(self)
        self.info_layout = QtWidgets.QVBoxLayout(self.info_group)
        self.file_choice = 'resources/tetrahedron_vertices.json'
        
        self.table = JsonTable(self.info_group)
        
        self.load_table_button = QtWidgets.QPushButton('Load')
        self.load_table_button.clicked.connect(lambda: self.table.load_json(self.file_choice))
        
        self.save_table_button = QtWidgets.QPushButton('Save')
        self.save_table_button.clicked.connect(lambda: self.table.save_json(self.file_choice))
        
        self.info_layout.addWidget(self.load_table_button)
        self.info_layout.addWidget(self.save_table_button)
        self.info_layout.addWidget(self.table)
        
        self.hlayout = QtWidgets.QHBoxLayout(self)
        self.hlayout.addWidget(self.isometric_canvas)
        self.hlayout.addLayout(self.info_layout)
        
