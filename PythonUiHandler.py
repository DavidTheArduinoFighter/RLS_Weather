import sys
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QFile, QIODevice


class ShowApp:
    def __init__(self, ui_file_name):
        self.app = QApplication(sys.argv)
        self.ui_file = QFile(ui_file_name)
        self.ui_file_name = ui_file_name
        self.open()
        self.run()

    def open(self):
        if not self.ui_file.open(QIODevice.ReadOnly):
            print(f"Cannot open {self.ui_file_name}: {self.ui_file.errorString()}")
            sys.exit(-1)

    def run(self):
        loader = QUiLoader()
        window = loader.load(self.ui_file)
        self.ui_file.close()
        if not window:
            print(loader.errorString())
            sys.exit(-1)
        window.show()
        sys.exit(self.app.exec())


if __name__ == "__main__":
    ui = "GUI.ui"
    App = ShowApp(ui)
