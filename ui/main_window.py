from PySide6 import QtCore, QtGui, QtWidgets

from models.basic_canvas import BasicCanvas
from models.vertices_table import JsonTable
from models.palette_table import PaletteTable

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Pyxelator')
        self.setMinimumSize(900, 520)
        
        self.file_choice = 'resources/tetrahedron_vertices.json'
        self.palette_choice = 'resources/mushroom-32x.png'
        self.palette_json = 'resources/mushroom_palette.json'
        
        self.grid_layout = QtWidgets.QGridLayout()
        
        self.grid_layout.setColumnMinimumWidth(0, 480)
        self.grid_layout.setColumnStretch(0, 400)
        self.grid_layout.setColumnMinimumWidth(1, 20)
        self.grid_layout.setColumnStretch(1, 0)
        self.grid_layout.setColumnMinimumWidth(2, 320)
        self.grid_layout.setColumnStretch(2, 0)
        
        
        self.grid_layout.setRowMinimumHeight(0, 20)
        self.grid_layout.setRowStretch(0, 0)
        self.grid_layout.setRowMinimumHeight(1, 220)
        self.grid_layout.setRowStretch(1, 400)
        self.grid_layout.setRowMinimumHeight(2, 20)
        self.grid_layout.setRowStretch(2, 0)
        self.grid_layout.setRowMinimumHeight(3, 20)
        self.grid_layout.setRowStretch(3, 0)
        self.grid_layout.setRowMinimumHeight(4, 240)
        self.grid_layout.setRowStretch(4, 0)
        
        self._setup_left_side()
        self._setup_right_side()
        
        self.setLayout(self.grid_layout)
        self.show()

    def _setup_left_side(self):
        self.canvas_label = QtWidgets.QLabel('Display', self)
        self.grid_layout.addWidget(self.canvas_label, 0, 0)
        
        self.isometric_canvas = BasicCanvas()
        self.grid_layout.addWidget(self.isometric_canvas, 1, 0, 5, 1)
    
    def _setup_right_side(self):
        self.configure_label = QtWidgets.QLabel('Configure', self)
        self.grid_layout.addWidget(self.configure_label, 0, 2)
        
        self.table = JsonTable()
        self.grid_layout.addWidget(self.table, 1, 2)
        
        self.table_button_layout = QtWidgets.QHBoxLayout()
        
        self.load_table_button = QtWidgets.QPushButton('Load')
        self.load_table_button.clicked.connect(lambda: self.table.load_json(self.file_choice))
        self.table_button_layout.addWidget(self.load_table_button)
        
        self.table_button_layout.addSpacerItem(QtWidgets.QSpacerItem(200, 25))
        
        self.save_table_button = QtWidgets.QPushButton('Save')
        self.save_table_button.clicked.connect(lambda: self.table.save_json(self.file_choice))
        self.table_button_layout.addWidget(self.save_table_button)
        
        self.grid_layout.addLayout(self.table_button_layout, 2, 2)
        
        
        self.palette_choices_layout = QtWidgets.QHBoxLayout()
        
        self.dark_table = PaletteTable()
        self.palette_choices_layout.addWidget(self.dark_table)
        
        self.mid_table = PaletteTable()
        self.palette_choices_layout.addWidget(self.mid_table)
        
        self.light_table = PaletteTable()
        self.palette_choices_layout.addWidget(self.light_table)
        
        self.grid_layout.addLayout(self.palette_choices_layout, 4, 2)
        
        self.palette_button_layout = QtWidgets.QHBoxLayout()
        
        self.load_palette_button = QtWidgets.QPushButton('Load')
        self.load_palette_button.clicked.connect(lambda: self.dark_table.load_palette(self.palette_choice))
        self.palette_button_layout.addWidget(self.load_palette_button)
        
        self.palette_button_layout.addSpacerItem(QtWidgets.QSpacerItem(200, 25))
        
        self.save_palette_button = QtWidgets.QPushButton('Save')
        self.save_palette_button.clicked.connect(lambda: self.dark_table.save_palette(self.palette_json))
        self.palette_button_layout.addWidget(self.save_palette_button)
        
        self.grid_layout.addLayout(self.palette_button_layout, 5, 2)
        