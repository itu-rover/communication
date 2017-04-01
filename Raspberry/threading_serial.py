#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from glob import glob
import serial
import threading
import sys


ports = glob('/dev/ttyACM*')
serials = []
utilities = {}
utility_names = {"SC": "Sensor Controller", "BM": "Battery Management",
                "RA": "Robotic Arm", "MC": "Motor Controller",
                "LR": "LORA"}

def read_data(utility_name):
    while(1):
	try:
            utility = utilities[utility_name]
            if utility.inWaiting:
                utility.flush()
	        try:
                    data_array = utility.readline().split()
                    utility_data = str(data_array[0])
                    print utility_data
	        except Exception:
	            pass
	except:
	    sys.exit()
def write_data(utility_name,msg):
    while(1):
	try:
	    utility = utilities[utility_name]
	    utility.write(msg)
            time.sleep(.5)
	except:
	    sys.exit()


for port in ports:
    try:
        serials.append(serial.Serial(port, 115200))
        print(port)
    except (OSError, serial.SerialException):
        pass

print(ports)
print(serials)
serial_count = 0
num_serials = len(serials)

print('Sleeping for 1 second for initializing')
#utility.write('BiE')
time.sleep(1)

while serial_count != num_serials:
    serial_data = serials[serial_count].readline().split()
    print(serial_data)
    utility_name = str(serial_data[0])

    if utility_name in utility_names:
        print(utility_name + " Identified")
        print("Connected to " + utility_names[utility_name] + ", initializing")

        utility = serials[serial_count]
        time.sleep(.5)

        utility.flushInput()
        utility.flushOutput()
        utilities[utility_name] = utility

        serial_count +=1


try:
    for utility_name in utilities:
        try:
            reading_thread = threading.Thread(target=read_data, args=(utility_name,))
	    reading_thread.daemon = True
            reading_thread.start()
        except Exception:
            pass            
    for utility_name in utilities:
        try:
            msg = "BiE\n"
            writing_thread = threading.Thread(target=write_data, args=(utility_name,msg))	
	    writing_thread.daemon = True
            writing_thread.start()
        except Exception:
	    pass
    while(1): time.sleep(1)
except Exception:
    print("Exiting")
    sys.exit()
	
