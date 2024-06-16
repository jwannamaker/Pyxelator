from PyQt6.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QFileDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Pyxelator')
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QGridLayout(central_widget)

        # Add viewports (placeholders for now)
        for i in range(2):
            for j in range(3):
                viewport = QWidget()
                layout.addWidget(viewport, i, j)

        self.show()
        
if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    app.exec()
