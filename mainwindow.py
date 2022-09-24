# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowMavjrq.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(639, 609)
        icon = QIcon()
        iconThemeName = u"SER"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u"../../../../../.designer/backup", QSize(), QIcon.Normal, QIcon.Off)

        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.vertricalLayout_1 = QVBoxLayout()
        self.vertricalLayout_1.setObjectName(u"vertricalLayout_1")
        self.grpTelemetryInfo = QGroupBox(self.centralwidget)
        self.grpTelemetryInfo.setObjectName(u"grpTelemetryInfo")
        self.gridLayout = QGridLayout(self.grpTelemetryInfo)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_13 = QLabel(self.grpTelemetryInfo)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout.addWidget(self.label_13, 2, 0, 1, 1)

        self.lblLastReceived = QLabel(self.grpTelemetryInfo)
        self.lblLastReceived.setObjectName(u"lblLastReceived")

        self.gridLayout.addWidget(self.lblLastReceived, 1, 1, 1, 1)

        self.label_10 = QLabel(self.grpTelemetryInfo)
        self.label_10.setObjectName(u"label_10")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)

        self.gridLayout.addWidget(self.label_10, 0, 0, 1, 1)

        self.lblSerialConnected = QLabel(self.grpTelemetryInfo)
        self.lblSerialConnected.setObjectName(u"lblSerialConnected")

        self.gridLayout.addWidget(self.lblSerialConnected, 2, 1, 1, 1)

        self.label_11 = QLabel(self.grpTelemetryInfo)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 1, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 3, 0, 1, 1)

        self.vertricalLayout_1.addWidget(self.grpTelemetryInfo)

        self.grpSpeedArrow = QGroupBox(self.centralwidget)
        self.grpSpeedArrow.setObjectName(u"grpSpeedArrow")
        self.verticalLayout = QVBoxLayout(self.grpSpeedArrow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_4 = QLabel(self.grpSpeedArrow)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.verticalLayout.addWidget(self.label_4)

        self.label = QLabel(self.grpSpeedArrow)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.rbArrowUp = QRadioButton(self.grpSpeedArrow)
        self.rbArrowUp.setObjectName(u"rbArrowUp")

        self.horizontalLayout_3.addWidget(self.rbArrowUp)

        self.rbArrowOff = QRadioButton(self.grpSpeedArrow)
        self.rbArrowOff.setObjectName(u"rbArrowOff")

        self.horizontalLayout_3.addWidget(self.rbArrowOff)

        self.rbArrowDown = QRadioButton(self.grpSpeedArrow)
        self.rbArrowDown.setObjectName(u"rbArrowDown")

        self.horizontalLayout_3.addWidget(self.rbArrowDown)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.btnArrowRequest = QPushButton(self.grpSpeedArrow)
        self.btnArrowRequest.setObjectName(u"btnArrowRequest")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnArrowRequest.sizePolicy().hasHeightForWidth())
        self.btnArrowRequest.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.btnArrowRequest)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.grpSpeedArrow)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lblSpeedArrowState = QLabel(self.grpSpeedArrow)
        self.lblSpeedArrowState.setObjectName(u"lblSpeedArrowState")

        self.horizontalLayout_2.addWidget(self.lblSpeedArrowState)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.vertricalLayout_1.addWidget(self.grpSpeedArrow)

        self.grpDriverInfo = QGroupBox(self.centralwidget)
        self.grpDriverInfo.setObjectName(u"grpDriverInfo")
        self.verticalLayout_3 = QVBoxLayout(self.grpDriverInfo)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.line = QFrame(self.grpDriverInfo)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line)

        self.label_5 = QLabel(self.grpDriverInfo)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.verticalLayout_3.addWidget(self.label_5)

        self.label_6 = QLabel(self.grpDriverInfo)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_3.addWidget(self.label_6)

        self.txtlnInfoInput = QLineEdit(self.grpDriverInfo)
        self.txtlnInfoInput.setObjectName(u"txtlnInfoInput")
        self.txtlnInfoInput.setMaxLength(25)

        self.verticalLayout_3.addWidget(self.txtlnInfoInput)

        self.cbInfoWarning = QCheckBox(self.grpDriverInfo)
        self.cbInfoWarning.setObjectName(u"cbInfoWarning")

        self.verticalLayout_3.addWidget(self.cbInfoWarning)

        self.btnInfoRequest = QPushButton(self.grpDriverInfo)
        self.btnInfoRequest.setObjectName(u"btnInfoRequest")
        sizePolicy.setHeightForWidth(self.btnInfoRequest.sizePolicy().hasHeightForWidth())
        self.btnInfoRequest.setSizePolicy(sizePolicy)

        self.verticalLayout_3.addWidget(self.btnInfoRequest)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_7 = QLabel(self.grpDriverInfo)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_4.addWidget(self.label_7)

        self.lblInfoState = QLabel(self.grpDriverInfo)
        self.lblInfoState.setObjectName(u"lblInfoState")

        self.horizontalLayout_4.addWidget(self.lblInfoState)

        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.line_2 = QFrame(self.grpDriverInfo)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_2)

        self.grpConsoleCommand = QGroupBox(self.grpDriverInfo)
        self.grpConsoleCommand.setObjectName(u"grpConsoleCommand")
        self.verticalLayout_4 = QVBoxLayout(self.grpConsoleCommand)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(self.grpConsoleCommand)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setBold(True)
        font1.setWeight(75)
        self.label_3.setFont(font1)

        self.verticalLayout_4.addWidget(self.label_3)

        self.txtlnConsoleCommand = QLineEdit(self.grpConsoleCommand)
        self.txtlnConsoleCommand.setObjectName(u"txtlnConsoleCommand")

        self.verticalLayout_4.addWidget(self.txtlnConsoleCommand)

        self.btnConsoleSend = QPushButton(self.grpConsoleCommand)
        self.btnConsoleSend.setObjectName(u"btnConsoleSend")
        sizePolicy.setHeightForWidth(self.btnConsoleSend.sizePolicy().hasHeightForWidth())
        self.btnConsoleSend.setSizePolicy(sizePolicy)

        self.verticalLayout_4.addWidget(self.btnConsoleSend)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.verticalLayout_3.addWidget(self.grpConsoleCommand)

        self.vertricalLayout_1.addWidget(self.grpDriverInfo)

        self.vertricalLayout_1.setStretch(0, 1)
        self.vertricalLayout_1.setStretch(1, 1)

        self.horizontalLayout.addLayout(self.vertricalLayout_1)

        self.horizontalLayout.setStretch(0, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SER4 Telemetry", None))
        self.grpTelemetryInfo.setTitle("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Telemetry hardware available:", None))
        self.lblLastReceived.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Telemetry Info", None))
        self.lblSerialConnected.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Last Received Time:", None))
        self.grpSpeedArrow.setTitle("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Speed Arrow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Desired State:", None))
        self.rbArrowUp.setText(QCoreApplication.translate("MainWindow", u"Up", None))
        self.rbArrowOff.setText(QCoreApplication.translate("MainWindow", u"Off", None))
        self.rbArrowDown.setText(QCoreApplication.translate("MainWindow", u"Down", None))
        self.btnArrowRequest.setText(QCoreApplication.translate("MainWindow", u"Request", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Current State", None))
        self.lblSpeedArrowState.setText(QCoreApplication.translate("MainWindow", u"txtLblcurrentArrow", None))
        self.grpDriverInfo.setTitle("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Driver info", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Desired State: (ASCII chars)", None))
        self.cbInfoWarning.setText(QCoreApplication.translate("MainWindow", u"Warning", None))
        self.btnInfoRequest.setText(QCoreApplication.translate("MainWindow", u"Request", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Current State", None))
        self.lblInfoState.setText(QCoreApplication.translate("MainWindow", u"txtLblCurrentInfo", None))
        self.grpConsoleCommand.setTitle("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Direct Console Input", None))
        self.btnConsoleSend.setText(QCoreApplication.translate("MainWindow", u"Send", None))
    # retranslateUi
