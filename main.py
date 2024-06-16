from PyQt6.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Pyxelator')
        
        self.show()
        
if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    app.exec()
