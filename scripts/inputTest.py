import pivideo_class
vid=pivideo_class.PiVideo() # create a pivideo object
pivideo_port=vid.open # open it on the default port
result=vid.lock # get the lock status
if (result > 0):
print(“Blue light on, video locked, camera mode = “,result)
else:
print(“Blue light off, no video detected by PiCapture”)

