import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox
from GUI import Ui_MainWindow
import PythonUiHandler as UI


class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)
        self.show()


class MainApp:
    def __init__(self, gui_ui):
        app = QApplication(sys.argv)
        window = UI.ShowApp(gui_ui)
        # window.show_temp("32")
        # window.show_wind("40")
        # window.show_humidity("78")
        app.exec()


if __name__ == '__main__':
    run = MainApp("GUI.ui")

