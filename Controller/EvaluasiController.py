

from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QWidget)
import os
import sys
from FormControl.ToolbarFolderSrc import ToolbarFolderSrc
from FormControl.TollbarFolderDetect import TollbarFolderDetect
from FormControl.ListImage import ListImage
from FormControl.BottomToolbar import BottomToolbar

class EvaluasiController(object):
    
    def __init__(self,parent):
        self.parent = parent
        self.ToolbarFolderSrc = ToolbarFolderSrc(self)
        self.TollbarFolderDetect = TollbarFolderDetect(self)
        self.BottomToolbar = BottomToolbar(self)

    def mainPage (self):
        self.widget = QtWidgets.QWidget(self.parent.containerVertical)
        self.widget.setMaximumSize(QtCore.QSize(1200, 900))
        self.widget.setObjectName("widget")
        self.ToolbarFolderSrc.Mainpage(self.widget)
        self.TollbarFolderDetect.Mainpage(self.widget)

        self.listImage1 = ListImage(self,QtCore.QRect(20, 120, 481, 420),160,100)
        self.listImage2 = ListImage(self,QtCore.QRect(530, 120, 481, 420),160,100)
        self.BottomToolbar.Mainpage(self.widget)

        return self.widget