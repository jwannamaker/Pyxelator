from PySide6 import QtCore, QtWidgets, QtGui

from ui.color_button import ColorButton


class PaletteWidget(QtWidgets.QGroupBox):
    button_pressed = QtCore.Signal(tuple)
    
    def __init__(self, colors):
        super().__init__()
        self.setTitle('Palette')
        
        scroll = QtWidgets.QScrollArea()
        scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        
        frame = QtWidgets.QFrame()
        grid_layout = QtWidgets.QGridLayout()
        grid_layout.setSpacing(0)
        
        for i, color in enumerate(colors):
            color_button = ColorButton(color=color)
            color_button.pressed.connect(lambda color: PaletteWidget.on_button_pressed(color))
            grid_layout.addWidget(color_button, i+1, 0)
            grid_layout.addWidget(QtWidgets.QLabel(str(color)), i+1, 1)
            # grid_layout.setRowMinimumHeight(i+1, 50)
        frame.setLayout(grid_layout)
        
        scroll.setWidget(frame)
        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(scroll)
        self.setLayout(vbox)        
        
    def on_button_pressed(color):
        print(str(color))
        # self.grid_layout.removeWidget(button)
        PaletteWidget.button_pressed.emit(color)