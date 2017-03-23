#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from glob import glob
import serial


ports = glob('/dev/ttyUSB*')
serials = []
utilities = {}
utility_names = {"SC": "Sensor Controller", "BM": "Battery Management",
                 "RA": "Robotic Arm", "MC": "Motor Controller",
                 "LR": "LORA"}


def read_data(utility_name):
    utility = utilities[utility_name]
    if utility.inWaiting:
        utility.flush()
        data_array = utility.readline().split("\n")
        utility_data = str(data_array[0])

        print(utility_name + " says:" + utility_data)


for port in ports:
    try:
        serials.append(serial.Serial(port, 9600))
        print(port)
    except (OSError, serial.SerialException):
        pass


serial_count = 0
num_serials = len(serials)


print('Sleeping for 1 second for initializing')
time.sleep(1)


while serial_count != num_serials:
    serial_data = serials[serial_count].readline().split("\n")
    utility_name = str(serial_data[0])

    if utility_name in utility_names:
        print(utility_name + " Identified")
        print("Connected to " + utility_names[utility_name] + ", initializing")

        utility = serials[serial_count]
        utility.write('i')
        time.sleep(.5)

        utility.flushInput()
        utility.flushOutput()
        utilities[utility_name] = utility

        serial_count +=1


while True:
    for utility_name in utility_names:
        try:
            read_data(utility_name)
        except Exception:
            pass
