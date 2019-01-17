# Qwt-6-Widget-Demo
Demo of QWT v6 widgets on Raspberry Pi
The purpose of this project was to develop a process for using the QWT-6 widgets in the QT/Python enviornment provided on the Raspberry Pi. Presently the Raspberian Stretch distro (Nov 2018 as of this writing) provides the QWT widgets (ver 6.1.2-6)for the QT5 "Designer" GUI development tool.
## QT Designer
![Hardware Setup](IMG/designerwidget.png)*Designer Widget Set*
## Software
The joystick interface GUI is developed in LabVIEW (Ver.2014) and uses the LINX open source hardware periferal library by Digilent/LabVIEW MakerHub. LINX is used to develop embedded applications using LabVIEW and includes VIs for accessing peripherals like digital I/O, analog I/O, PWM, I2C, SPI, and UART. Here are the directions for adding [LINX support for the Arduino](https://www.labviewmakerhub.com/doku.php?id=learn:tutorials:libraries:linx:getting_started). Make sure NI VISA is installed for LabVIEW. LabVIEW communicates with the Arduino over a serial connection while the Arduino gaththers data from its various hardware interfaces.
![Diagram](IMG/JoystickBlockDiagram.PNG)*LabVIEW Block Diagram*
## Operation
The VI provides X and Y trim sliders to center the cursor on the graph screen. Moving the joystick results in cooresponding movement of the cursor and tracks the output voltages. Clicking the Joystick marks the selection temporarily with a red dot and records the selection in the controls and indicators section. A novel feature is a string indicator for the coordinates that track with the movement of the cursor.
![Demo](IMG/qwtdemo.gif)
