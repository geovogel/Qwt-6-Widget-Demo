# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer_qwt.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
from PyQt5.Qwt import *

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(800, 640)
        mainWindow.setAutoFillBackground(True)
        mainWindow.setStyleSheet("#centralwidget {\n"
"border: 3 px solid gray;\n"
"border-radius: 5px;\n"
"background: SteelBlue;\n"
"}\n"
"\n"
"#AnalogClock{\n"
"}\n"
"\n"
"#SpeedDial{\n"
"}\n"
"\n"
"#frame1, #frame2, #frame3, #frame4, #frame5{\n"
"background-color: LightSteelBlue;\n"
"}\n"
"\n"
"#SpeedLCD,  #TBD_LCD{\n"
"color: white;\n"
"background-color: darkBlue;\n"
"border-style: sunken;\n"
"border-width: 1px;\n"
"border-color: lightgrey;\n"
"border-radius: 1 px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.qwtPlot = QwtPlot(self.centralwidget)
        self.qwtPlot.setGeometry(QtCore.QRect(20, 20, 371, 200))
        self.qwtPlot.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.qwtPlot.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.qwtPlot.setObjectName("qwtPlot")
        self.AnalogClock = QwtAnalogClock(self.centralwidget)
        self.AnalogClock.setGeometry(QtCore.QRect(110, 370, 200, 200))
        self.AnalogClock.setProperty("value", 450.0)
        self.AnalogClock.setLineWidth(6)
        self.AnalogClock.setObjectName("AnalogClock")
        self.Compass = QwtCompass(self.centralwidget)
        self.Compass.setGeometry(QtCore.QRect(506, 316, 200, 200))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Compass.sizePolicy().hasHeightForWidth())
        self.Compass.setSizePolicy(sizePolicy)
        self.Compass.setBaseSize(QtCore.QSize(180, 180))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.Compass.setFont(font)
        self.Compass.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Compass.setAutoFillBackground(False)
        self.Compass.setScaleMaxMajor(30)
        self.Compass.setScaleStepSize(5.0)
        self.Compass.setProperty("value", 0.0)
        self.Compass.setInvertedControls(False)
        self.Compass.setLineWidth(6)
        self.Compass.setFrameShadow(QwtDial.Sunken)
        self.Compass.setMode(QwtDial.RotateScale)
        self.Compass.setOrigin(270.0)
        self.Compass.setObjectName("Compass")
        self.Counter = QwtCounter(self.centralwidget)
        self.Counter.setGeometry(QtCore.QRect(513, 524, 181, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Counter.sizePolicy().hasHeightForWidth())
        self.Counter.setSizePolicy(sizePolicy)
        self.Counter.setMaximum(360.0)
        self.Counter.setSingleStep(1.0)
        self.Counter.setNumButtons(3)
        self.Counter.setStepButton2(5)
        self.Counter.setStepButton3(10)
        self.Counter.setWrapping(False)
        self.Counter.setObjectName("Counter")
        self.SpeedDial = QwtDial(self.centralwidget)
        self.SpeedDial.setGeometry(QtCore.QRect(420, 22, 200, 200))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.SpeedDial.setFont(font)
        self.SpeedDial.setUpperBound(80.0)
        self.SpeedDial.setScaleStepSize(5.0)
        self.SpeedDial.setLineWidth(6)
        self.SpeedDial.setMinScaleArc(30.0)
        self.SpeedDial.setMaxScaleArc(330.0)
        self.SpeedDial.setObjectName("SpeedDial")
        self.ThermoSlider = QwtSlider(self.centralwidget)
        self.ThermoSlider.setGeometry(QtCore.QRect(710, 20, 64, 250))
        self.ThermoSlider.setTrough(True)
        self.ThermoSlider.setGroove(True)
        self.ThermoSlider.setBorderWidth(4)
        self.ThermoSlider.setObjectName("ThermoSlider")
        self.Thermo = QwtThermo(self.centralwidget)
        self.Thermo.setGeometry(QtCore.QRect(646, 27, 60, 234))
        self.Thermo.setAlarmEnabled(True)
        self.Thermo.setBorderWidth(3)
        self.Thermo.setPipeWidth(12)
        self.Thermo.setObjectName("Thermo")
        self.SpeedWheel = QwtWheel(self.centralwidget)
        self.SpeedWheel.setGeometry(QtCore.QRect(460, 237, 131, 24))
        self.SpeedWheel.setMaximum(80.0)
        self.SpeedWheel.setViewAngle(175.0)
        self.SpeedWheel.setTickCount(18)
        self.SpeedWheel.setBorderWidth(3)
        self.SpeedWheel.setObjectName("SpeedWheel")
        self.SpeedoLbl = QwtTextLabel(self.centralwidget)
        self.SpeedoLbl.setGeometry(QtCore.QRect(465, 260, 121, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.SpeedoLbl.setFont(font)
        self.SpeedoLbl.setIndent(0)
        self.SpeedoLbl.setObjectName("SpeedoLbl")
        self.SpeedLCD = QtWidgets.QLCDNumber(self.centralwidget)
        self.SpeedLCD.setGeometry(QtCore.QRect(500, 176, 40, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.SpeedLCD.setFont(font)
        self.SpeedLCD.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.SpeedLCD.setLineWidth(1)
        self.SpeedLCD.setSmallDecimalPoint(True)
        self.SpeedLCD.setDigitCount(2)
        self.SpeedLCD.setSegmentStyle(QtWidgets.QLCDNumber.Outline)
        self.SpeedLCD.setProperty("intValue", 0)
        self.SpeedLCD.setObjectName("SpeedLCD")
        self.CompassLbl = QwtTextLabel(self.centralwidget)
        self.CompassLbl.setGeometry(QtCore.QRect(540, 554, 121, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.CompassLbl.setFont(font)
        self.CompassLbl.setIndent(0)
        self.CompassLbl.setObjectName("CompassLbl")
        self.ThremoLbl = QwtTextLabel(self.centralwidget)
        self.ThremoLbl.setGeometry(QtCore.QRect(643, 260, 121, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.ThremoLbl.setFont(font)
        self.ThremoLbl.setIndent(0)
        self.ThremoLbl.setObjectName("ThremoLbl")
        self.frame1 = QtWidgets.QFrame(self.centralwidget)
        self.frame1.setGeometry(QtCore.QRect(639, 10, 150, 280))
        self.frame1.setMinimumSize(QtCore.QSize(0, 0))
        self.frame1.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame1.setLineWidth(4)
        self.frame1.setMidLineWidth(3)
        self.frame1.setObjectName("frame1")
        self.frame2 = QtWidgets.QFrame(self.centralwidget)
        self.frame2.setGeometry(QtCore.QRect(409, 10, 221, 280))
        self.frame2.setMinimumSize(QtCore.QSize(0, 0))
        self.frame2.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame2.setLineWidth(4)
        self.frame2.setMidLineWidth(3)
        self.frame2.setObjectName("frame2")
        self.frame3 = QtWidgets.QFrame(self.centralwidget)
        self.frame3.setGeometry(QtCore.QRect(409, 300, 379, 280))
        self.frame3.setMinimumSize(QtCore.QSize(0, 0))
        self.frame3.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame3.setLineWidth(4)
        self.frame3.setMidLineWidth(3)
        self.frame3.setObjectName("frame3")
        self.frame4 = QtWidgets.QFrame(self.centralwidget)
        self.frame4.setGeometry(QtCore.QRect(10, 10, 391, 341))
        self.frame4.setMinimumSize(QtCore.QSize(0, 0))
        self.frame4.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame4.setLineWidth(4)
        self.frame4.setMidLineWidth(3)
        self.frame4.setObjectName("frame4")
        self.AmpLbl = QwtTextLabel(self.frame4)
        self.AmpLbl.setGeometry(QtCore.QRect(70, 316, 121, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.AmpLbl.setFont(font)
        self.AmpLbl.setIndent(0)
        self.AmpLbl.setObjectName("AmpLbl")
        self.FreqLbl = QwtTextLabel(self.frame4)
        self.FreqLbl.setGeometry(QtCore.QRect(235, 316, 121, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FreqLbl.sizePolicy().hasHeightForWidth())
        self.FreqLbl.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.FreqLbl.setFont(font)
        self.FreqLbl.setIndent(0)
        self.FreqLbl.setObjectName("FreqLbl")
        self.AmpKnob = QwtKnob(self.frame4)
        self.AmpKnob.setGeometry(QtCore.QRect(77, 217, 112, 112))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.AmpKnob.setFont(font)
        self.AmpKnob.setScaleMaxMajor(10)
        self.AmpKnob.setScaleMaxMinor(1)
        self.AmpKnob.setScaleStepSize(1.0)
        self.AmpKnob.setProperty("value", 5.0)
        self.AmpKnob.setKnobStyle(QwtKnob.Sunken)
        self.AmpKnob.setKnobWidth(60)
        self.AmpKnob.setMarkerStyle(QwtKnob.Triangle)
        self.AmpKnob.setMarkerSize(12)
        self.AmpKnob.setBorderWidth(4)
        self.AmpKnob.setObjectName("AmpKnob")
        self.FreqKnob = QwtKnob(self.frame4)
        self.FreqKnob.setGeometry(QtCore.QRect(239, 217, 112, 112))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.FreqKnob.setFont(font)
        self.FreqKnob.setScaleMaxMajor(10)
        self.FreqKnob.setScaleMaxMinor(1)
        self.FreqKnob.setScaleStepSize(1.0)
        self.FreqKnob.setProperty("value", 5.0)
        self.FreqKnob.setKnobStyle(QwtKnob.Sunken)
        self.FreqKnob.setKnobWidth(60)
        self.FreqKnob.setMarkerStyle(QwtKnob.Triangle)
        self.FreqKnob.setMarkerSize(12)
        self.FreqKnob.setBorderWidth(4)
        self.FreqKnob.setObjectName("FreqKnob")
        self.AmpLbl.raise_()
        self.FreqLbl.raise_()
        self.AmpKnob.raise_()
        self.qwtPlot.raise_()
        self.qwtPlot.raise_()
        self.FreqKnob.raise_()
        self.frame5 = QtWidgets.QFrame(self.centralwidget)
        self.frame5.setGeometry(QtCore.QRect(10, 359, 391, 221))
        self.frame5.setMinimumSize(QtCore.QSize(0, 0))
        self.frame5.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame5.setLineWidth(4)
        self.frame5.setMidLineWidth(3)
        self.frame5.setObjectName("frame5")
        self.frame5.raise_()
        self.frame4.raise_()
        self.frame3.raise_()
        self.frame2.raise_()
        self.frame1.raise_()
        self.qwtPlot.raise_()
        self.AnalogClock.raise_()
        self.Compass.raise_()
        self.Counter.raise_()
        self.SpeedDial.raise_()
        self.ThermoSlider.raise_()
        self.Thermo.raise_()
        self.SpeedWheel.raise_()
        self.SpeedoLbl.raise_()
        self.SpeedLCD.raise_()
        self.CompassLbl.raise_()
        self.ThremoLbl.raise_()
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Demo for QWT Widgets"))
        self.SpeedoLbl.setPlainText(_translate("mainWindow", "Set Speedometer"))
        self.CompassLbl.setPlainText(_translate("mainWindow", "Set Compass"))
        self.ThremoLbl.setPlainText(_translate("mainWindow", "Set Thermo"))
        self.AmpLbl.setPlainText(_translate("mainWindow", "Set Amplitude"))
        self.FreqLbl.setPlainText(_translate("mainWindow", "Set Frequency"))

