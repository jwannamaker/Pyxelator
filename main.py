from PyQt6.QtWidgets import QApplication, QMainWindow

from ui.main_window import MainWindow

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    app.exec()
