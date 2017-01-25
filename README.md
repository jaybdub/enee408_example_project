ENEE408I Example Project
========================

Installation
------------

### Windows

1. Install Arduino 1.6+
2. Install the intel curie package (for arduino 101)
    1. Launch the arduino ide
    2. Tools->Boards->Board Manager
    3. Search 'Intel Curie Boards'
    4. Select install
3. Set the arduino sketchbook location to **enee408_example_project/arduino**
    1. Launch arduino ide
    2. File->Preferences->Sketchbook Location
4. Install Python 2.7 (Anaconda distribution)

### Linux (Ubuntu)

1. Install Arduino 1.6+ following [link](#).
2. Install the intel curie package (for arduino 101)
    1. Launch the arduino ide 
    2. Tools->Boards->Board Manager
    3. Search 'Intel Curie Boards'
    4. Select install
3. Set the arduino sketchbook location to **enee408_example_project/arduino**
    1. Launch arduino ide
    2. File->Preferences->Sketchbook Location
4. Run script to enable serial port.  In a terminal,
    1. cd ~/.arduino15/packages/Intel/tools/arduino101load/<version>/scripts
    2. sudo ./create_dfu_udev_rule
5. Python 2.7 should already by installed

Running Example
---------------

### Client Side (Arduino)

1.  Launch the Arduino IDE, ensure sketchbook location is correct.
2.  Open the serial_example sketch
3.  Upload it to the Arduino101

### Host Side (PC / Python)

1.  python serial_example.py <port_name>