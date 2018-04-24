import os
import pivideo_class

import subprocess as subprocess
from subprocess import call
from screen import *
from gpiozero import Button
from signal import pause
import picamera
from datetime import datetime
import RPi.GPIO as GPIO

vid=pivideo_class.PiVideo() # create a pivideo object
pivideo_port=vid.open # open it on the default port
result=vid.lock # get the lock status


#initialize GPIO buttons
button1 = Button(23)
button2 = Button(18)

#initialize datetime object for file naming
now = datetime.now()
strVideo = str(now.month) + "-" + str(now.day) + "-" + str(now.year) + "_" + str(now.hour) + '.' + str(now.minute) + "." + str(now.second)

#initialize and set camera object
camera = picamera.PiCamera()
camera.resolution = camera.MAX_RESOLUTION
camera.resolution = (1920, 1080)
camera.contrast = 10
camera.saturation = -60
camera.awb_mode = "auto"

writeToScreen("Status:", "ready")
#Start recording to file
def record():
    try:
        pass
    except Exception as e:
        raise
    else:
        pass
    finally:
        pass
    writeToScreen("Status:", "recording")
    camera.start_recording("%s.h264" %strVideo,bitrate = 25000000, sei = True,quality = 23,intra_period = 8 )
   
#Ends recording process
def stopRecording():
    camera.stop_recording()
    writeToScreen("Status:", "stopped recording")
    time.sleep(1)
    #convert h264 file to mp4 file
    call(["MP4Box -add  " + strVideo + ".h264 " + strVideo + ".mp4 -fps 40"  ],shell=True)
    writeToScreen("Status:", "converting to MP4")
    time.sleep(5)
    #remove .h264
    os.system("rm "+strVideo + ".h264")
    os.system("sudo mv -f -t /media/pi/untitled/videos " +strVideo + ".mp4" )
    writeToScreen("Status:", "ready")


#Execute functions on button pressed
button1.when_pressed = record
button2.when_pressed = stopRecording
pause()

