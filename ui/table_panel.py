import json
from pathlib import Path, PurePosixPath

import numpy as np
from PySide6 import QtCore, QtGui, QtWidgets

from ui.json_table_widget import JsonTableWidget

class TablePanel(QtWidgets.QWidget):
    def __init__(self, file_types=['.json']):
        """ file_type: suffix of the files that show up in the file choice combobox. """
        super().__init__()
        self._setup(file_types)

    def _setup(self, file_types):
        self.panel_layout = QtWidgets.QGridLayout()
        self.panel_layout.setContentsMargins(0, 0, 0, 0)
        self.panel_layout.setSpacing(5)
        self.panel_layout.setRowMinimumHeight(0, 5)
        self.panel_layout.setRowStretch(0, 5)

        toolbar = QtWidgets.QHBoxLayout()
        
        self.file_choice = QtWidgets.QComboBox()
        self.file_choice.setPlaceholderText('-')
        self.file_choices = {i.name: i 
                             for i in Path.joinpath(Path.cwd(), 'resources').iterdir() 
                             if i.is_file() and i.suffix in file_types}
        self.file_choice.addItems(self.file_choices)
        toolbar.addWidget(self.file_choice, QtCore.Qt.AlignmentFlag.AlignTop)
        
        self.open_button = QtWidgets.QPushButton('Open')
        self.open_button.setFixedWidth(80)
        toolbar.addWidget(self.open_button, QtCore.Qt.AlignmentFlag.AlignTop)
        
        self.render_button = QtWidgets.QPushButton('Render')
        self.render_button.setFixedWidth(80)
        toolbar.addWidget(self.render_button, QtCore.Qt.AlignmentFlag.AlignTop)
        
        self.panel_layout.addLayout(toolbar, 0, 0)
        self.setLayout(self.panel_layout)

    def setup_tables(self, tables: list[JsonTableWidget]):
        for i, table in enumerate(tables):
            self.panel_layout.addWidget(table, 1, i)
    
    def get_current_choice(self):
        return self.file_choices[self.file_choice.currentText()]