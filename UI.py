# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Attendence(object):
    def setupUi(self, Attendence):
        Attendence.setObjectName("Attendence")
        Attendence.resize(715, 510)
        self.label = QtWidgets.QLabel(Attendence)
        self.label.setGeometry(QtCore.QRect(265, 150, 191, 141))
        self.label.setStyleSheet("image:url(:/newPrefix/object recog.png)")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Attendence)
        self.label_2.setGeometry(QtCore.QRect(416, 110, 301, 191))
        self.label_2.setStyleSheet("image:url(:/newPrefix/face filter.png)")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Attendence)
        self.label_3.setGeometry(QtCore.QRect(50, 150, 221, 141))
        self.label_3.setStyleSheet("image:url(:/newPrefix/face1.png)")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(Attendence)
        self.label_5.setGeometry(QtCore.QRect(-30, -60, 751, 581))
        self.label_5.setStyleSheet("image:url(:/newPrefix/bg.jpg)")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(Attendence)
        self.pushButton.setGeometry(QtCore.QRect(80, 300, 161, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Attendence)
        self.pushButton_2.setGeometry(QtCore.QRect(480, 300, 171, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Attendence)
        self.pushButton_3.setGeometry(QtCore.QRect(280, 300, 161, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_5.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()

        self.retranslateUi(Attendence)
        QtCore.QMetaObject.connectSlotsByName(Attendence)

    def retranslateUi(self, Attendence):
        _translate = QtCore.QCoreApplication.translate
        Attendence.setWindowTitle(_translate("Attendence", "Dialog"))
        self.pushButton.setText(_translate("Attendence", "Face Detection"))
        self.pushButton_2.setText(_translate("Attendence", "Face Filter"))
        self.pushButton_3.setText(_translate("Attendence", "Object Recognition"))

import source1
import source2
import source3
import source
