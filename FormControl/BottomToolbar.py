from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import ( QWidget)



class BottomToolbar(object):

    def __init__(self,parent):
        self.parent = parent

    def Mainpage (self, Widget):
        self.tollbar1 = QtWidgets.QWidget(Widget)
        self.tollbar1.setGeometry(QtCore.QRect(31, 470, 981, 300))
        self.tollbar1.setObjectName("tollbar1")
        self.vertikaltollbar1Layout = QtWidgets.QVBoxLayout(self.tollbar1)
        self.vertikaltollbar1Layout.setObjectName("vertikaltollbar1Layout")
        self.horizontaltollbar1Layout = QtWidgets.QHBoxLayout()
        self.horizontaltollbar1Layout.setObjectName("horizontaltollbar1Layout")
        self.label1 = QtWidgets.QLabel()
        self.label1.setObjectName("label1")
        self.horizontaltollbar1Layout.addWidget(self.label1)
        self.lineEdit1 = QtWidgets.QLineEdit("80%")
        self.horizontaltollbar1Layout.addWidget(self.lineEdit1)
        spacerItem1 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontaltollbar1Layout.addItem(spacerItem1)
        self.label2 = QtWidgets.QLabel()
        self.label2.setObjectName("label2")
        self.horizontaltollbar1Layout.addWidget(self.label2)
        self.lineEdit2 = QtWidgets.QLineEdit("80%")
        self.horizontaltollbar1Layout.addWidget(self.lineEdit2)
        spacerItem2 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontaltollbar1Layout.addItem(spacerItem2)
        self.label3 = QtWidgets.QLabel()
        self.label3.setObjectName("label3")
        self.horizontaltollbar1Layout.addWidget(self.label3)
        self.lineEdit3 = QtWidgets.QLineEdit("80%")
        self.horizontaltollbar1Layout.addWidget(self.lineEdit3)
        spacerItem3 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontaltollbar1Layout.addItem(spacerItem3)
        self.vertikaltollbar1Layout.addLayout(self.horizontaltollbar1Layout)

        self.horizontaltollbar1Layout2 = QtWidgets.QHBoxLayout()
        self.horizontaltollbar1Layout2.setObjectName("horizontaltollbar1Layout2")
        spacerItem1 = QtWidgets.QSpacerItem(515, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontaltollbar1Layout2.addItem(spacerItem1)
        self.buttonProcess = QtWidgets.QPushButton()
        self.horizontaltollbar1Layout2.addWidget(self.buttonProcess)
        self.vertikaltollbar1Layout.addLayout(self.horizontaltollbar1Layout2)
        self.tollbar1.setLayout(self.vertikaltollbar1Layout)
        self.retranslateUi(self.parent)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.label1.setText(_translate("MainWindow", "Mean (Rata - Rata)"))
        self.label2.setText(_translate("MainWindow", "Rata - rata Macro"))
        self.label3.setText(_translate("MainWindow", "Rata - rata Micro"))
        self.buttonProcess.setText(_translate("MainWindow", "Proses"))


