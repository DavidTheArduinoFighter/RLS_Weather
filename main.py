from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox, QPushButton
# from PyQt5 import QtWidgets
from PyQt5 import QtCore
from GUI import Ui_MainWindow
import PythonUiHandler as UI

import sys

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

        self.window = UI.ShowApp(gui_ui)

        self.thread = {}
        url_test = 'http://agromet.mkgp.gov.si/APP2/sl/Home/Index?id=2&archive=0&graphs=1'
        web_data = Get_Data.Locations(url_test)
        locations = web_data.locations()
        self.locations_data = locations[1]

        self.locations_combobox = self.window.findChild(QComboBox, 'comboBox_select_location')
        self.locations_combobox.addItems(locations[0])

        self.refresh_button = self.window.findChild(QPushButton, 'pushButton_refresh')
        self.refresh_button.pressed.connect(self.start_worker_1)

        self.window.show()
        app.exec()

    def start_worker_1(self):
        self.thread[1] = ThreadClass(parent=None, index=1)
        self.thread[1].start()
        self.thread[1].any_signal.connect(self.refresh)
        # self.refresh_button.setEnabled(False)

    def refresh(self, url):
        # could use for finding old values
        date = None

        url_test = 'http://agromet.mkgp.gov.si/APP2/sl/Home/Index?id=2&archive=0&graphs=1'
        web_data = Get_Data.Locations(url_test)
        locations = web_data.locations()

        location = self.locations_combobox.currentText()

        url = 'http://agromet.mkgp.gov.si' + locations[1][locations[0].index(location)]

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
                    self.window.show_date(f"{value[0]}")
                    break
            # if date is selected
            elif data == value[0]:
                self.window.show_date(date)
                if value[1] is None:
                    self.window.show_temp("No data")
                    self.window.show_date(f"{value[0]}")
                    break
                else:
                    self.window.show_temp(f"{value[1]}")
                    self.window.show_date(f"{value[0]}")
                    break

        for value in hum:
            # if date is not selected
            if date is None:
                if value[1] is None:
                    pass
                # find first showing humidity
                else:
                    self.window.show_humidity(f"{value[1]}")
                    break
            # if date is selected
            elif data == value[0]:
                self.window.show_humidity(date)
                if value[1] is None:
                    self.window.show_humidity("No data")
                    break
                else:
                    self.window.show_humidity(f"{value[1]}")
                    break

        for value in rain:
            # if date is not selected
            if date is None:
                if value[1] is None:
                    pass
                # find first showing rainfall sum
                else:
                    self.window.show_rainfall_sum(f"{value[1]}")
                    break
            # if date is selected
            elif data == value[0]:
                self.window.show_rainfall_sum(date)
                if value[1] is None:
                    self.window.show_rainfall_sum("No data")
                    break
                else:
                    self.window.show_rainfall_sum(f"{value[1]}")
                    break


class ThreadClass(QtCore.QThread):
    any_signal = QtCore.pyqtSignal(str)

    def __init__(self, parent=None, index=0):
        super(ThreadClass, self).__init__(parent)
        self.index = index
        self.is_running = True

    def run(self):
        print('Starting thread...', self.index)
        url = 'http://agromet.mkgp.gov.si/APP2/AgrometContent/xml/62.xml'
        self.any_signal.emit(url)

    def stop(self):
        self.is_running = False
        print('Stopping thread...', self.index)
        self.terminate()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    test_url = 'http://agromet.mkgp.gov.si/APP2/AgrometContent/xml/62.xml'
    run = MainApp("GUI.ui")
    # run.refresh(test_url)
