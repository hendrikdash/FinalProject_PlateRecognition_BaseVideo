
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QApplication, QFileDialog, QHBoxLayout, QLabel, QAction,QListWidgetItem,QMainWindow,
        QPushButton, QSizePolicy, QSlider, QStyle, QVBoxLayout, QWidget,QTabWidget)
from FormControl.MenuSideBar import MenuSideBar
from Controller.DeteksiVideoController import DeteksiVideoController
from Controller.PreprocessingController import PreprocessingController
from Controller.EvaluasiController import EvaluasiController
import os
import sys

class MainWIndows(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("FirstPage")
        MainWindow.resize(1300, 750)
        MainWindow.setMaximumSize(QtCore.QSize(1300, 750))
        self.MainWindow = MainWindow
        self.containerVertical = QtWidgets.QWidget(MainWindow)
        self.containerVertical.setObjectName("containerVertical")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.containerVertical)
        self.verticalLayout.setObjectName("verticalLayout")
        self.menuSideBar = MenuSideBar(self.horizontalLayout,self.containerVertical)
        self.menuSideBar.ButtonDeteksiVideo.clicked.connect(self.funcDetekciVideo)
        self.menuSideBar.ButtonPreprocessing.clicked.connect(self.funcPreprocessing)
        self.menuSideBar.ButtonEvaluasi.clicked.connect(self.funcEvaluasi)
        
        self.DeteksiVideoController = DeteksiVideoController(self)
        self.halaman1 = self.DeteksiVideoController.mainPage()
        self.PreprocessingController = PreprocessingController(self)
        self.halaman2 = self.PreprocessingController.mainPage()
        self.EvaluasiController = EvaluasiController(self)
        self.halaman3 = self.EvaluasiController.mainPage()
        self.Home = self.initHome()
    
        self.verticalLayout.addLayout(self.Home.main_layout)
        MainWindow.setCentralWidget(self.containerVertical)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        


    def initHome(self):
        self.right_widget = QTabWidget()
        self.right_widget.tabBar().setObjectName("mainTab")
        self.right_widget.addTab(self.halaman1, '')
        self.right_widget.addTab(self.halaman2, '')
        self.right_widget.addTab(self.halaman3, '')
        self.right_widget.setCurrentIndex(0)
        self.right_widget.setStyleSheet('''QTabBar::tab{width: 0; \
            height: 0; margin: 0; padding: 0; border: none;}''')
        self.main_layout = QHBoxLayout()
        self.main_layout.addWidget(self.menuSideBar.frame)
        self.main_layout.addWidget(self.right_widget)
        self.main_layout.setStretch(0, 40)
        self.main_layout.setStretch(1, 200)
        return self

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate 


    def funcDetekciVideo(self):
        self.Home.right_widget.setCurrentIndex(0)
    
    def funcPreprocessing(self):
        self.Home.right_widget.setCurrentIndex(1)

    def funcEvaluasi(self):
        self.Home.right_widget.setCurrentIndex(2)

    
    def startProgress(self):
        self.completed = 0
        while self.completed < 100:
            self.completed += 0.0001
            self.DeteksiVideoController.ToolbarPage1.progressBar.setValue(self.completed)

    def openFile(self):
        fileName, _ = QFileDialog.getOpenFileName(self.MainWindow , "Open Movie",
                QtCore.QDir.homePath())
        filenames, file_extension = os.path.splitext(fileName)
        if file_extension == '.mp4' and filenames != '':
            self.DeteksiVideoController.videoWindow.setCapturing()
            self.startProgress()
            self.DeteksiVideoController.videoWindow.setFilePath(fileName)
            self.DeteksiVideoController.Toolbar2Page1.buttonProses.setEnabled(True)
            self.DeteksiVideoController.ResethandleError()
        else:
            self.DeteksiVideoController.handleError("Extensi Input Harus .mp4")



def closeEvent(self):
    if(self.DeteksiVideoController):
        self.DeteksiVideoController.videoWindow.setCapturing()


def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MainWIndows()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.aboutToQuit.connect(lambda:closeEvent(ui))
    sys.exit(app.exec_())

    

if __name__ == '__main__':
    main()