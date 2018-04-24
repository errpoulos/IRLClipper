import os
import subprocess
import threading
import time
from screen import *


RASPIVIDCMD = ["raspivid"]
TIMETOWAITFORABORT = 0.5

#class for controlling the running and shutting down of raspivid
class RaspiVidController(threading.Thread):
    def __init__(self, filePath, otherOptions=None):
        threading.Thread.__init__(self)
        
        #setup the raspivid cmd
        self.raspividcmd = RASPIVIDCMD

        #add file path, timeout and preview to options
        self.raspividcmd.append("-o")
        self.raspividcmd.append(filePath)
        

        #if there are other options, add them
        if otherOptions != None:
            self.raspividcmd = self.raspividcmd + otherOptions

        #set state to not running
        self.running = False
        
    def run(self):
        #run raspivid
        raspivid = subprocess.Popen(self.raspividcmd)
        
        #loop until its set to stopped or it stops
        self.running = True
        while(self.running and raspivid.poll() is None):
            time.sleep(TIMETOWAITFORABORT)
        self.running = False
        
        #kill raspivid if still running
        if raspivid.poll() == True: raspivid.kill()

    def stopController(self):
        self.running = False
