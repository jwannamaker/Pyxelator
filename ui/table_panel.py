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
        self.panel_layout.setSpacing(0)

        toolbar = QtWidgets.QHBoxLayout()
        toolbar.setSpacing(0)
        
        self.file_choice = QtWidgets.QComboBox()
        self.file_choice.setPlaceholderText('Select a File')
        self.file_choices = {i.name: i 
                             for i in Path.joinpath(Path.cwd(), 'resources').iterdir() 
                             if i.is_file() and i.suffix in file_types}
        self.file_choice.addItems(self.file_choices)
        toolbar.addWidget(self.file_choice, QtCore.Qt.AlignmentFlag.AlignTop)
        
        self.render_button = QtWidgets.QPushButton('Render')
        self.render_button.setFixedWidth(120)
        toolbar.addWidget(self.render_button, QtCore.Qt.AlignmentFlag.AlignTop)
        
        self.panel_layout.addLayout(toolbar, 0, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.setLayout(self.panel_layout)

    def setup_tables(self, tables: list[QtWidgets.QWidget]):
        table_layout = QtWidgets.QHBoxLayout()
        for table in tables:
            if isinstance(table, QtWidgets.QWidget):
                table_layout.addWidget(table)
            else:
                table_layout.addLayout(table)
        self.panel_layout.addLayout(table_layout, 1, 0, QtCore.Qt.AlignmentFlag.AlignBottom)
    
    def get_current_choice(self):
        return self.file_choices[self.file_choice.currentText()]