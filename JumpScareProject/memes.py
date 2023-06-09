"""
'publish.py'
=========================================
Publishes an incrementing value to a feed
Author(s): Brent Rubell, Todd Treece for Adafruit Industries
"""
# Import standard python modules
import time
from time import sleep
import serial
import cv2
from Adafruit_IO import Client, Feed, MQTTClient
import paho.mqtt.client as mqtt
import sys
# Import Adafruit IO REST client.
from Adafruit_IO import Client, Feed

# holds the count for the feed
peopleby = 0
run = True
ser = serial.Serial('COM8', 115200) # open serial port at 115200 bits per second 8  13
cap = cv2.VideoCapture("Jumpscare.mp4")
capneu = cv2.VideoCapture("NeutralVideo.mp4")
sound_file = 'audio.wav'
# Set to your Adafruit IO key.
# Remember, your key is a secret,
# so make sure not to publish it when you publish this code!
ADAFRUIT_IO_KEY = 'aio_RGaa86IrG8TsUrDV2itDwDdatHp2'

# Set to your Adafruit IO username.
# (go to https://accounts.adafruit.com to find your username)
ADAFRUIT_IO_USERNAME = 'Anthony000001'

# Create an instance of the REST client.
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

# Create a new feed named 'counter'
feed = Feed(name="peopleby")
#response = aio.create_feed(feed)

frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Define the new frame size for display
new_width = int(frame_width / 2)
new_height = int(frame_height / 2)


while True:
    message = "Hello, ESP32!"  # message to send

    ser.write(message.encode('utf-8'))  # send message over serial
   
    response = ser.readline().decode('utf-8').rstrip()  # read response from ESP32
    
    if response == '0':
        while cap.isOpened():
            ret, frame = cap.read() 
            if ret:
                cv2.imshow('Video', frame)      
                if cv2.waitKey(30) & 0xFF == ord('q'):
                    print("play")
                    break
            else:
                break     
        peopleby += 1
        sleep(1)
        aio.send_data('peopleby', peopleby)
        print('sending count: ', peopleby)
        #only prints when there is someone there
        cap.release()
        cv2.destroyAllWindows()
        response = '1'
        # if it doesnt restart it throttled out
        
    
        

    if response == '1':
        peopleby += 0
        print('sending count: ', peopleby)
        #to print the current total which wont be stuck for infinitley incrementing the value
        
        
        
        
        
            # plus 1 to how many people go past and gets sent to the dashboard
            
        
        # Adafruit IO is rate-limited for publishing
            # so we'll need a delay for calls to aio.send_data()
        

    
