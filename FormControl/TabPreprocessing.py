from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QPushButton,QVBoxLayout,QTabWidget)
from FormControl.ToolbarPage2 import ToolbarPage2
from PyQt5.QtGui import QIcon,QPixmap



class TabPreprocessing(object):

    def __init__(self,parent):
        self.parent = parent

    def Mainpage(self):
        self.RotasiWiggets = QtWidgets.QWidget()
        self.RotasiWiggets.setObjectName("RotasiWiggets")
        self.RotasiWiggets.setGeometry(QtCore.QRect(10, 10, 140, 100))
        self.vertikalRotasiWiggetsLayout = QtWidgets.QVBoxLayout()
        self.vertikalRotasiWiggetsLayout.setObjectName("vertikalRotasiWiggetsLayout")
        self.horizontalRotasiWiggetsLayout = QtWidgets.QHBoxLayout()
        self.horizontalRotasiWiggetsLayout.setObjectName("horizontalRotasiWiggetsLayout")
        self.leftPixImage1 = QPixmap("images/defaultVideo1.png")
        self.gambar1 = QtWidgets.QLabel()
        self.gambar1.setPixmap(self.leftPixImage1)
        self.leftPixImage2 = QPixmap("images/defaultVideo1.png")
        self.gambar2 = QtWidgets.QLabel()
        self.gambar2.setPixmap(self.leftPixImage2)
        self.horizontalRotasiWiggetsLayout.addWidget(self.gambar1)
        self.horizontalRotasiWiggetsLayout.addWidget(self.gambar2)
        self.vertikalRotasiWiggetsLayout.addLayout(self.horizontalRotasiWiggetsLayout)
        self.horizontalRotasiWiggetsLayout2 = QtWidgets.QHBoxLayout()
        self.horizontalRotasiWiggetsLayout2.setObjectName("horizontalRotasiWiggetsLayout2")
        self.lineEdit1 = QtWidgets.QLabel()
        self.horizontalRotasiWiggetsLayout2.addWidget(self.lineEdit1)
        self.lineEdit2 = QtWidgets.QLineEdit("80%")
        self.horizontalRotasiWiggetsLayout2.addWidget(self.lineEdit2)
        spacerItem1 = QtWidgets.QSpacerItem(515, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalRotasiWiggetsLayout2.addItem(spacerItem1)
        self.vertikalRotasiWiggetsLayout.addLayout(self.horizontalRotasiWiggetsLayout2)
        self.horizontalRotasiWiggetsLayout3 = QtWidgets.QHBoxLayout()
        self.horizontalRotasiWiggetsLayout3.setObjectName("horizontalRotasiWiggetsLayout3")
        verticalSpacer = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalRotasiWiggetsLayout3.addItem(verticalSpacer)
        self.vertikalRotasiWiggetsLayout.addLayout(self.horizontalRotasiWiggetsLayout3)
        self.horizontalRotasiWiggetsLayout4 = QtWidgets.QHBoxLayout()
        self.horizontalRotasiWiggetsLayout4.setObjectName("horizontalRotasiWiggetsLayout3")
        spacerItem2 = QtWidgets.QSpacerItem(515, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalRotasiWiggetsLayout4.addItem(spacerItem2)
        self.ButtonProcess = QtWidgets.QPushButton()
        self.horizontalRotasiWiggetsLayout4.addWidget(self.ButtonProcess)
        self.vertikalRotasiWiggetsLayout.addLayout(self.horizontalRotasiWiggetsLayout4)
        self.RotasiWiggets.setLayout(self.vertikalRotasiWiggetsLayout)
        self.retranslateUi(self.parent)
        return self.RotasiWiggets

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.lineEdit1.setText(_translate("MainWindow", "MSE (Mean Square Error)"))
        self.ButtonProcess.setText(_translate("MainWindow", "Proses"))