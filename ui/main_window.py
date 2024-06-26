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
        self.palette_choice = {'dark': ['resources/mushroom-32x.png', 'resources/mushroom_palette.json'],
                               'mid': ['resources/mushroom-32x.png', 'resources/mushroom_palette.json'],
                               'light': ['resources/mushroom-32x.png', 'resources/mushroom_palette.json']}
        
        self.grid_layout = QtWidgets.QGridLayout()
        
        self.grid_layout.setColumnMinimumWidth(0, 480)
        # self.grid_layout.setColumnStretch(0, 400)
        self.grid_layout.setColumnMinimumWidth(1, 10)
        self.grid_layout.setColumnStretch(1, 0)
        self.grid_layout.setColumnMinimumWidth(2, 140)
        self.grid_layout.setColumnMinimumWidth(3, 140)
        self.grid_layout.setColumnMinimumWidth(4, 140)
        # self.grid_layout.setColumnStretch(2, 0)
        
        
        self.grid_layout.setRowMinimumHeight(0, 240)
        # self.grid_layout.setRowStretch(0, 0)
        self.grid_layout.setRowMinimumHeight(1, 10)
        self.grid_layout.setRowStretch(1, 0)
        self.grid_layout.setRowMinimumHeight(2, 240)
        # self.grid_layout.setRowStretch(2, 0)
        
        self._setup_left_side()
        self._setup_right_side()
        
        self.setLayout(self.grid_layout)
        self.show()

    def _setup_left_side(self):
        self.isometric_canvas = BasicCanvas()
        self.grid_layout.addWidget(self.isometric_canvas, 0, 0)
        
        self.render_canvas = BasicCanvas()
        self.grid_layout.addWidget(self.render_canvas, 2, 0)     
                                               
    def _setup_right_side(self):
        self.vertices_table = JsonTable()
        self._place_table(self.vertices_table, 0, 2, 1, 2)
        
        self.dark_palette_table = PaletteTable()
        self._place_table(self.dark_palette_table, 2, 2)
        
        self.mid_palette_table = PaletteTable()
        self._place_table(self.mid_palette_table, 2, 3)
        
        self.light_palette_table = PaletteTable()
        self._place_table(self.light_palette_table, 2, 4)
        
    def _place_table(self, table, grid_x, grid_y, row_span=1, column_span=1):
        table_layout = QtWidgets.QGridLayout()
        table_layout.setRowMinimumHeight(0, 20)
        
        open_button = QtWidgets.QPushButton('Open')
        open_button.clicked.connect(lambda: self._open_file_dialog(table))
        table_layout.addWidget(open_button, 0, 0, 1, 2)
        
        save_button = QtWidgets.QPushButton('Save')
        save_button.clicked.connect(lambda: self._save_file_dialog(table))
        table_layout.addWidget(save_button, 0, 2)
        
        table_layout.addWidget(table, 1, 0, 1, 3)
        self.grid_layout.addLayout(table_layout, grid_x, grid_y, row_span, column_span)
    
    @QtCore.Slot(QtWidgets.QTableWidget)
    def _open_file_dialog(self, table):
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open', 'resources', ('Text files (*.json)'))
        if filename:
            table.load_json(filename)
    
    @QtCore.Slot(QtWidgets.QTableWidget)
    def _save_file_dialog(self, table):
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(self, 'Save', 'resources', ('Text files (*.json)'))
        if filename:
            table.save_json(filename)