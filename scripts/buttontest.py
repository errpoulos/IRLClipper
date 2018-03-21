import RPi.GPIO as GPIO
import time
from io import BytesIO
import os



GPIO.setmode(GPIO.BCM)


GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)  #  Button to GPIO20
GPIO.setup(21, GPIO.OUT)  # LED to GPIO21

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Button to GPIO23
GPIO.setup(24, GPIO.OUT)  # LED to GPIO24

try:
    while True:
        button_state = GPIO.input(23)
        if button_state == False:
            GPIO.output(24, True)
            print('red on...')
            time.sleep(.2)
            GPIO.output(21, False)
        else:
            GPIO.output(24, False)
    

except:
    GPIO.cleanup()
    
    

try:
    while True:
        button_state = GPIO.input(20)
        if button_state == False:
            GPIO.output(21, True)
            print('green on...')
            time.sleep(1)
            GPIO.output(21, False)
        else:
            GPIO.output(21, False)
except:
    GPIO.cleanup()
        
        