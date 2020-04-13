from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (  QHBoxLayout, QWidget)



class MenuSideBar(object):

    def __init__(self, QHBoxLayout,QWidget):
        self.frame = QtWidgets.QFrame(QWidget)
        self.frame.setMaximumSize(QtCore.QSize(200, 900))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.layoutWidgetFrame = QtWidgets.QWidget(self.frame)
        self.layoutWidgetFrame.setGeometry(QtCore.QRect(30, 20, 140, 100))
        self.layoutWidgetFrame.setObjectName("layoutWidgetFrame")
        self.verticalLayoutFrame = QtWidgets.QVBoxLayout(self.layoutWidgetFrame)
        self.verticalLayoutFrame.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutFrame.setObjectName("verticalLayoutFrame")
        self.ButtonDeteksiVideo = QtWidgets.QPushButton(self.layoutWidgetFrame)
        self.ButtonDeteksiVideo.setObjectName("ButtonDeteksiVideo")
        self.verticalLayoutFrame.addWidget(self.ButtonDeteksiVideo)
        self.ButtonPreprocessing = QtWidgets.QPushButton(self.layoutWidgetFrame)
        self.ButtonPreprocessing.setObjectName("ButtonPreprocessing")
        self.verticalLayoutFrame.addWidget(self.ButtonPreprocessing)
        self.ButtonEvaluasi = QtWidgets.QPushButton(self.layoutWidgetFrame)
        self.ButtonEvaluasi.setObjectName("ButtonEvaluasi")
        self.verticalLayoutFrame.addWidget(self.ButtonEvaluasi)
        self.layoutWidgetFrame.raise_()
        self.retranslateUi(QWidget)
        #QHBoxLayout.addWidget(self.frame)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ButtonDeteksiVideo.setText(_translate("MainWindow", "Deteksi Video"))
        self.ButtonPreprocessing.setText(_translate("MainWindow", "Praprocessing Gambar"))
        self.ButtonEvaluasi.setText(_translate("MainWindow", "Evaluasi"))