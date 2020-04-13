from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QPushButton,QVBoxLayout,QTabWidget)
from FormControl.ToolbarPage2 import ToolbarPage2
from PyQt5.QtGui import QIcon,QPixmap
import os
import sys
from FormControl.TabPreprocessing import TabPreprocessing


class PreprocessingController(object):

    def __init__(self,parent):
        self.parent = parent


    def mainPage (self):
        self.widgetContainerPreprocessing = QtWidgets.QWidget(self.parent.containerVertical)
        self.widgetContainerPreprocessing.setMaximumSize(QtCore.QSize(1200, 900))
        self.widgetContainerPreprocessing.setObjectName("widgetContainerPreprocessing")

        self.verticalLayoutPage2 = QVBoxLayout()
        
        self.ToolbarPage2 = ToolbarPage2(self.widgetContainerPreprocessing,self.parent.MainWindow)
        
        # #self.ToolbarPage2.buttonLoadPage2.clicked.connect(self.openFile)

        self.verticalLayoutPage2.addWidget(self.ToolbarPage2.tollbarUpPage2)
        self.TabPreprocessing = TabPreprocessing(self)
        
        self.test1 =  self.TabPreprocessing.Mainpage()
        self.test2 =  self.TabPreprocessing.Mainpage()
        self.test3 =  self.TabPreprocessing.Mainpage()
        self.test4 =  self.TabPreprocessing.Mainpage()
        

        self.testTabe = QTabWidget(self.widgetContainerPreprocessing)
        self.testTabe.setContentsMargins(0, 100, 0, 0)
        self.testTabe.tabBar().setObjectName("mainTab")
        self.testTabe.addTab(self.test1, 'Rotasi')
        self.testTabe.addTab(self.test2, 'Blurring')
        self.testTabe.addTab(self.test3, 'Sharpening')
        self.testTabe.addTab(self.test4, 'Adaptive Threshold')
        
        self.testTabe.setCurrentIndex(0)

        self.verticalLayoutPage2.addWidget(self.testTabe)
        self.widgetContainerPreprocessing.setLayout(self.verticalLayoutPage2)
        self.testTabe.setStyleSheet('''
            QTabWidget::tab-bar {
                left: 5px;
                
            }
            QTabBar::tab{
                width: 200px; 
                height: 20; 
                margin-top: 10px; 
                padding: 5;
                border-width: 2px;
                border-style: solid;
                border-color: #DCDCDC;
                border-bottom-color: #00ffffff;
            }
            QTabBar::tab:selected {
                border-color: #DCDCDC;
                border-bottom-color: #00ffffff;
                background-color: #DCDCDC;
            }                                        
        ''')
        return self.widgetContainerPreprocessing

    