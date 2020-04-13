from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import ( QWidget)



class Toolbar2Page1(object):

    def __init__(self,QWidget,MainWindow):

        self.tollbarUp2 = QtWidgets.QWidget(QWidget)
        self.tollbarUp2.setGeometry(QtCore.QRect(31, 71, 981, 30))
        self.tollbarUp2.setObjectName("tollbarUp2")
        self.horizontaltollbarUp2Layout = QtWidgets.QHBoxLayout(self.tollbarUp2)
        self.horizontaltollbarUp2Layout.setContentsMargins(0, 0, 0, 0)
        self.horizontaltollbarUp2Layout.setObjectName("horizontaltollbarUp2Layout")
        self.horizontalSlider = QtWidgets.QSlider(self.tollbarUp2)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider.setRange(0, 0)
        self.horizontalSlider.setEnabled(False)
        #self.horizontalSlider.sliderMoved.connect(self.setPosition)
        self.horizontaltollbarUp2Layout.addWidget(self.horizontalSlider)
        # spacerItem = QtWidgets.QSpacerItem(128, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        # self.horizontalLayout_3.addItem(spacerItem)
        self.buttonProses = QtWidgets.QPushButton(self.tollbarUp2)
        self.buttonProses.setObjectName("buttonProses")
        self.buttonProses.setEnabled(False)
        #self.buttonProses.clicked.connect(self.play)
        self.horizontaltollbarUp2Layout.addWidget(self.buttonProses)
        

        self.retranslateUi(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.buttonProses.setText(_translate("MainWindow", "Proses"))


