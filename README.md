# Qwt-6-Widget-Demo
The purpose of this project was to develop a means for using the QWT-6 widgets in the QT5/Python3 enviornment provided on the Raspberry Pi.
## Qwt Widgets on the Raspberry Pi
 Presently the Raspberian Stretch distro (Nov 2018 as of this writing) provides the Qwt widgets (ver 6.1.2-6) for the QT5 "Designer" GUI development tool. However a clean interface to the Python3 does not presently exist. Note that there is a Qwt version 5.2.3 in the distro that works well (including dynamic loading of the .ui file) however it only supports QT4 and python2 and the implimentation is not as rich as the Qwt-v6 widgets. Even more confusing is the inclusion of a version 5.2.1 Qwt5/QT4/Python2 set which has the plotting features but does not include the control and indicator widgets.
## QT Designer
![Hardware Setup](IMG/designerwidgets.PNG)*Designer Widget Set*
## Software
The joystick interface GUI is developed in LabVIEW (Ver.2014) and uses the LINX open source hardware periferal library by Digilent/LabVIEW MakerHub. LINX is used to develop embedded applications using LabVIEW and includes VIs for accessing peripherals like digital I/O, analog I/O, PWM, I2C, SPI, and UART. Here are the directions for adding [LINX support for the Arduino](https://www.labviewmakerhub.com/doku.php?id=learn:tutorials:libraries:linx:getting_started). Make sure NI VISA is installed for LabVIEW. LabVIEW communicates with the Arduino over a serial connection while the Arduino gaththers data from its various hardware interfaces.
![Diagram](IMG/JoystickBlockDiagram.PNG)*LabVIEW Block Diagram*
## Operation
The VI provides X and Y trim sliders to center the cursor on the graph screen. Moving the joystick results in cooresponding movement of the cursor and tracks the output voltages. Clicking the Joystick marks the selection temporarily with a red dot and records the selection in the controls and indicators section. A novel feature is a string indicator for the coordinates that track with the movement of the cursor.
![Demo](IMG/qwtdemo.gif)
