# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 08:31:18 2019

@author: Le Quang Dung
"""

from PyQt5.QtWidgets import (QMainWindow, QTextEdit, QAction, QFileDialog, QApplication, QMessageBox)
from PyQt5.QtCore import *
from PyQt5.QtCore import QThread, pyqtSignal, QTimer
from PyQt5.QtGui import QPixmap, QImage
from PyQt5 import (QtWidgets, QtGui, QtCore) #uic
from ScanBundle import Ui_MainWindow
import sys
import os
import mysql.connector

import serial
import serial.tools.list_ports

import GRBL
import time
#import pandas as pd

import cv2
from pyzbar import pyzbar
#import argparse
import numpy
#import math

'''mydb=mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                passwd='123456',
                database="employee_performance_db"
        )

myCursor=mydb.cursor()'''


global s

class myWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(myWindow, self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)   
        self.ui.runCode_btn.setEnabled(True)
        #init Camera
#        self.init_webcam()
        #connect COM
        self.ui.comConnect_btn.clicked.connect(self.connect_event)
        #reset GRBL
        self.ui.resetMachine_btn.clicked.connect(self.resetZ_grbl)
        #auto level GRBL
        self.ui.autoLevel_btn.clicked.connect(self.autoLevel_grbl)
        #run code GRBL
        self.ui.runCode_btn.clicked.connect(self.runcode_event)
        
        self.grblRunThread=GRBLRunThread()
        self.grblRunThread.image_capture.connect(self.image_capture_thread)
        
    def runcode_event(self):
        #self.grblRunThread=GRBLRunThread()
        self.grblRunThread.start()
        #self.grblRunThread.image_capture.connect(self.image_capture_thread)
        
    def image_capture_thread(self, qimg1):
        qimg1=qimg1.scaled(480, 320)
        self.ui.webcam1.setPixmap(QPixmap.fromImage(qimg1))
        
    def connect_event(self):  
        if self.ui.comConnect_btn.text()=="CONNECT":
            self.ui.comConnect_btn.setEnabled(False)
            self.ui.comConnect_btn.setText("WAITING...")
            self.loadCOMThread=LoadCOMThread()
            self.loadCOMThread.start()
            self.loadCOMThread.result_connection.connect(self.connectCOM)
        else:
            self.ui.comConnect_btn.setText("CONNECT")
            self.ui.resetMachine_btn.setEnabled(False)
            self.ui.autoLevel_btn.setEnabled(False)
    
    def connectCOM(self,result):
        if result!="no":
            global s
            self.ui.comConnect_btn.setText("DISCONNECT")
            self.ui.comConnect_btn.setEnabled(True)
            self.ui.resetMachine_btn.setEnabled(True)
            self.ui.autoLevel_btn.setEnabled(True)
            s=serial.Serial(result, 115200)
        else:
            self.ui.comConnect_btn.setEnabled(True)
        
#    def init_webcam(self):
#        global capture1
#        global capture2
#        
#        capture1=cv2.VideoCapture(0, cv2.CAP_DSHOW)
#        capture2=cv2.VideoCapture(1, cv2.CAP_DSHOW)
#        focus1=35
#        #self.capture1.set(28, focus1)
#        capture1.set(3, 2304.0)
#        capture1.set(4, 1536.0)
#        capture1.set(cv2.CAP_PROP_FPS, 30.0)
#        focus2=35
#        #self.capture2.set(28, focus2)
#        capture2.set(3, 2304.0)
#        capture2.set(4, 1536.0)
#        capture2.set(cv2.CAP_PROP_FPS, 30.0)
        
    def resetZ_grbl(self):
        global s
        GRBL.init_reset_grbl(s)
        
    def autoLevel_grbl(self):
        global s
        GRBL.auto_level_grbl(s)
        
    def closeEvent(self, event):
        global s
#        GRBL.disconnect_grbl(s)
        #self.capture1.release()
        #self.capture2.release()

class LoadCOMThread(QtCore.QThread):
    def __init__(self, parent=None):
        super(LoadCOMThread, self).__init__(parent)
    
    result_connection=pyqtSignal(str)
    def run(self):
        result=GRBL.connect_grbl()
        self.result_connection.emit(result)
        
class GRBLRunThread(QtCore.QThread):
    image_capture=pyqtSignal(QImage)
    
    def __init__(self, parent=None):
        super(GRBLRunThread, self).__init__(parent)
        self.capture1=cv2.VideoCapture(0)
    
    def run(self):
        global s
        #GRBL.cycle_run(s)
        while True:
            ret1, frame1=self.capture1.read()
            img1=cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB)
            qimg1=QImage(img1.data, img1.shape[1], img1.shape[0], img1.strides[0], QImage.Format_RGB888)
            self.image_capture.emit(qimg1)
            
    def finished(self):
        self.capture1.release()
        
app=QtWidgets.QApplication([])
application=myWindow()
application.show()
sys.exit(app.exec())
