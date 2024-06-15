from PyQt6.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QAction, QFileDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Pyxelator')

        # Menu actions
        import_action = QAction('Import Model', self)
        import_action.triggered.connect(self.import_model)

        save_action = QAction('Save Model', self)
        save_action.triggered.connect(self.save_model)

        # Menu bar
        menubar = self.menuBar()
        file_menu = menubar.addMenu('File')
        file_menu.addAction(import_action)
        file_menu.addAction(save_action)

        # Layout for viewports
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QGridLayout(central_widget)

        # Add viewports (placeholders for now)
        for i in range(2):
            for j in range(3):
                viewport = QWidget()
                layout.addWidget(viewport, i, j)

        self.show()

    def import_model(self):
        file_name, _ = QFileDialog.getOpenFileName(self, 'Open Model File', '', 'Model Files (*.obj *.json *.stl)')
        if file_name:
            # Load the model here
            pass

    def save_model(self):
        file_name, _ = QFileDialog.getSaveFileName(self, 'Save Model File', '', 'Model Files (*.json)')
        if file_name:
            # Save the model here
            pass

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    app.exec()
