from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QWidget)

class ToolbarPage1(object):

    def __init__(self,QWidget,MainWindow):
        self.tollbarUp1 = QtWidgets.QWidget(QWidget)
        self.tollbarUp1.setGeometry(QtCore.QRect(31, 31, 981, 30))
        self.tollbarUp1.setObjectName("tollbarUp1")
        self.horizontalTollbarUp1Layout = QtWidgets.QHBoxLayout(self.tollbarUp1)
        self.horizontalTollbarUp1Layout.setContentsMargins(0, 0, 0, 0)
        self.horizontalTollbarUp1Layout.setObjectName("horizontalTollbarUp1Layout")
        self.label = QtWidgets.QLabel(self.tollbarUp1)
        self.label.setObjectName("label")
        self.horizontalTollbarUp1Layout.addWidget(self.label)
        self.progressBar = QtWidgets.QProgressBar(self.tollbarUp1)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.horizontalTollbarUp1Layout.addWidget(self.progressBar)

        self.buttonLoad = QtWidgets.QPushButton(self.tollbarUp1)
        self.buttonLoad.setObjectName("buttonLoad")
        self.horizontalTollbarUp1Layout.addWidget(self.buttonLoad)
        self.retranslateUi(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Path Video"))
        self.buttonLoad.setText(_translate("MainWindow", "Load"))



  