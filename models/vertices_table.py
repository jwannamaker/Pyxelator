import json
import string

from PySide6 import QtCore, QtGui, QtWidgets

class JsonTable(QtWidgets.QTableWidget):
    def __init__(self):
        super().__init__()
        self.data = {}
        
        self.setColumnCount(3)
        
        self.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.setHorizontalHeaderLabels(['X', 'Y', 'Z'])
        self.verticalHeader().setVisible(False)
        self.setSelectionBehavior(QtWidgets.QTableWidget.SelectionBehavior.SelectRows)
    
    @QtCore.Slot(str)
    def load_json(self, json_file):
        with open(json_file, 'r') as f:
            self.data = json.load(f)
        
        if not self.data:
            return
        self.populate_table()
    
    def populate_table(self):
        self.setRowCount(len(self.data))
        
        # populate the table
        for row_index, entry in enumerate(list(self.data.values())):
            for col_index, value in enumerate(entry):
                value = round(value, 3)
                self.setItem(row_index, col_index, QtWidgets.QTableWidgetItem(str(value)))
                self.item(row_index, col_index).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            
    @QtCore.Slot(str)
    def save_json(self, json_file):
        with open(json_file, 'w') as f:
            json.dump(self.data, f)