import serial
import time

# Port of arduino (may be something like COM3 for windows, check arduino IDE)
arduino_port = '/dev/ttyACM0'

# Speeds to send [(durationSeconds, leftSpeed, rightSpeed), ...]
speeds = [
    (1.5, 0, 0),
    (1.0, 150, 150),
    (2.0, 0, 0),
    (2.0, -150, 150)
]

# Connect to serial port
ser = serial.Serial(port=arduino_port)

# Send speed pattern over and over
while True:
    for s in speeds:
        ser.write("%d, %d\n" % (s[1], s[2]))
        time.sleep(s[0])