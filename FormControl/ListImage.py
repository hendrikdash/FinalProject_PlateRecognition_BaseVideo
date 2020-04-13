
from PyQt5 import QtCore,QtWidgets
from PyQt5.QtWidgets import (QHBoxLayout, QLabel,QListWidgetItem, QVBoxLayout, QWidget)
from PyQt5.QtGui import QPixmap

class QCustomQWidget (QWidget):
    def __init__ (self, parent = None):
        super(QCustomQWidget, self).__init__(parent)
        self.textQVBoxLayout = QVBoxLayout()
        self.textUpQLabel    = QLabel()
        self.textDownQLabel  = QLabel()
        self.textQVBoxLayout.addWidget(self.textUpQLabel)
        self.textQVBoxLayout.addWidget(self.textDownQLabel)
        self.allQHBoxLayout  = QHBoxLayout()
        self.iconQLabel      = QLabel()
        self.allQHBoxLayout.addWidget(self.iconQLabel, 0)
        self.allQHBoxLayout.addLayout(self.textQVBoxLayout, 1)
        self.setLayout(self.allQHBoxLayout)
        # setStyleSheet
        self.textUpQLabel.setStyleSheet('''
            color: rgb(0, 0, 255);
        ''')
        self.textDownQLabel.setStyleSheet('''
            color: rgb(255, 0, 0);
        ''')

    def setTextUp (self, text):
        self.textUpQLabel.setText(text)

    def setTextDown (self, text):
        self.textDownQLabel.setText(text)

    def setIcon (self, imagePath):
        self.iconQLabel.setScaledContents(True)
        self.iconQLabel.setPixmap(QPixmap(imagePath))

    def setIconWH (self, iconW,iconH):
        self.iconQLabel.setFixedWidth(iconW)
        self.iconQLabel.setFixedHeight(iconH)


class ListImage(object):
    def __init__(self,parent,geomet,iconW,iconH):
        self.parent = parent
        self.MainPage(geomet,iconW,iconH)
    
    def MainPage(self,geomet,iconW,iconH):
        self.listWidget = QtWidgets.QListWidget(self.parent.widget)
        self.listWidget.setGeometry(geomet)
        self.listWidget.setObjectName("listWidget")
        for index, name, icon in [
            ('No.1', 'Meyoko',  'images/defaultVideo1.png'),
            ('No.2', 'Nyaruko', 'images/defaultVideo1.png'),
            ('No.3', 'Louise',  'images/defaultVideo1.png')]:
            # Create QCustomQWidget
            myQCustomQWidget = QCustomQWidget()
            myQCustomQWidget.setTextUp(index)
            myQCustomQWidget.setTextDown(name)
            myQCustomQWidget.setIcon(icon)
            myQCustomQWidget.setIconWH(iconW,iconH)
            myQListWidgetItem = QListWidgetItem(self.listWidget)
            myQListWidgetItem.setSizeHint(myQCustomQWidget.sizeHint())
            self.listWidget.addItem(myQListWidgetItem)
            self.listWidget.setItemWidget(myQListWidgetItem, myQCustomQWidget)
            self.listWidget.raise_()



