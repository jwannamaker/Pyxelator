import json
from pathlib import Path, PurePosixPath

import numpy as np
from PySide6 import QtCore, QtGui, QtWidgets

from models.json_table_widget import JsonTableWidget

class InteractiveTablePanel(QtWidgets.QWidget):
    def __init__(self, table: JsonTableWidget):
        super().__init__()
        self.file_label = QtWidgets.QLabel()
        self.table = table
        self._setup()

    def _setup(self):
        panel_layout = QtWidgets.QGridLayout()
        panel_layout.setRowMinimumHeight(0, 20)
        panel_layout.setRowStretch(0, 0)

        self.file_label.setText('Select File')
        panel_layout.addWidget(self.file_label, 0, 0)
        
        open_button = QtWidgets.QPushButton('Open')
        open_button.clicked.connect(self.table.open_file_dialog)
        self.table.file_changed.connect(self.update_label)
        panel_layout.addWidget(open_button, 0, 2)

        panel_layout.addWidget(self.table, 1, 0, 1, 3)
        
        self.setLayout(panel_layout)

    @QtCore.Slot(str)
    def update_label(self, filename):
        self.file_label.setText(PurePosixPath(filename).name)