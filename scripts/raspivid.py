import os
os.system('raspivid -o newvid.h264 -k -rf rgb -pf high -drc low -sa -50 -vs -br 40 -fps 30 -b 1200000000')
os.system('MP4Box -add newvid.h264 newvid.mp4 -fps 32')
os.system('omxplayer newvid.mp4')


