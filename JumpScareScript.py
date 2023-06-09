import serial

ser = serial.Serial('/dev/ttyACM0', 9600) # open serial port at 9600 bits per second

while True:
    line = ser.readline().decode('utf-8').rstrip() # read serial data as a string
    print(line) # print the received data
