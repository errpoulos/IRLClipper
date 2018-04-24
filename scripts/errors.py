import pivideo_class
from screen import *

vid=pivideo_class.PiVideo() # create a pivideo object
pivideo_port=vid.open # open it on the default port
result=vid.lock # get the lock status

try: 
    if result !=0 : writeToScreen('Status:','ready')
    elif result == 0 : raise IOError
except IOError : writeToScreen('Error','No video input detected. Please connect HDMI or component source')

