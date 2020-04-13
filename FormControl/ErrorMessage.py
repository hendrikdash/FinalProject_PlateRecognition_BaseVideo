from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import ( QHBoxLayout, QLabel, QSizePolicy)
import os
import sys

class ErrorMessage(object):

    def __init__(self,QWidget,MainWindow):
        self.errorm = QtWidgets.QWidget(QWidget)
        self.errorm.setGeometry(QtCore.QRect(30, 550, 411, 30))
        self.errorm.setObjectName("errorm")
        self.horizontalErrormLayout = QtWidgets.QHBoxLayout(self.errorm)
        self.horizontalErrormLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalErrormLayout.setObjectName("horizontalErrormLayout")


        self.errorLabel = QLabel(QWidget)
        self.errorLabel.setGeometry(QtCore.QRect(30, 550, 411, 30))
        self.errorLabel.setSizePolicy(QSizePolicy.Preferred,
                QSizePolicy.Maximum)
        self.errorLabel.setObjectName("errorLabel")


 
 