import numpy as np
from PySide6 import QtCore, QtGui, QtWidgets

from ui.top_viewport import TopViewport
from ui.bottom_viewport import BottomViewport
from ui.vertices_table import VerticesTable
from ui.projection_info import ProjectionInfo
from ui.faces_table import FacesTable
from ui.palette_table import PaletteTable
from ui.table_panel import TablePanel


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Pyxelator')
        self.setMinimumSize(800, 800)
        self.setFocus(QtCore.Qt.FocusReason.NoFocusReason)
        self.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        
        self.setFont(QtGui.QFont(['Courier', 'Monospace']))
        # self.setStyle()
        
        self.grid_layout = QtWidgets.QGridLayout()
        self.grid_layout.setSpacing(12)
        
        self.grid_layout.setColumnMinimumWidth(0, 200)
        self.grid_layout.setColumnMinimumWidth(1, 5)
        self.grid_layout.setColumnStretch(1, 0)
        self.grid_layout.setColumnMinimumWidth(2, 400)
        
        self.grid_layout.setRowMinimumHeight(0, 300)
        self.grid_layout.setRowMinimumHeight(1, 5)
        self.grid_layout.setRowStretch(1, 0)
        self.grid_layout.setRowMinimumHeight(2, 300)
        
        self._setup_left_side()
        self._setup_right_side()
        
        self.setLayout(self.grid_layout)
        self.show()

    def _setup_left_side(self):
        self.top_viewport = TopViewport()
        self.grid_layout.addWidget(self.top_viewport, 0, 0)
        
        self.bottom_viewport = BottomViewport()
        self.top_viewport.projection_changed.connect(self.bottom_viewport.update_projection)
        self.grid_layout.addWidget(self.bottom_viewport, 2, 0)
        
    def _setup_right_side(self):
        # self.grid_layout.addWidget(QtWidgets.QLabel('Model Configuration'), 0, 0, 1, 3,
        #                            QtCore.Qt.AlignmentFlag.AlignCenter | QtCore.Qt.AlignmentFlag.AlignTop)
        self.vertices_table = VerticesTable()
        
        self.projection_info = ProjectionInfo()
        self.top_viewport.projection_changed.connect(self.projection_info.update_projection)
        self.top_viewport.angle_changed.connect(self.projection_info.update_angles)
        
        self.model_config_panel = TablePanel(['.obj'])
        self.model_config_panel.setup_tables([self.vertices_table])
        self.model_config_panel.file_choice.currentIndexChanged.connect(self.open_model)
        self.model_config_panel.render_button.released.connect(self.render_top)
        
        self.grid_layout.addWidget(self.model_config_panel, 0, 2, 3, 1)
        
        # self.grid_layout.addWidget(QtWidgets.QLabel('Pixel Art Configuration'), 2, 0, 1, 3,
        #                            QtCore.Qt.AlignmentFlag.AlignCenter | QtCore.Qt.AlignmentFlag.AlignTop)
        self.faces_table = FacesTable(self.vertices_table.get_faces())
        self.faces_table.face_changed.connect(self.vertices_table.show_selected_face)
        self.faces_table.color_chosen.connect(self.vertices_table.set_highlight_color)
        self.faces_table.face_double_clicked.connect(self.top_viewport.isolate_face)
        
        self.palette_table = PaletteTable()
        self.palette_table.color_clicked.connect(self.faces_table.update_icon)
        self.palette_table.color_clicked.connect(self.vertices_table.set_highlight_color)
        
        self.color_config_panel = TablePanel(['.png'])
        self.color_config_panel.setup_tables([self.faces_table, self.palette_table])
        self.color_config_panel.file_choice.currentIndexChanged.connect(self.open_palette)
        self.color_config_panel.render_button.released.connect(self.render_bottom)
        
        self.grid_layout.addWidget(self.color_config_panel, 0, 3, 3, 1)
    
    def open_model(self):
        self.vertices_table.reset()
        self.vertices_table.open_file_dialog(self.model_config_panel.get_current_choice())
        
        self.faces_table.clearSelection()
        self.faces_table.reset(self.vertices_table.get_faces())
        
        self.model_config_panel.setup_tables([self.vertices_table])

    def open_palette(self):
        self.palette_table.open_file_dialog(self.color_config_panel.get_current_choice())
        self.color_config_panel.setup_tables([self.faces_table, self.palette_table])

    def render_top(self):
        self.top_viewport.draw_figure(self.vertices_table.get_vertices(), 
                                      self.vertices_table.get_faces())
        
    def render_bottom(self):
        pass