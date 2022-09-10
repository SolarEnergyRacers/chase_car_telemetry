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

        req_widg = Ui_RequestWidget()
        req_widg.setupUi(self.lstRequests)

        rowPosition = self.tblRequests.rowCount()
        self.tblRequests.insertRow(rowPosition)
        qtblw = QTableWidgetItem("    5") #.setTextAlignment(4)
        self.tblRequests.setItem(rowPosition, 0, qtblw)
        self.tblRequests.setItem(rowPosition, 1, QTableWidgetItem(time.strftime("%H:%M:%S")))
        self.tblRequests.setItem(rowPosition, 2, QTableWidgetItem("6"))
        self.tblRequests.setItem(rowPosition, 3, QTableWidgetItem("open"))

        self.out_req = []

    @pyqtSlot()
    def speedArrowRequest(self):
        self.ch.mutex.acquire()
        if self.rbArrowUp.isChecked():
            self.ch.setSpeedArrow("u")
        elif self.rbArrowDown.isChecked():
            self.ch.setSpeedArrow("d")
        else:
            self.ch.setSpeedArrow("o")
        self.ch.mutex.release()

    @pyqtSlot()
    def driverInfoRequest(self):
        txt = self.txtlnInfoInput.text()
        txt.strip().encode("ascii", "ignore")

        req = self.ch.getDriverInfoReq(self.cbInfoWarning.isChecked(), txt)
        self.out_req.append(req)

        #self.ch.mutex.acquire()
        #self.ch.setDriverInfo(self.cbInfoWarning.isChecked(), txt)
        #self.ch.mutex.release()

    def setTelemetryAvailable(self, text):
        self.lblSerialConnected.setText(text)

    def setLastReceivedTime(self, text):
        self.lblLastReceived.setText(text)

    def setSpeedArrowState(self, text):
        self.lblSpeedArrowState.setText(text)

    def setDriverInfoState(self, text):
        self.lblInfoState.setText(text)

    def updateRequestList(self, reqs):
        for req_id in reqs:
            print(req_id)
            print(reqs[req_id])
            print("----------")
            req = reqs[req_id]
            rowPosition = self.tblRequests.rowCount()
            self.tblRequests.setItem(rowPosition, 0, QTableWidgetItem(str(req_id)))
            self.tblRequests.setItem(rowPosition, 1, QTableWidgetItem(datetime.utcfromtimestamp(req.last_attempt).strftime("%H:%M:%S")))
            self.tblRequests.setItem(rowPosition, 2, QTableWidgetItem(str(req.attempt)))
            self.tblRequests.setItem(rowPosition, 3, QTableWidgetItem(req.done))