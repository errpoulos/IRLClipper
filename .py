import RPi.GPIO as GPIO
import time
import picamera
from io import BytesIO
import os
from screen import writeToScreen

camera = picamera.PiCamera()
camera.resolution = (1920, 1080)

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Button to GPIO23

GPIO.setwarnings(False)

def record():
    os.system('raspivid -o newvid.h264 -10000 -rf rgb -pf high -drc low -sa -50 -vs -br 40 -fps 30 -b 1200000000')
    os.system('MP4Box -add newvid.h264 newvid.mp4 -fps 32')
    os.system('omxplayer newvid.mp4')

try:
    while True:
        button_state = GPIO.input(23)
        if button_state == False:
            record()
            writeToScreen('Status:', 'recording...')
            time.sleep(10)
            writeToScreen('Status:', 'Converting to MP4...')

        else:
            break
except:
    GPIO.cleanup()
