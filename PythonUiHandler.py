import sys
from PyQt5.QtWidgets import  QMainWindow, QApplication, QLabel
from PyQt5 import uic


class ShowApp(QMainWindow):
    def __init__(self, gui_ui):
        QMainWindow.__init__(self)
        # super(ShowApp, self).__init__()
        uic.loadUi(gui_ui, self)

        # self.show()

    def show_temp(self, value):
        label = self.findChild(QLabel, 'label_temperature_value')
        QLabel.setText(label, value)

    def show_rainfall_sum(self, value):
        label = self.findChild(QLabel, 'label_wind_value')
        QLabel.setText(label, value)

    def show_humidity(self, value):
        label = self.findChild(QLabel, 'label_humidity_value')
        QLabel.setText(label, value)

    def show_time(self, value):
        label = self.findChild(QLabel, 'label_date_value')
        QLabel.setText(label, value)


if __name__ == "__main__":
    ui = "GUI.ui"
    # App = ShowAppPiside(ui)

    app = QApplication(sys.argv)
    UIWindow = ShowApp(ui)
    UIWindow.show_temp("32")
    UIWindow.show_rainfall_sum("40")
    UIWindow.show_humidity("78")
    app.exec()

