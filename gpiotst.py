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

writeToScreen(' ', ' ', ' ')
# #initialize GPIO buttons
# button1 = Button(23)
# button2 = Button(18)


# def printReadyMessage():
#     print('1')

# def printStopMessage():
#     print('2')

# # def printStopMessage():
# #     writeToScreen ('Status:', 'stopped','...' )
# # printReadyMessage()

# # testUSB()
# button1.when_pressed = printReadyMessage
# button2.when_pressed = printStopMessage
# pause()

