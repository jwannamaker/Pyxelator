import json
import string

import numpy as np
from PySide6 import QtCore, QtWidgets, QtGui

from ui.json_table_widget import JsonTableWidget


class VerticesTable(JsonTableWidget):
    def __init__(self):
        super().__init__(1, ['Vertices'])
        self.setSelectionMode(QtWidgets.QTableWidget.SelectionMode.MultiSelection)
        self.verticalHeader().setVisible(True)
        # self.verticalScrollBar().setEnabled(True)
        self.faces = {}
    
    def _reset(self):
        super()._reset()
        self.data = {}
    
    def populate_table(self):
        self.setRowCount(len(self.data))
        
        for i, v in enumerate(list(self.data.values())):
            self.setItem(i, 0, QtWidgets.QTableWidgetItem(f'( {v[0]:+.2f} {v[1]:+.2f} {v[2]:+.2f} )'))
            self.item(i, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

    def get_vertices(self):
        return list(self.data.values())

    def get_faces(self):
        return list(self.faces.values())

    def get_faced_vertices(self):
        # X = [self.data[k][0] for k in self.data]
        # Y = [self.data[k][1] for k in self.data]
        # Z = [self.data[k][2] for k in self.data]
        return [[self.data[v] for v in face] for face in self.faces.values()]

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
        with open(obj_file, 'r') as f:
            for line in f.readlines():
                if line[0] == 'v':
                    vertices = line.split()
                    vertices.remove('v')
                    self.data[len(self.data)] = [float(x) for x in vertices]
                
                if line[0] == 'f':
                    face = line.split()
                    face.remove('f')
                    self.faces[len(self.faces)] = [int(x)-1 for x in face]
        
        self.populate_table()
        self.file_changed.emit(obj_file)
    
    @QtCore.Slot(list)
    def show_selected_face(self, row_indices):
        self.clearSelection()

        for v in row_indices:
            self.selectRow(v)
            
        