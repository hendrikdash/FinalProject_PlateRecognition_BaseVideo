from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QLabel
from PyQt5.QtWidgets import QWidget, QAction, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QFont, QPainter, QImage, QTextCursor, QPixmap
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, QPoint, pyqtSignal
from PyQt5.QtWidgets import QWidget, QAction, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QFont, QPainter, QImage, QTextCursor
import queue as Queue
import time, threading, cv2
import numpy as np
import queue as Queue
import os


delayVideo = 5
image_queue = Queue.Queue()
capturing   = True              
cvNet = cv2.dnn.readNetFromTensorflow("D:/Skripsi/OpencvCode/FinalProject/Model/SSD_Kendaraan/frozen_inference_graph.pb", "D:/Skripsi/OpencvCode/View/Model/graph_kendaraan.pbtxt")
fourcc = cv2.VideoWriter_fourcc(*'XVID')

def deteksiVideo(fileInput, queue, self):
    position = 0
    index = 0
    cap = cv2.VideoCapture(fileInput)
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    seconds = int(frame_count / fps)
    self.parent.Toolbar2Page1.horizontalSlider.setRange(0, seconds )
    tmpFps = fps
    while capturing:
        rects = []
        if cap.grab():
            retval, frame = cap.retrieve(0)
            posFrame = cap.get(cv2.CAP_PROP_POS_FRAMES)
            overlay = frame.copy()
            (h, w) = frame.shape[:2]
            contours = np.array([[[0, (h//2)+150],[w, (h//2)+150],[w, (h//2)+550],[0, (h//2)+550]]], np.int32)
            alpha = 0.5
            cv2.drawContours(overlay, contours, -1, (255,0,0), 2)
            frame = cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0)
            cvNet.setInput(cv2.dnn.blobFromImage(frame, size=(300, 300), swapRB=True, crop=False))
            start = time.time()
            layerOutputs = cvNet.forward()
            end = time.time()
            for i in np.arange(0, layerOutputs.shape[2]):
                confidence = layerOutputs[0, 0, i, 2]
                idx = int(layerOutputs[0, 0, i, 1])
                box = layerOutputs[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = box.astype("int")
                if confidence > 0.6 and idx in [0,3,4,6,8]:
                    centro = ((startX+endX)//2, (startY+endY)//2)
                    point = cv2.pointPolygonTest(contours, centro, False)
                    drawCropDetect = frame[startY:endY, startX:endX]
                    if int(point) == 1:
                        path = "cropKendaraan/"+str(i)+".jpg"
                        isFile = os.path.isfile(path)
                        if not isFile and np.sum(drawCropDetect) != 0:
                            cv2.imwrite(path, drawCropDetect)
                    #cv2.rectangle(frame, (startX, startY), (endX, endY),(0,0,255), 2)
                
            
            if frame is not None and queue.qsize() < 2:
                queue.put(frame)
            else:
                time.sleep(delayVideo / 1000.0)

            if(index >= tmpFps or int(posFrame) ==  frame_count - 1):
                tmpFps = tmpFps + fps
                position += 1
                self.parent.Toolbar2Page1.horizontalSlider.setValue(position)
            index+=1
        else:
            break
    cap.release()


class ImageWidget(QWidget):
    def __init__(self, parent=None):
        super(ImageWidget, self).__init__(parent)
        self.image = None

    def setImage(self, image):
        self.image = image
        self.setGeometry(QtCore.QRect(30, 120, 480, 401))
        self.setMaximumSize(QtCore.QSize(800, 800))
        self.setMinimumSize(image.size())
        self.setObjectName("videoWindow")
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        if self.image:
            qp.drawImage(QPoint(0, 0), self.image)
        qp.end()

class VideoWindow(object):

    def __init__(self,parent, width, height):
        self.parent = parent
        self.mediaPlayer = self.parent.mediaPlayer
        self.MainWindow = self.parent.parent.MainWindow
        #self.Mainpage()
        self.width = width
        self.height = height
        self.filePath = ""
        self.MainpageOpencv()
        self.threads = None


    def MainpageOpencv(self):
        self.disp = ImageWidget(self.parent.widget)
        self.defaultImage = QtWidgets.QLabel(self.parent.widget)
        self.defaultImage.setGeometry(QtCore.QRect(30, 55, 480, 491))
        self.defaultImage.setText("")
        self.defaultImage.setPixmap(QtGui.QPixmap("images/defaultVideo1.png"))
        self.defaultImage.setObjectName("defaultImage")
        self.defaultImage.raise_()
        self.disp.raise_()
        return self
       
    def play(self):
        global capturing
        capturing = True
        self.timer = QTimer()
        self.timer.timeout.connect(lambda:self.tampilGambar(image_queue, self.disp))
        self.timer.start(delayVideo)
        self.threads = threading.Thread(target=deteksiVideo,args=(self.filePath, image_queue, self))
        self.threads.start()  
        self.defaultImage.hide()

    def tampilGambar(self, imageqs, display):
        if not imageqs.empty():
            image = imageqs.get()
            if image is not None and len(image) > 0:
                img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                self.tampilkanGambar(img, display)


    def tampilkanGambar(self, img, display):
        dispSize = self.width//2, self.height//2
        disp_bpl = dispSize[0] * 3
        img = cv2.resize(img, dispSize,interpolation=cv2.INTER_CUBIC)
        qimg = QImage(img.data, dispSize[0], dispSize[1], disp_bpl, QImage.Format_RGB888)
        display.setImage(qimg)

    
    def setFilePath(self,path):
        self.filePath = str(path)

    def setCapturing(self):
        global capturing
        capturing = False
        self.parent.Toolbar2Page1.horizontalSlider.setValue(0)
        if(self.threads):
            self.threads.join()
        

