import RPi.GPIO as GPIO
import time


from io import BytesIO
import os


GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Button to GPIO23
GPIO.setup(24, GPIO.OUT)  # LED to GPIO24



try:
    
    while True:
        button_state = GPIO.input(23)
        if button_state == False:
            GPIO.output(24, True)
            print('Recording...')
            os.system('cd scripts')
            os.system('raspivid -o newvid.h264 -k -rf rgb -pf high -drc low -sa -50 -vs -br 40 -fps 30 -b 250000000')
        else:
            GPIO.output(24, False)
            
    while True:
        button_state = GPIO.input(18)
        if button_state == False:
            GPIO.output(17, True)
            print('Converting to MP4...')
            os.system('xdotool enter')
            os.system('MP4Box -add newvid.h264 newvid.mp4 -fps 32')
            os.system('omxplayer newvid.mp4')
            print('Finished')
        else:
             GPIO.output(17, True)

        
except:
    GPIO.cleanup()

