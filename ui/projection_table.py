import numpy as np
from PySide6 import QtCore, QtGui, QtWidgets

from ui.json_table_widget import JsonTableWidget

class ProjectionTable(JsonTableWidget):
    def __init__(self):
        super().__init__(1, ['Projection Matrix'])
        self.setEnabled(False)
    
    def populate_table(self):
        self.setRowCount(4)

        for i in range(4):
            row = '| '
            for j in range(4):
                row += f'{self.proj_matrix[i][j]:+.2f} '
            row += '|'
            self.setItem(i, 0, QtWidgets.QTableWidgetItem(row))
            self.item(i, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        
    @QtCore.Slot(np.ndarray)
    def update_projection(self, proj_matrix):
        super()._reset()
        self.proj_matrix = proj_matrix
        self.populate_table()