import json
from abc import abstractmethod

from PySide6 import QtCore, QtGui, QtWidgets

class JsonTableWidget(QtWidgets.QTableWidget):
    def __init__(self, num_col, col_labels):
        super().__init__()
        self.file = ''
        self.data = {}
        self.setColumnCount(num_col)
        self.setHorizontalHeaderLabels(col_labels)
        self._config_table()

    def _config_table(self):
        self.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.verticalHeader().setVisible(False)
        self.setSelectionBehavior(QtWidgets.QTableWidget.SelectionBehavior.SelectRows)
        self.setSelectionMode(QtWidgets.QTableWidget.SelectionMode.SingleSelection)
        self.setEditTriggers(QtWidgets.QTableWidget.EditTrigger.NoEditTriggers)
        self.setShowGrid(False)

    def get_current_selected(self):
        return tuple(self.data[self.currentRow()])
    
    @abstractmethod
    def populate_table(self):
        pass

    def convert_keys(self, x):
        if isinstance(x, dict):
            return {int(k): v for k, v in x.items()}
        return x

    def load_json(self, json_file):
        with open(json_file) as f:
            self.data = json.load(f, object_hook=self.convert_keys)
        
        if not self.data:
            return
        
    def save_json(self, json_file):
        with open(json_file, 'w') as f:
            json.dump(self.data, f)
            
    @abstractmethod
    @QtCore.Slot()
    def open_file_dialog(self):
        pass

    @abstractmethod
    @QtCore.Slot()
    def save_file_dialog(self):
        pass
