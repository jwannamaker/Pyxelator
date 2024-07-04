import json
import string

import numpy as np
from PySide6 import QtCore, QtGui, QtWidgets

from models.json_table_widget import JsonTableWidget

class VerticesTable(JsonTableWidget):
    def __init__(self):
        super().__init__(3, ['X', 'Y', 'Z'])
        self.faces = {}
    
    def populate_table(self):
        self.setRowCount(len(self.data))
        
        # populate the table
        for row_index, entry in enumerate(list(self.data.values())):
            for col_index, value in enumerate(entry):
                value = round(value, 3)
                self.setItem(row_index, col_index, QtWidgets.QTableWidgetItem(str(value)))
                self.item(row_index, col_index).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

    def get_plot_data(self):
        # X = [self.data[k][0] for k in self.data]
        # Y = [self.data[k][1] for k in self.data]
        # Z = [self.data[k][2] for k in self.data]
        return [self.data[k] for k in self.data], [self.faces[k] for k in self.faces]

    @QtCore.Slot()
    def open_file_dialog(self):
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open', 'resources')
        if filename:
            if filename.endswith('.obj'):
                self.load_obj(filename)
            if filename.endswith('.json'):
                self.load_json(filename)
            self.populate_table()
    
    @QtCore.Slot()
    def save_file_dialog(self):
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(self, 'Save', 'resources', ('Text file (*.json)'))
        if filename:
            self.save_json(filename)

    @QtCore.Slot(str)
    def load_obj(self, obj_file):
        self.vertices_count = 0
        self.faces_count = 0

        with open(obj_file, 'r') as f:
            for line in f.readlines():
                if line[0] == 'v':
                    vertices = line.split()
                    vertices.remove('v')
                    self.data[self.vertices_count] = [float(x) for x in vertices]
                    self.vertices_count += 1
                
                if line[0] == 'f':
                    face = line.split()
                    face.remove('f')
                    self.faces[self.faces_count] = [int(x) for x in face]
                    self.faces_count += 1
        
        self.file_changed.emit(obj_file)