import numpy as np
from PySide6 import QtCore, QtGui, QtWidgets

from models.top_viewport import TopViewport
from models.bottom_viewport import BottomViewport
from models.vertices_table import VerticesTable
from models.palette_table import PaletteTable
from models.table_panel import TablePanel

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Pyxelator')
        self.setMinimumSize(600, 600)
        self.setFocus(QtCore.Qt.FocusReason.NoFocusReason)
        self.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        
        self.grid_layout = QtWidgets.QGridLayout()
        
        self.grid_layout.setColumnMinimumWidth(0, 200)
        self.grid_layout.setColumnMinimumWidth(1, 5)
        self.grid_layout.setColumnStretch(1, 0)
        self.grid_layout.setColumnMinimumWidth(2, 400)
        
        self.grid_layout.setRowMinimumHeight(0, 5)
        # self.grid_layout.setRowStretch(0, 0)
        self.grid_layout.setRowMinimumHeight(1, 200)
        self.grid_layout.setRowMinimumHeight(2, 5)
        # self.grid_layout.setRowStretch(2, 0)
        self.grid_layout.setRowMinimumHeight(3, 200)
        
        self._setup_left_side()
        self._setup_right_side()
        
        self.setLayout(self.grid_layout)
        self.show()

    def _setup_left_side(self):
        self.top_viewport = TopViewport()
        self.grid_layout.addWidget(self.top_viewport, 1, 0)
        
        self.bottom_viewport = BottomViewport()
        self.grid_layout.addWidget(self.bottom_viewport, 3, 0)
                                               
    def _setup_right_side(self):
        # self.grid_layout.addWidget(QtWidgets.QLabel('Model Configuration'), 0, 0, 1, 3,
        #                            QtCore.Qt.AlignmentFlag.AlignCenter | QtCore.Qt.AlignmentFlag.AlignTop)
        self.vertices_table = VerticesTable()
        self.model_config_panel = TablePanel(['.obj'])
        self.model_config_panel.open_button.released.connect(self.open_model)
        self.model_config_panel.render_button.released.connect(self.render_top)
        self.grid_layout.addWidget(self.model_config_panel, 1, 2)
        
        # self.grid_layout.addWidget(QtWidgets.QLabel('Pixel Art Configuration'), 2, 0, 1, 3,
        #                            QtCore.Qt.AlignmentFlag.AlignCenter | QtCore.Qt.AlignmentFlag.AlignTop)
        self.palette_table = PaletteTable()
        self.color_config_panel = TablePanel(['.png'])
        self.color_config_panel.open_button.released.connect(self.open_palette)
        self.color_config_panel.render_button.released.connect(self.render_bottom)
        self.grid_layout.addWidget(self.color_config_panel, 3, 2)
        
    def open_model(self):
        self.vertices_table.open_file_dialog(self.model_config_panel.get_current_choice())
        self.model_config_panel.setup_tables([self.vertices_table])

    def open_palette(self):
        self.palette_table.open_file_dialog(self.color_config_panel.get_current_choice())
        self.color_config_panel.setup_tables([self.palette_table])
        self.palette_table.set_num_selectable(self.vertices_table.faces_count)

    def render_top(self):
        self.top_viewport.draw_figure(self.vertices_table.get_vertices(), 
                                      self.vertices_table.get_faced_vertices())
        
    def render_bottom(self):
        self.bottom_viewport.render(self.vertices_table.get_faced_vertices(), 
                                    self.palette_table.get_colors(),
                                    *self.top_viewport.get_camera_angles())