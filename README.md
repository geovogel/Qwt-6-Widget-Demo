# Qwt-6-Widget-Demo
The purpose of this project was to develop a means for using the QWT-6 widgets in the QT5/Python3 enviornment provided on the Raspberry Pi.
## Qwt Widgets on the Raspberry Pi
 Presently the Raspberian Stretch distro (ver. Nov-2018 as of this writing) provides a fairly up to date version of Qwt widgets (ver 6.1.2-6) for the QT5 "Designer" GUI development tool. However, a clean interface to the Python3 via PyQt5 does not presently exist. Note that there is a Qwt version 5.2.3 in the distro that works well (including dynamic loading of the .ui file) however it only supports QT4 and python2 and the implimentation is not as rich as the Qwt-v6 widgets. Even more confusing is the inclusion of a version 5.2.1 Qwt5/QT4/Python2 set which has the plotting features but does not include the control and indicator widgets. An end to end implimentation of QT5/Qwt6 to Python3 would be a great addition to the distro and would greatly benifit technical applications such as data acquisition and control.
## QT Toolchain
Solarized dark                                                            |  Qt5/Qwt6 Widget Palette
:------------------------------------------------------------------------:|:-----------------------------------------------------------:
The QT tool chain starts with the Designer application which is used to layout the widgets and set up many, but not all, of the widget attributes.  |<img src="https://github.com/geovogel/Qwt-6-Widget-Demo/blob/master/IMG/designerwidgets.PNG" width="150"  title="Qt5/Qwt6 Widget Palette">

![Demo](IMG/qwtdemo.gif)
