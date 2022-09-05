from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot

from mainwindow import Ui_MainWindow


class UIHandler(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, ch, parent=None):
        super(UIHandler, self).__init__(parent=parent)
        self.setupUi(self)
        self.ch = ch
        self.btnArrowRequest.clicked.connect(lambda: self.speedArrowRequest())
        self.btnInfoRequest.clicked.connect(lambda: self.driverInfoRequest())

    @pyqtSlot()
    def speedArrowRequest(self):
        if self.rbArrowUp.isChecked() and self.lblSpeedArrowState != "up":
            self.ch.setSpeedArrow("u", False)
        elif self.rbArrowDown.isChecked() and self.lblSpeedArrowState != "down":
            self.ch.setSpeedArrow("d", False)
        else:  # turn off
            # maybe adjust interface?
            if self.lblSpeedArrowState.text() == "up":
                self.ch.setSpeedArrow("u", True)
            elif self.lblSpeedArrowState.text() == "down":
                self.ch.setSpeedArrow("d", True)
            else:
                pass

    @pyqtSlot()
    def driverInfoRequest(self):
        txt = self.txtlnInfoInput.text()
        txt.strip().encode("ascii", "ignore")
        self.ch.setDriverInfo(self.cbInfoWarning.isChecked(), txt)

    def setTelemetryAvailable(self, text):
        self.lblSerialConnected.setText(text)

    def setLastReceivedTime(self, text):
        self.lblLastReceived.setText(text)

    def setSpeedArrowState(self, text):
        self.lblSpeedArrowState.setText(text)

    def setDriverInfoState(self, text):
        self.lblInfoState.setText(text)

    def updateRequestList(self):
        pass