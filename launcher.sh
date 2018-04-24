#!/bin/sh
# launcher.sh
# navigate to home directory, then to this directory, then execute python script

sudo mount /dev/sda1 /media/pi/untitled
cd /
cd home/pi/IRLClipper/scripts
sudo python record.py
