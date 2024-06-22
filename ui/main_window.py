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
        
        self.button = QtWidgets.QPushButton('Push it baby!')
        self.table = JsonTable('resources/tetrahedron_vertices.json', self)
        
        self.vlayout = QtWidgets.QVBoxLayout()
        self.vlayout.addWidget(self.table)
        self.vlayout.addWidget(self.button)
        
        self.hlayout = QtWidgets.QHBoxLayout(self)
        self.hlayout.addWidget(self.isometric_canvas)
        self.hlayout.addLayout(self.vlayout)
        
        
    
        
