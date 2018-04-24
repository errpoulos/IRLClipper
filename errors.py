import pivideo_class

vid=pivideo_class.PiVideo() # create a pivideo object
pivideo_port=vid.open # open it on the default port
result=vid.active_source # get the lock status
print(result)
