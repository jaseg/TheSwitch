#!/usr/bin/env python
import serial
import os

newpid = os.fork()
if newpid == 0:
	pidfile = open('/var/run/THE_SWITCH.pid', 'w')
	pidfile.write(str(newpid))
	pidfile.close()

	ser = serial.Serial("/dev/ttyACM0", 115200)
	while True:
		line = ser.readline()
		if "herpderp" in line:
			os.system("/home/jaseg/the-switch/motivate.sh&")
		if "kthxbye" in line:
			os.system("/home/jaseg/the-switch/demotivate.sh")
