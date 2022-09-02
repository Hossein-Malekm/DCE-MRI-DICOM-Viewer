###########################################################
##
## BY: HOSSEIN M.MOHAMMADI
## PROJECT MADE WITH : Qt Designer and PyQt6
## v:1.0.0
## date : 2021
##
############################################################
## 
import os
from re import S 
os.system("pyuic6 show.ui -o show.py")
## ADD LIBARAIS
import sys
import numpy as np
from PyQt6.QtCore import (Qt,QTimer)
from PyQt6.QtWidgets import QMainWindow,QApplication,QFileDialog
import pyqtgraph as pg
from pydicom import dcmread
import random
# from pyqtgraph.Qt import QtGui
## ==> SPLASH SCREEN
from show import *
## ==> GLOBALS
run_path = os.getcwd()
## Configure plots
data = np.zeros((16,65,256,256))
time =65
x=0
class FIRST_WINDOW_CLASS(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.timer = QTimer()
        ## UI ==> INTERFACE CODE
        ## UI ==> INTERFACE CODE
        ######################################################
        # REMOVE TITILE BAR
        ######################################################
        self.ui.actionLoad_Data.triggered.connect(self.openFileNameDialog_loaddata)
        self.timer.timeout.connect(self.Slider_value_change)
        self.timer.setInterval(100)
        self.ui.horizontalSlider.valueChanged.connect(self.datachange)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.ui.actionExit.triggered.connect(sys.exit)
        self.ui.pushButton.clicked.connect(self.start)
        self.ui.pushButton_2.clicked.connect(self.stop)
        ## ==> END ##
    ## ==> APP FUNCTIONS
    def start(self):
        self.timer.start()
    def stop(self):
        self.timer.stop()
    def Slider_value_change(self):
        global x 
        if x > time :
            x = 1
        else :
            x = x+1
        self.ui.horizontalSlider.setValue(x)
        self.ui.label.setText(str(x))
    def datachange(self):
        global x
        if x > time :
            x = 1
        #1
        data2 = np.rot90(np.flipud(data[0,x-1,:,:]))
        img = pg.ImageItem(data2)
        vb = pg.ViewBox()
        vb.setAspectLocked()
        self.ui.widget_1.setCentralItem(vb)
        vb.addItem(img)
        vb.autoRange()
        #2
        data2 = np.rot90(np.flipud(data[1,x-1,:,:]))
        img = pg.ImageItem(data2)
        vb = pg.ViewBox()
        vb.setAspectLocked()
        self.ui.widget_2.setCentralItem(vb)
        vb.addItem(img)
        vb.autoRange()
        #3
        data2 = np.rot90(np.flipud(data[2,x-1,:,:]))
        img = pg.ImageItem(data2)
        vb = pg.ViewBox()
        vb.setAspectLocked()
        self.ui.widget_3.setCentralItem(vb)
        vb.addItem(img)
        vb.autoRange()
        #4
        data2 = np.rot90(np.flipud(data[3,x-1,:,:]))
        img = pg.ImageItem(data2)
        vb = pg.ViewBox()
        vb.setAspectLocked()
        self.ui.widget_4.setCentralItem(vb)
        vb.addItem(img)
        vb.autoRange()
        #5
        data2 = np.rot90(np.flipud(data[4,x-1,:,:]))
        img = pg.ImageItem(data2)
        vb = pg.ViewBox()
        vb.setAspectLocked()
        self.ui.widget_5.setCentralItem(vb)
        vb.addItem(img)
        vb.autoRange()
        #6
        data2 = np.rot90(np.flipud(data[5,x-1,:,:]))
        img = pg.ImageItem(data2)
        vb = pg.ViewBox()
        vb.setAspectLocked()
        self.ui.widget_6.setCentralItem(vb)
        vb.addItem(img)
        vb.autoRange()
        #7
        data2 = np.rot90(np.flipud(data[6,x-1,:,:]))
        img = pg.ImageItem(data2)
        vb = pg.ViewBox()
        vb.setAspectLocked()
        self.ui.widget_7.setCentralItem(vb)
        vb.addItem(img)
        vb.autoRange()
        #8
        data2 = np.rot90(np.flipud(data[7,x-1,:,:]))
        img = pg.ImageItem(data2)
        vb = pg.ViewBox()
        vb.setAspectLocked()
        self.ui.widget_8.setCentralItem(vb)
        vb.addItem(img)
        vb.autoRange()
        #9
        data2 = np.rot90(np.flipud(data[8,x-1,:,:]))
        img = pg.ImageItem(data2)        
        vb = pg.ViewBox()
        vb.setAspectLocked()
        self.ui.widget_9.setCentralItem(vb)
        vb.addItem(img)
        vb.autoRange()
        #10
        data2 = np.rot90(np.flipud(data[9,x-1,:,:]))
        img = pg.ImageItem(data2)
        vb = pg.ViewBox()
        vb.setAspectLocked()
        self.ui.widget_10.setCentralItem(vb)
        vb.addItem(img)
        vb.autoRange()
        #11
        data2 = np.rot90(np.flipud(data[10,x-1,:,:]))
        img = pg.ImageItem(data2)
        vb = pg.ViewBox()
        vb.setAspectLocked()
        self.ui.widget_11.setCentralItem(vb)
        vb.addItem(img)
        vb.autoRange()
        #12
        data2 = np.rot90(np.flipud(data[11,x-1,:,:]))
        img = pg.ImageItem(data2)
        vb = pg.ViewBox()
        vb.setAspectLocked()
        self.ui.widget_12.setCentralItem(vb)
        vb.addItem(img)
        vb.autoRange()
        #13
        data2 = np.rot90(np.flipud(data[12,x-1,:,:]))
        img = pg.ImageItem(data2)
        vb = pg.ViewBox()
        vb.setAspectLocked()
        self.ui.widget_13.setCentralItem(vb)
        vb.addItem(img)
        vb.autoRange()
        #14
        data2 = np.rot90(np.flipud(data[13,x-1,:,:]))
        img = pg.ImageItem(data2)
        vb = pg.ViewBox()
        vb.setAspectLocked()
        self.ui.widget_14.setCentralItem(vb)
        vb.addItem(img)
        vb.autoRange()
        #15
        data2 = np.rot90(np.flipud(data[14,x-1,:,:]))
        img = pg.ImageItem(data2)
        vb = pg.ViewBox()
        vb.setAspectLocked()
        self.ui.widget_15.setCentralItem(vb)
        vb.addItem(img)
        vb.autoRange()
        #16
        data2 = np.rot90(np.flipud(data[15,x-1,:,:]))
        img = pg.ImageItem(data2)
        vb = pg.ViewBox()
        vb.setAspectLocked()
        self.ui.widget_16.setCentralItem(vb)
        vb.addItem(img)
        vb.autoRange()
    def openFileNameDialog_loaddata(self):
        fileName = QFileDialog.getExistingDirectoryUrl(self)
        global data
        for i in range(1,17):
            target_path = fileName.url()[8::]+f'/{i}'
            if i < 10:
                for j in range(1,66):
                    if j < 10 :
                        filename2 = target_path + f'/0{j}-000{i}.dcm'
                        loaddata = dcmread(filename2)
                        data[i-1,j-1,:,:] = loaddata.pixel_array
                    if j >=10 :
                        filename2 = target_path + f'/{j}-000{i}.dcm'
                        loaddata = dcmread(filename2)
                        data[i-1,j-1,:,:] = loaddata.pixel_array
            else :
                for j in range(1,66):
                    if j < 10 :
                        filename2 = target_path + f'/0{j}-00{i}.dcm'
                        loaddata = dcmread(filename2)
                        data[i-1,j-1,:,:] = loaddata.pixel_array
                    if j >=10 :
                        filename2 = target_path + f'/{j}-00{i}.dcm'
                        loaddata = dcmread(filename2)
                        data[i-1,j-1,:,:] = loaddata.pixel_array
        global time
        time = (data.shape[1])
        self.ui.horizontalSlider.setMaximum(time)
        self.timer.setInterval(500)
        self.timer.timeout.connect(self.Slider_value_change)
        self.timer.start()

    #######################################################

## ==> MAIN CODE 
if __name__ =="__main__":
    app = QApplication(sys.argv)
    window = FIRST_WINDOW_CLASS()
    window.show()
    sys.exit(app.exec())
