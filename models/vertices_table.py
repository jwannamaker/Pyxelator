import json

from PySide6 import QtCore, QtGui, QtWidgets

class JsonTable(QtWidgets.QTableWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.data = {}
        
    def load_json(self, json_file):
        with open(json_file, 'r') as f:
            self.data = json.load(f)
        
        if not self.data:
            return
        
        self.setRowCount(len(self.data))
        self.setColumnCount(len(self.data[list(self.data.keys())[0]]))
        
        self.setHorizontalHeaderLabels(['x', 'y', 'z'])
        self.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.setSelectionBehavior(QtWidgets.QTableWidget.SelectionBehavior.SelectRows)
        
        # populate the table
        for row_index, entry in enumerate(list(self.data.values())):
            for col_index, value in enumerate(entry):
                value = round(value, 3)
                self.setItem(row_index, col_index, QtWidgets.QTableWidgetItem(str(value)))
                self.item(row_index, col_index).setTextAlignment(QtCore.Qt.AlignCenter)
                