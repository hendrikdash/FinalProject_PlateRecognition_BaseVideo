

from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QStyle,QWidget)
from PyQt5.QtGui import QIcon
from FormControl.ToolbarPage1 import ToolbarPage1
from FormControl.Toolbar2Page1 import Toolbar2Page1
from FormControl.VideoWindow import VideoWindow
from FormControl.ListImage import ListImage
from FormControl.ErrorMessage import ErrorMessage
import os
import sys

class DeteksiVideoController(object):
    
    def __init__(self,parent):
        self.parent = parent

    def mainPage (self):
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.widget = QtWidgets.QWidget(self.parent.containerVertical)
        self.widget.setObjectName("widget")
        self.ToolbarPage1 = ToolbarPage1(self.widget,self.parent.MainWindow)
        self.Toolbar2Page1 = Toolbar2Page1(self.widget,self.parent.MainWindow)
        self.videoWindow = VideoWindow(self,1100,750)
        self.Toolbar2Page1.buttonProses.clicked.connect(self.videoWindow.play)
        self.ToolbarPage1.buttonLoad.clicked.connect(self.parent.openFile)
        self.listImage = ListImage(self,QtCore.QRect(600, 120, 450, 531),210,150)
        self.ErrorMessage = ErrorMessage(self.widget,self.parent.MainWindow)
        self.parent.verticalLayout.addLayout(self.parent.horizontalLayout)
        self.Toolbar2Page1.horizontalSlider.raise_()

        return self.widget

        
    def handleError(self,message):
        self.Toolbar2Page1.buttonProses.setEnabled(False)
        self.ToolbarPage1.progressBar.setValue(0)
        self.ErrorMessage.errorLabel.setStyleSheet('QLabel#errorLabel {color: red; font: 16pt Arial}')
        self.ErrorMessage.errorLabel.setText("Error: " + message)

    def ResethandleError(self):
        self.ErrorMessage.errorLabel.setText("")