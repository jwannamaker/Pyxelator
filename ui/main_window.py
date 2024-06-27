from PySide6 import QtCore, QtGui, QtWidgets

from models.basic_canvas import BasicCanvas
from models.vertices_table import VerticesTable
from models.palette_table import PaletteTable
from models.interactive_table import InteractiveTablePanel

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Pyxelator')
        self.setMinimumSize(900, 520)
        
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
        self.vertices_table = VerticesTable()
        self.vertices_panel = InteractiveTablePanel(self.vertices_table)
        self.grid_layout.addWidget(self.vertices_panel, 0, 2, 1, 2)
        
        get_colors_button = QtWidgets.QPushButton('Get Colors')
        get_colors_button.clicked.connect(self.get_colors)
        get_colors_button.clicked.connect(self.get_plot_data)
        self.grid_layout.addWidget(get_colors_button, 0, 4)
        
        self.dark_palette_table = PaletteTable()
        self.dark_palette_panel = InteractiveTablePanel(self.dark_palette_table)
        self.grid_layout.addWidget(self.dark_palette_panel, 2, 2)
        
        self.mid_palette_table = PaletteTable()
        self.mid_palette_panel = InteractiveTablePanel(self.mid_palette_table)
        self.grid_layout.addWidget(self.mid_palette_panel, 2, 3)
        
        self.light_palette_table = PaletteTable()
        self.light_palette_panel = InteractiveTablePanel(self.light_palette_table)
        self.grid_layout.addWidget(self.light_palette_panel, 2, 4)
            
    def get_colors(self):
        dark_color = self.dark_palette_table.get_current_selected()
        mid_color = self.mid_palette_table.get_current_selected()
        light_color = self.light_palette_table.get_current_selected()
        return {'dark': dark_color, 'mid': mid_color, 'light': light_color}
        
    def get_plot_data(self):
        self.vertices_table.get_plot_data()