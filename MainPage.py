import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi
import TRIAL1



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Attendence = QDialog()
    ui = TRIAL1.Ui_Attendence()
    ui.setupUi(Attendence)
    Attendence.show()
    app.exec_()
