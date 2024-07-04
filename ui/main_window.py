import numpy as np
from PySide6 import QtCore, QtGui, QtWidgets

from models.top_viewport import TopViewport
from models.bottom_viewport import BottomViewport
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
        self.top_viewport = TopViewport()
        self.grid_layout.addWidget(self.top_viewport, 0, 0)
        
        self.bottom_viewport = BottomViewport()
        self.grid_layout.addWidget(self.bottom_viewport, 2, 0)     
                                               
    def _setup_right_side(self):
        self.vertices_table = VerticesTable()
        self.vertices_panel = InteractiveTablePanel(self.vertices_table)
        self.grid_layout.addWidget(self.vertices_panel, 0, 2, 1, 2)

        self.info_panel = QtWidgets.QPlainTextEdit('render info')
        self.info_panel.setEnabled(False)
        self.grid_layout.addWidget(self.info_panel, 0, 4)
        
        get_colors_button = QtWidgets.QPushButton('Render Top Viewport')
        get_colors_button.clicked.connect(self.draw_figure)
        self.grid_layout.addWidget(get_colors_button, 0, 4, QtCore.Qt.AlignmentFlag.AlignBottom)
        
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
        pass
        
    def draw_figure(self):
        vertices, faces = self.vertices_table.get_plot_data()
        self.top_viewport.draw_figure(vertices, faces)