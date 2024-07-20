import json
import string

import numpy as np
from PySide6 import QtCore, QtGui, QtWidgets

from ui.json_table_widget import JsonTableWidget


class VerticesTable(JsonTableWidget):
    def __init__(self):
        super().__init__(3, ['X', 'Y', 'Z'])
        self.faces = {}
    
    def _reset(self):
        self.data = {}
        self.faces = {}
        
        for i in range(self.rowCount()):
            self.removeRow(i)
    
    def populate_table(self):
        self.setRowCount(len(self.data))
        
        for row_index, entry in enumerate(list(self.data.values())):
            for col_index, value in enumerate(entry):
                value = round(value, 3)
                self.setItem(row_index, col_index, QtWidgets.QTableWidgetItem(str(value)))
                self.item(row_index, col_index).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

    def get_vertices(self):
        return list(self.data.values())

    def get_faced_vertices(self):
        # X = [self.data[k][0] for k in self.data]
        # Y = [self.data[k][1] for k in self.data]
        # Z = [self.data[k][2] for k in self.data]
        return [[self.data[v - 1] for v in face] for face in self.faces.values()]

    @QtCore.Slot()
    def open_file_dialog(self, file_choice=None):
        self._reset()
        
        """ Open file_choice if there is one, else bring up dialog. """
        if file_choice and str(file_choice).endswith('.obj'):
            self.load_obj(file_choice)
            return
        if file_choice and str(file_choice).endswith('.json'):
            self.load_json(file_choice)
            return
        
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open', 'resources')
        if filename and filename.endswith('.obj'):
            self.load_obj(filename)
            return
        if filename and filename.endswith('.json'):
            self.load_json(filename)
            return
    
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
        
        self.populate_table()
        self.file_changed.emit(obj_file)