from PySide6 import QtCore, QtWidgets, QtGui

from ui.color_button import ColorButton


class PaletteWidget(QtWidgets.QWidget):
    button_pressed = QtCore.Signal(tuple)
    
    def __init__(self, colors):
        super().__init__()
        self.grid_layout = QtWidgets.QGridLayout()
        for i, color in enumerate(colors):
            color_button = ColorButton(color=color)
            color_button.pressed.connect(lambda state, c=color: self.on_button_pressed(c))
            self.grid_layout.addWidget(ColorButton(color=color), i, 0)
            self.grid_layout.addWidget(QtWidgets.QLabel(str(color)), i, 1)
        self.setLayout(self.grid_layout)
        
    def on_button_pressed(self, color):
        print(str(color))
        # self.grid_layout.removeWidget(button)
        self.button_pressed.emit(color)