#!/usr/bin/env python

import os
import glob
import time
import re

# load the kernel modules needed to handle the sensor
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

# find the path of a sensor directory that starts with 28
devicelist = glob.glob('/sys/bus/w1/devices/28*')
deviceName = os.path.basename(devicelist[0]);

# append the device file name to get the absolute path of the sensor 
devicefile = devicelist[0] + '/w1_slave'

# open the file representing the sensor.
fileobj = open(devicefile,'r')
lines = fileobj.readlines()
fileobj.close()

# print the lines read from the sensor apart from the extra \n chars
#print lines[0][:-1]
#print lines[1][:-1]

crcokMatch = re.match( ".*(YES)\Z", lines[0][:-1] )
if crcokMatch is not None:
  if re.match(".*t=(\d+)\Z", lines[1][:-1] ) is not None:
    temp = re.sub(r".*t=(\d+)(\d\d\d)\Z",r"\1.\2",lines[1][:-1])

    print deviceName," ",temp
