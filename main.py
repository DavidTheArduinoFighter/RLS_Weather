import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox
from GUI import Ui_MainWindow
import PythonUiHandler as UI

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    return name


def check_sum(num1, num2):
    return num1 + num2


class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)
        self.show()


class MainApp:
    def __init__(self):
        gui_ui = "GUI.ui"
        UI.ShowApp(gui_ui)


if __name__ == '__main__':
    run = MainApp()
    # app = QApplication(sys.argv)
    # w = Window()
    # w.show()
    # sys.exit(app.exec_())
