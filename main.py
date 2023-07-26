import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox
from GUI import Ui_MainWindow
import PythonUiHandler as UI

import Get_Data


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
        self.window = UI.ShowApp(gui_ui)
        # self.window.show_temp("32")
        # self.window.show_wind("40")
        # self.window.show_humidity("78")
        # self.window.show_date("78")
        app.exec()

    def refresh(self, url, date=None):
        data = Get_Data.Data(url)
        temp = data.temperature()
        hum = data.humidity()
        rain = data.rainfall_sum()

        for value in temp:
            # if date is not selected
            if date is None:
                if value[1] is None:
                    pass
                # find first showing temp
                else:
                    self.window.show_temp(f"{value[1]}")
                    break
            # if date is selected
            elif data == value[0]:
                self.window.show_date(date)
                if value[1] is None:
                    self.window.show_temp("No data")
                    break
                else:
                    self.window.show_temp(f"{value[1]}")
                    break


if __name__ == '__main__':
    run = MainApp("GUI.ui")
    test_url = 'http://agromet.mkgp.gov.si/APP2/AgrometContent/xml/62.xml'
    run.refresh(test_url)

