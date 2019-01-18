# Qwt-6-Widget-Demo
The purpose of this project was to develop a means for using the QWT-6 widgets in the QT5/Python3 enviornment provided on the Raspberry Pi.
## Qwt Widgets on the Raspberry Pi
 Presently the Raspberian Stretch distro (ver. Nov-2018 as of this writing) provides a fairly up to date version of Qwt widgets (ver 6.1.2-6) for the QT5 "Designer" GUI development tool. However, a clean interface to the Python3 via PyQt5 does not presently exist. Note that there is a Qwt version 5.2.3 in the distro that works well (including dynamic loading of the .ui file) however it only supports QT4 and python2 and the implimentation is not as rich as the Qwt-v6 widgets. Even more confusing is the inclusion of a version 5.2.1 Qwt5/QT4/Python2 set which has the plotting features but does not include the control and indicator widgets. An end to end implimentation of QT5/Qwt6 to Python3 would be a great addition to the distro and would greatly benifit technical applications such as data acquisition and control.
## QT Tool Chain
<div style="float: right">
<img src="IMG/designerwidgets.PNG" width="210" align="right" hspace="2" vspace="2
0" title="Qt5/Qwt6 Widget Palette">
The QT tool chain starts with the Qt "Designer" application which is used to layout the widgets and set up many, but not all, of the widget attributes. Most higher level attributes such as scale intervals and upper and lower bounds to values are avaiable for setting in Qt Designer. Other finer and more subtle detail attributes can be set as modifications to the widgets in the Python program itself through the PyQt5 wrapper which is the primary integration to Qt. Additional integrastion modules can be added to the core installation of PyQt5 and the <a href="https://github.com/GauiStori/PyQt-Qwt">PyQt-Qwt Python Wrapper</a> provides full feature support for the Qwt widget set. Although Debian Linux is supported difficulties were encountered in the build on the Rasperian distro version. From a non-developer point of view the issues appeared to be largely to do with version mismatches between the component applications and also with the SIP version. SIP is the C to python bindings that connects the QT to Python and anything in between. The PyQt-Qwt(Qwt6) author was gracious enough to create a backport version of the module for Rasperian Strech and was more than helpful in seeing me through the installation.
</div>

## Implimentation and Demo Program
Once the installation was sucessful a demo program was written in Python to excersce the widgets and establish a project template for future use. First consideration of the program was the inheritance structuring. In the past I have prefered using a multiple inheritanceapproach to designer forms and dynamicaslly loading the ui direvtly from the Python application. One aspect of the Demo program was to  


![Demo](IMG/qwtdemo.gif)
