import RPi.GPIO as GPIO
import time
import picamera
from io import BytesIO
import os

camera = picamera.PiCamera()
camera.resolution = (1920, 1080)

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Button to GPIO23
GPIO.setup(24, GPIO.OUT)  # LED to GPIO24


def record():
    camera.start_recording('new.h264')
    camera.wait_recording(10)
    camera.stop_recording()


try:
    while True:
        button_state = GPIO.input(23)
        if button_state == False:
            GPIO.output(24, True)
            print('recording...')
            record()
            time.sleep(10)
            print("Converting to MP4...")
            os.system("MP4Box -add new.h264 vid.mp4")

        else:
            GPIO.output(24, False)

except:
    GPIO.cleanup()
