from datetime import datetime
import time

from PyQt5 import QtWidgets, Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QTableWidgetItem

from mainwindow import Ui_MainWindow
from requestwidget import Ui_RequestWidget


class UIHandler(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, ch, parent=None):
        super(UIHandler, self).__init__(parent=parent)
        self.setupUi(self)
        self.ch = ch
        self.btnArrowRequest.clicked.connect(lambda: self.speedArrowRequest())
        self.btnInfoRequest.clicked.connect(lambda: self.driverInfoRequest())
        self.btnConsoleSend.clicked.connect(lambda: self.directConsoleCommand())

        self.out_req = []

    @pyqtSlot()
    def speedArrowRequest(self):
        req = "a"

        if self.rbArrowUp.isChecked():
            req += "u\n"
        elif self.rbArrowDown.isChecked():
            req += "d\n"
        else:
            req += "o\n"

        self.out_req.append(req)

    @pyqtSlot()
    def driverInfoRequest(self):
        req = ":" + self.txtlnInfoInput.text() + "\n"
        self.out_req.append(req)

    @pyqtSlot()
    def directConsoleCommand(self):
        req = self.txtlnConsoleCommand.text() + "\n"
        self.out_req.append(req)
        self.txtlnConsoleCommand.setText("")

    def setTelemetryAvailable(self, text):
        self.lblSerialConnected.setText(text)

    def setLastReceivedTime(self, text):
        self.lblLastReceived.setText(text)

    def setSpeedArrowState(self, text):
        self.lblSpeedArrowState.setText(text)

    def setDriverInfoState(self, text):
        self.lblInfoState.setText(text)

    def updateRequestList(self, reqs):
        pass