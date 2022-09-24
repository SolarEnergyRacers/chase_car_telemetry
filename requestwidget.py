# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RequestWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication, QMetaObject
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QSizePolicy, QGridLayout, QLabel


class Ui_RequestWidget(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(298, 91)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lblId = QLabel(Form)
        self.lblId.setObjectName(u"lblId")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lblId.sizePolicy().hasHeightForWidth())
        self.lblId.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblId.setFont(font)

        self.gridLayout.addWidget(self.lblId, 0, 1, 1, 1)

        self.lblLastRequest = QLabel(Form)
        self.lblLastRequest.setObjectName(u"lblLastRequest")
        sizePolicy1.setHeightForWidth(self.lblLastRequest.sizePolicy().hasHeightForWidth())
        self.lblLastRequest.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.lblLastRequest, 1, 1, 1, 1)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.lblAttemptCount = QLabel(Form)
        self.lblAttemptCount.setObjectName(u"lblAttemptCount")
        sizePolicy1.setHeightForWidth(self.lblAttemptCount.sizePolicy().hasHeightForWidth())
        self.lblAttemptCount.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.lblAttemptCount, 2, 1, 1, 1)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)

        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")
        sizePolicy1.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)

        self.lblStatus = QLabel(Form)
        self.lblStatus.setObjectName(u"lblStatus")
        sizePolicy1.setHeightForWidth(self.lblStatus.sizePolicy().hasHeightForWidth())
        self.lblStatus.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.lblStatus, 3, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lblId.setText(QCoreApplication.translate("Form", u"txtId", None))
        self.lblLastRequest.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label.setText(QCoreApplication.translate("Form", u"id:", None))
        self.lblAttemptCount.setText(QCoreApplication.translate("Form", u"10", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"last request attempt:", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"attempt count", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"status", None))
        self.lblStatus.setText(QCoreApplication.translate("Form", u"open", None))
    # retranslateUi



