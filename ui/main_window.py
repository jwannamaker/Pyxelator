import numpy as np
from PySide6 import QtCore, QtGui, QtWidgets

from models.basic_canvas import BasicCanvas
from models.viewport import Viewport
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
        self.top_viewport = Viewport()
        self.grid_layout.addWidget(self.top_viewport, 0, 0)
        
        self.render_canvas = BasicCanvas()
        self.grid_layout.addWidget(self.render_canvas, 2, 0)     
                                               
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
        dark_color = self.dark_palette_table.get_current_selected()
        mid_color = self.mid_palette_table.get_current_selected()
        light_color = self.light_palette_table.get_current_selected()
        colors = dark_color + mid_color + light_color
        return [i / 255 for i in dark_color], \
               [i / 255 for i in mid_color], \
               [i / 255 for i in light_color]
        
    def draw_figure(self):
        vertices, faces = self.vertices_table.get_plot_data()
        
        colors = self.get_colors()

        self.info_panel.appendPlainText('Vertices')
        self.info_panel.appendPlainText(str(vertices))
        self.info_panel.appendPlainText('Faces')
        self.info_panel.appendPlainText(str(faces))
        self.info_panel.appendPlainText('Colors')
        self.info_panel.appendPlainText(str(colors))
        self.top_viewport.draw_figure(vertices, faces, colors)