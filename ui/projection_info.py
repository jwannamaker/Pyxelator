import numpy as np
from PySide6 import QtCore, QtGui, QtWidgets


class ProjectionInfo(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.grid_layout = QtWidgets.QGridLayout()
        self.grid_layout.setContentsMargins(10, 10, 10, 10)
        self.grid_layout.setSpacing(0)
        
        self.proj_matrix = np.zeros((4, 4))
        self.angles = {'Elev': 0.0, 'Azim': 0.0, 'Roll': 0.0}
        
        self._setup()
        self.setLayout(self.grid_layout)
        self.display_info()
    
    def _setup(self):
        self.proj_labels = {
            'Tx': QtWidgets.QLineEdit(), 
            'Ty': QtWidgets.QLineEdit(),
            'Tz': QtWidgets.QLineEdit(),
            'Tw': QtWidgets.QLineEdit()}
        
        vbox = QtWidgets.QVBoxLayout()
        vbox.setSpacing(0)
        vbox.addWidget(QtWidgets.QLabel('Projection Matrix'), 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        for label, line in self.proj_labels.items():
            hbox = QtWidgets.QHBoxLayout()
            label_widget = QtWidgets.QLabel(label)
            label_widget.setFixedWidth(50)
            hbox.addWidget(label_widget)
            line.setTextMargins(1, 0, 1, 0)
            line.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
            line.setEnabled(False)
            hbox.addWidget(line)
            vbox.addLayout(hbox)
        self.grid_layout.addLayout(vbox, 0, 0)
        
        self.camera_labels = {
            'Azim': QtWidgets.QLineEdit(),
            'Elev': QtWidgets.QLineEdit(),
            'Roll': QtWidgets.QLineEdit()}
        
        vbox = QtWidgets.QVBoxLayout()
        vbox.setSpacing(0)
        vbox.addWidget(QtWidgets.QLabel('Camera Angles'), 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        for label, line in self.camera_labels.items():
            hbox = QtWidgets.QHBoxLayout()
            label_widget = QtWidgets.QLabel(label)
            label_widget.setFixedWidth(50)
            hbox.addWidget(label_widget)
            line.setTextMargins(1, 0, 1, 0)
            line.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
            line.setEnabled(False)
            hbox.addWidget(line)
            vbox.addLayout(hbox)
        self.grid_layout.addLayout(vbox, 2, 0)
        
    def display_info(self):
        for i, line_edit in enumerate(list(self.proj_labels.values())):
            text = '['
            for j in range(4):
                text += f' {self.proj_matrix[i][j]:>-6.2f}'
            text += ']'
            line_edit.clear()
            line_edit.setText(text)
        
        for label, line_edit in list(self.camera_labels.items()):
            text = f'{self.angles[label]:>-6.2f}'
            line_edit.clear()
            line_edit.setText(text)
        
        self.update()
    
    @QtCore.Slot(np.ndarray)
    def update_projection(self, proj_matrix):
        self.proj_matrix = proj_matrix
        self.display_info()
        
    @QtCore.Slot(float, float, float)
    def update_angles(self, azim, elev, roll):
        self.angles['Azim'] = azim
        self.angles['Elev'] = elev
        self.angles['Roll'] = roll
        self.display_info()