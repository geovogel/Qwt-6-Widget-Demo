#!/usr/bin/env python3

import sys
from PyQt5 import QtWidgets, QtGui, Qwt
from PyQt5.QtCore import Qt, QTimer       # QRectF, QPointF, qRound, pyqtSignal, QSize, QBasicTimer
from PyQt5.QtGui import QColor, QPalette  # QPainterPath, QPen, QPixmap, QFont, QIcon, QLinearGradient
from ui_QWTwidgetTest import Ui_mainWindow
import numpy as np
import math

# ======= QT SETUP =================================================================================


class MyApp(QtWidgets.QMainWindow):

    def __init__(self):
        super(MyApp, self).__init__()
        # Set up the user interface from Designer.
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)

# ======= LOCAL WIDGET MODIFICATIONS ===============================================================

        spdMeter   = self.ui.SpeedDial
        spdLCD     = self.ui.SpeedLCD
        spdWheel   = self.ui.SpeedWheel
        thermo     = self.ui.Thermo
        thermSlide = self.ui.ThermoSlider
        compass    = self.ui.Compass
        counter    = self.ui.Counter
        global clk
        clk = self.ui.AnalogClock

        # SPEEDOMETER SETUP
        palette2 = QPalette()
        palette2.setColor(QPalette.Base, Qt.black)
        palette2.setColor(QPalette.WindowText, QColor(Qt.darkBlue))
        palette2.setColor(QPalette.Text, Qt.yellow)
        palette2.setColor(QPalette.Dark, Qt.darkGray)       # Bezel ring color 1
        palette2.setColor(QPalette.Light, Qt.lightGray)     # Bezel Ring Color 2
        spdMeter.setPalette(palette2)
        needle = Qwt.QwtDialSimpleNeedle(Qwt.QwtDialSimpleNeedle.Arrow, True, Qt.red, QtGui.QColor(Qt.gray))
        spdMeter.setNeedle(needle)

        # THERMO SETUP
        colorMap = Qwt.QwtLinearColorMap()
        colorMap.setColorInterval(Qt.blue, Qt.red)
        thermo.setColorMap(colorMap)

        # COMPASS SETUP
        palette0 = QPalette()
        palette0.setColor(QPalette.Base, Qt.darkBlue)
        palette0.setColor(QPalette.WindowText, QColor(Qt.darkBlue))
        palette0.setColor(QPalette.Text, Qt.yellow)
        palette0.setColor(QPalette.Dark, Qt.darkGray)       # Bezel ring color 1
        palette0.setColor(QPalette.Light, Qt.lightGray)     # Bezel Ring Color 2
        compass.setPalette(palette0)
        # Tick marks for each degree
        CompSclDrw = Qwt.QwtCompassScaleDraw()
        CompSclDrw.enableComponent(Qwt.QwtAbstractScaleDraw.Ticks, True)
        CompSclDrw.enableComponent(Qwt.QwtAbstractScaleDraw.Labels, True)
        CompSclDrw.enableComponent(Qwt.QwtAbstractScaleDraw.Backbone, False)
        CompSclDrw.setTickLength(Qwt.QwtScaleDiv.MinorTick, 0)
        CompSclDrw.setTickLength(Qwt.QwtScaleDiv.MediumTick, 0)
        CompSclDrw.setTickLength(Qwt.QwtScaleDiv.MajorTick, 5)
        compass.setScaleDraw(CompSclDrw)
        compass.setNeedle(Qwt.QwtCompassMagnetNeedle(Qwt.QwtCompassMagnetNeedle.ThinStyle, Qt.darkBlue, Qt.red))

        # ANALOG CLOCK SETUP
        palette1 = QPalette()
        palette1.setColor(QPalette.Base, Qt.black)           # Clock number ring background
        palette1.setColor(QPalette.Text, Qt.yellow)          # Clock numbers color
        palette1.setColor(QPalette.Foreground, Qt.darkBlue)  # Inner Ring Color
        palette1.setColor(QPalette.Dark, Qt.darkGray)        # Bezel ring color 1
        palette1.setColor(QPalette.Light, Qt.lightGray)      # Bezel Ring Color 2
        clk.setPalette(palette1)
        # Disable minor ticks
        ClkSclDrw = Qwt.QwtRoundScaleDraw()
        ClkSclDrw.setTickLength(Qwt.QwtScaleDiv.MinorTick, 0)
        # Set color of clock hands
        knobColor = QColor(Qt.gray)
        for i in range(clk.NHands):
            handColor = QColor(Qt.gray)
            width = 8
            if i == clk.SecondHand:
                handColor = Qt.red
                knobColor = QColor(Qt.darkRed)
                width = 5
            hand = Qwt.QwtDialSimpleNeedle(Qwt.QwtDialSimpleNeedle.Arrow, True, handColor, knobColor)
            hand.setWidth(width)
            clk.setHand(clk.Hand(i), hand)

