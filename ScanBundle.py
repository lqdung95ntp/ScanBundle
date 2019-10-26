# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ScanBundle.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1008, 638)
        font = QtGui.QFont()
        font.setPointSize(13)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 50, 991, 571))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.webcam1 = QtWidgets.QLabel(self.tab_2)
        self.webcam1.setGeometry(QtCore.QRect(10, 50, 480, 320))
        self.webcam1.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.webcam1.setText("")
        self.webcam1.setObjectName("webcam1")
        self.webcam2 = QtWidgets.QLabel(self.tab_2)
        self.webcam2.setGeometry(QtCore.QRect(500, 50, 480, 320))
        self.webcam2.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.webcam2.setText("")
        self.webcam2.setObjectName("webcam2")
        self.rgbColor_btn = QtWidgets.QPushButton(self.tab_2)
        self.rgbColor_btn.setGeometry(QtCore.QRect(500, 10, 101, 31))
        self.rgbColor_btn.setObjectName("rgbColor_btn")
        self.threshold_btn = QtWidgets.QPushButton(self.tab_2)
        self.threshold_btn.setGeometry(QtCore.QRect(610, 10, 141, 31))
        self.threshold_btn.setObjectName("threshold_btn")
        self.runCode_btn = QtWidgets.QPushButton(self.tab_2)
        self.runCode_btn.setEnabled(False)
        self.runCode_btn.setGeometry(QtCore.QRect(760, 10, 101, 31))
        self.runCode_btn.setObjectName("runCode_btn")
        self.resetMachine_btn = QtWidgets.QPushButton(self.tab_2)
        self.resetMachine_btn.setEnabled(False)
        self.resetMachine_btn.setGeometry(QtCore.QRect(240, 10, 121, 31))
        self.resetMachine_btn.setObjectName("resetMachine_btn")
        self.comConnect_btn = QtWidgets.QPushButton(self.tab_2)
        self.comConnect_btn.setGeometry(QtCore.QRect(110, 10, 121, 31))
        self.comConnect_btn.setObjectName("comConnect_btn")
        self.autoLevel_btn = QtWidgets.QPushButton(self.tab_2)
        self.autoLevel_btn.setEnabled(False)
        self.autoLevel_btn.setGeometry(QtCore.QRect(370, 10, 121, 31))
        self.autoLevel_btn.setObjectName("autoLevel_btn")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(170, 380, 131, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(670, 380, 131, 21))
        self.label_5.setObjectName("label_5")
        self.barcodesList1_txt = QtWidgets.QPlainTextEdit(self.tab_2)
        self.barcodesList1_txt.setGeometry(QtCore.QRect(10, 410, 481, 121))
        self.barcodesList1_txt.setObjectName("barcodesList1_txt")
        self.barcodesList2_txt = QtWidgets.QPlainTextEdit(self.tab_2)
        self.barcodesList2_txt.setGeometry(QtCore.QRect(500, 410, 481, 121))
        self.barcodesList2_txt.setObjectName("barcodesList2_txt")
        self.totalBarcode1_txt = QtWidgets.QLabel(self.tab_2)
        self.totalBarcode1_txt.setGeometry(QtCore.QRect(300, 380, 81, 21))
        self.totalBarcode1_txt.setObjectName("totalBarcode1_txt")
        self.totalBarcode2_txt = QtWidgets.QLabel(self.tab_2)
        self.totalBarcode2_txt.setGeometry(QtCore.QRect(800, 380, 81, 21))
        self.totalBarcode2_txt.setObjectName("totalBarcode2_txt")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget.addTab(self.tab_4, "")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(430, 10, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Run"))
        self.rgbColor_btn.setText(_translate("MainWindow", "RGB COLOR"))
        self.threshold_btn.setText(_translate("MainWindow", "THRESHOLD"))
        self.runCode_btn.setText(_translate("MainWindow", "RUN"))
        self.resetMachine_btn.setText(_translate("MainWindow", "RESET HOME"))
        self.comConnect_btn.setText(_translate("MainWindow", "CONNECT"))
        self.autoLevel_btn.setText(_translate("MainWindow", "GO TO TOP"))
        self.label_4.setText(_translate("MainWindow", "BARCODE LIST:"))
        self.label_5.setText(_translate("MainWindow", "BARCODE LIST:"))
        self.totalBarcode1_txt.setText(_translate("MainWindow", "0"))
        self.totalBarcode2_txt.setText(_translate("MainWindow", "0"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Test Camera"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Test Chương Trình"))
        self.label.setText(_translate("MainWindow", "CAMERA SCAN"))
