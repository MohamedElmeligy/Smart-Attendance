# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TRIAL1.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import finalTrial as FaceRecognition
import objectDetection as ObjectDetection
import Attendance as Attendance
import cv2

loc = ("F:\PythonProjects\CS_Project\Mohamed_Elhadidi_CSCE201_G7.xlsx") 
attendance = []

class Ui_Attendence(object):
    def setupUi(self, Attendence):
        Attendence.setObjectName("Attendence")
        Attendence.resize(715, 510)
        self.pushButton = QtWidgets.QPushButton(Attendence)
        self.pushButton.setGeometry(QtCore.QRect(80, 300, 161, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Attendence)
        self.pushButton_2.setGeometry(QtCore.QRect(480, 300, 171, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Attendence)
        self.pushButton_3.setGeometry(QtCore.QRect(280, 300, 161, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(Attendence)
        self.label.setGeometry(QtCore.QRect(-60, -60, 841, 641))
        self.label.setStyleSheet("image: url(:/newPrefix/bg.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Attendence)
        self.label_2.setGeometry(QtCore.QRect(490, 140, 151, 141))
        self.label_2.setStyleSheet("image: url(:/newPrefix/face filter.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Attendence)
        self.label_3.setGeometry(QtCore.QRect(90, 140, 141, 141))
        self.label_3.setStyleSheet("image: url(:/newPrefix/face1.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Attendence)
        self.label_4.setGeometry(QtCore.QRect(290, 130, 151, 151))
        self.label_4.setStyleSheet("image: url(:/newPrefix/object recog.png);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        
        self.pushButton.clicked.connect(self.lunchFace)
        self.pushButton_3.clicked.connect(self.lunchObject)

        self.retranslateUi(Attendence)
        QtCore.QMetaObject.connectSlotsByName(Attendence)

    def retranslateUi(self, Attendence):
        _translate = QtCore.QCoreApplication.translate
        Attendence.setWindowTitle(_translate("Attendence", "Attendence System"))
        self.pushButton.setText(_translate("Attendence", "Face Detection"))
        self.pushButton_2.setText(_translate("Attendence", "Face Filter"))
        self.pushButton_3.setText(_translate("Attendence", "Object Recognition"))
    
    def lunchFace(self):
        FaceRecognition.run()
        attendance = FaceRecognition.attendance()
        print(attendance)
        
        rows,students,file = Attendance.readStudents(loc)
        print(rows,students,file)
        Attendance.writeAttendance(rows,attendance,students,file)        
       
        
    def lunchObject(self):
        ObjectDetection.run()

import s1
import s2
import s3
import sb


#if __name__ == "__main__":
    #import sys
    #app = QtWidgets.QApplication(sys.argv)
    #Attendence = QtWidgets.QDialog()
    #ui = Ui_Attendence()
    #ui.setupUi(Attendence)
    #Attendence.show()
    #app.exec_()
    
    