# ======= WIDGET CONNECTIONS =======================================================================

        spdMeter.setValue(self.ui.SpeedWheel.value())
        spdWheel.valueChanged['double'].connect(spdMeter.setValue)
        spdWheel.valueChanged['double'].connect(spdLCD.display)
        thermSlide.valueChanged['double'].connect(thermo.setValue)
        counter.valueChanged['double'].connect(compass.setValue)

# =======  SINE WAVE PLOT SETUP ====================================================================

        global ampKnob, frqKnob, maxPts, n, angle, xData, yData, curve, plot, deg
        ampKnob = self.ui.AmpKnob                # Amplitude knob object
        frqKnob = self.ui.FreqKnob               # Frequency knob object
        maxPts = 250                             # X axis range for plots
        xData = np.zeros(1, dtype=np.uint16)     # Buffer for x data
        yData = np.zeros(1, dtype=np.float32)    # Buffer for y Data
        n = 0                                    # loop counter and base for frequency steps
        angle = 0                                # Rotation angle along X axis for plots
        deg = u'\N{DEGREE SIGN}'
        plot = self.ui.qwtPlot                   # Plot object
        # plot.setTitle("SINE WAVE PLOT")
        # plot.insertLegend(Qwt.QwtLegend())
        plot.setCanvasBackground(Qt.black)
        plot.setAxisScale(2, 0, maxPts, 50)      # X bottom axis
        plot.setAxisMaxMinor(2, 5)
        plot.setAxisScale(0, -10, 10, 2)         # Y Left Axis
        plot.setAxisMaxMinor(0, 2)
        grid = Qwt.QwtPlotGrid()
        grid.setPen(Qt.darkGray, 0, Qt.DotLine)
        grid.attach(plot)
        curve = Qwt.QwtPlotCurve()
        # curve.setTitle("Some Points")
        curve.attach(plot)
        curve.setPen(Qt.yellow, 2)
        curve.setRenderHint(Qwt.QwtPlotItem.RenderAntialiased, True)
        # Start the loop function
        update()

# =======   UPDATE LOOP ===========================================================================


def update():
    global n, angle, maxPts, amp
    global ampKnob, frqKnob
    global xData, yData
    # Get control knob settings
    amp = ampKnob.value()
    freq = frqKnob.value() + 1   # Add 1 to freq value to avoid div by 0 error at f=0
    step = 360 / (freq * 10)     # calculate step size, scale to knob settings
    # Plot Data
    if n == 0:
        curve.setSamples(xData, yData)
        plot.replot()
        n += 1
        angle = angle + step
    elif 0 < n < maxPts:
        if angle <= 360:
            xData = np.append(xData, [n])
            yData = np.append(yData, (math.sin(math.radians(angle))) * amp)
            curve.setSamples(xData, yData)
            angle = angle + step
            n += 1
        else:
            yData[n-1] = 0
            curve.setSamples(xData, yData)
            angle = 0 + step
        plot.replot()
    elif n == maxPts:
        if angle <= 360:
            yData = np.roll(yData, -1)
            yData[maxPts-1] = math.sin(math.radians(angle)) * amp
            curve.setSamples(xData, yData)
            angle = angle + step
        else:
            yData[n - 1] = 0
            curve.setSamples(xData, yData)
            angle = 0 + step
        plot.replot()

    clk.setCurrentTime()             # Update  analog clock
    QTimer.singleShot(50, update)    # Repeat

# ======= MAIN CODE ================================================================================
# Create the Qt application "Qapplication"

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())