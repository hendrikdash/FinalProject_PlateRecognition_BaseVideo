from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import ( QWidget)



class ToolbarFolderSrc(object):

    def __init__(self,parent):
        self.parent = parent

    def Mainpage (self, Widget):
        self.tollbarFolder1 = QtWidgets.QWidget(Widget)
        self.tollbarFolder1.setGeometry(QtCore.QRect(31, 31, 981, 30))
        self.tollbarFolder1.setObjectName("tollbarFolder1")
        self.horizontaltollbarFolder1Layout = QtWidgets.QHBoxLayout(self.tollbarFolder1)
        self.horizontaltollbarFolder1Layout.setContentsMargins(0, 0, 0, 0)
        self.horizontaltollbarFolder1Layout.setObjectName("horizontaltollbarFolder1Layout")
        self.labelTollbarFolder1 = QtWidgets.QLabel(self.tollbarFolder1)
        self.labelTollbarFolder1.setObjectName("labelTollbarFolder1")
        self.horizontaltollbarFolder1Layout.addWidget(self.labelTollbarFolder1)
        self.progressBar = QtWidgets.QProgressBar(self.tollbarFolder1)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.horizontaltollbarFolder1Layout.addWidget(self.progressBar)

        self.buttonLoadFolder = QtWidgets.QPushButton(self.tollbarFolder1)
        self.buttonLoadFolder.setObjectName("buttonLoadFolder")
        self.horizontaltollbarFolder1Layout.addWidget(self.buttonLoadFolder)
        self.retranslateUi(self.parent)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.labelTollbarFolder1.setText(_translate("MainWindow", "Path Folder"))
        self.buttonLoadFolder.setText(_translate("MainWindow", "  Load Folder Gambar Asli   "))


