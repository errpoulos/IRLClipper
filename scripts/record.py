import os
import picamera

camera = picamera.PiCamera()
camera.resolution = (1920, 1080)
camera.framerate = 30
camera.start_recording('new.h264')
camera.wait_recording(10)
camera.stop_recording()

os.system("MP4Box -fps 60 -s component -add new.h264 vid.mp4")