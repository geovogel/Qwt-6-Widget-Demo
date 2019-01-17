# Qwt-6-Widget-Demo
The purpose of this project was to develop a means for using the QWT-6 widgets in the QT5/Python3 enviornment provided on the Raspberry Pi.
## Qwt Widgets on the Raspberry Pi
 Presently the Raspberian Stretch distro (ver. Nov-2018 as of this writing) provides a fairly up to date version of Qwt widgets (ver 6.1.2-6) for the QT5 "Designer" GUI development tool. However, a clean interface to the Python3 via PyQt5 does not presently exist. Note that there is a Qwt version 5.2.3 in the distro that works well (including dynamic loading of the .ui file) however it only supports QT4 and python2 and the implimentation is not as rich as the Qwt-v6 widgets. Even more confusing is the inclusion of a version 5.2.1 Qwt5/QT4/Python2 set which has the plotting features but does not include the control and indicator widgets. An end to end implimentation of QT5/Qwt6 to Python3 would be a great addition to the distro and would greatly benifit technical applications such as data acquisition and control.
## QT Toolchain
!<img src="https://github.com/geovogel/Qwt-6-Widget-Demo/blob/master/IMG/designerwidgets.PNG" width="150" title="Qt5/Qwt6 Widget Palette">
## Software

## Operation
The VI provides X and Y trim sliders to center the cursor on the graph screen. Moving the joystick results in cooresponding movement of the cursor and tracks the output voltages. Clicking the Joystick marks the selection temporarily with a red dot and records the selection in the controls and indicators section. A novel feature is a string indicator for the coordinates that track with the movement of the cursor.
![Demo](IMG/qwtdemo.gif)
