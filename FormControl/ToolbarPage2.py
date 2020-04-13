from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QWidget)

class ToolbarPage2(object):

    def __init__(self,QWidget,MainWindow):
        self.tollbarUpPage2 = QtWidgets.QWidget(QWidget)
        self.tollbarUpPage2.setGeometry(QtCore.QRect(31, 31, 981, 30))
        self.tollbarUpPage2.setObjectName("tollbarUpPage2")
        self.horizontaltollbarUpPage2Layout = QtWidgets.QHBoxLayout(self.tollbarUpPage2)
        self.horizontaltollbarUpPage2Layout.setContentsMargins(0, 0, 0, 0)
        self.horizontaltollbarUpPage2Layout.setObjectName("horizontaltollbarUpPage2Layout")
        self.labelPage2 = QtWidgets.QLabel(self.tollbarUpPage2)
        self.labelPage2.setObjectName("label")
        self.horizontaltollbarUpPage2Layout.addWidget(self.labelPage2)
        self.progressBarPage2 = QtWidgets.QProgressBar(self.tollbarUpPage2)
        self.progressBarPage2.setProperty("value", 0)
        self.progressBarPage2.setObjectName("progressBarPage2")
        self.horizontaltollbarUpPage2Layout.addWidget(self.progressBarPage2)

        self.buttonLoadPage2 = QtWidgets.QPushButton(self.tollbarUpPage2)
        self.buttonLoadPage2.setObjectName("buttonLoadPage2")
        self.horizontaltollbarUpPage2Layout.addWidget(self.buttonLoadPage2)
        self.retranslateUi(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelPage2.setText(_translate("MainWindow", "Path Foto"))
        self.buttonLoadPage2.setText(_translate("MainWindow", "Load"))



  