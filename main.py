import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox
from GUI import Ui_MainWindow

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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
