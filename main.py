import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox
from PyQt5.QtCore import QRunnable, QThreadPool, pyqtSlot
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
        self.execute()
        self.threadpool = QThreadPool()
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

    def execute(self):
        url = 'http://agromet.mkgp.gov.si/APP2/AgrometContent/xml/62.xml'
        worker = Worker(self.refresh(url))


class Worker(QRunnable):
    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        # self.signals = WorkerSignals()

        # Add the callback to our kwargs
        # self.kwargs['progress_callback'] = self.signals.progress

    @pyqtSlot()
    def run(self):
        '''
        Initialise the runner function with passed args, kwargs.
        '''
        self.fn(*self.args, **self.kwargs)

if __name__ == '__main__':
    run = MainApp("GUI.ui")
    # test_url = 'http://agromet.mkgp.gov.si/APP2/AgrometContent/xml/62.xml'
    # run.refresh(test_url)

