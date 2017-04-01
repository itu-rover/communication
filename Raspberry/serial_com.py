#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from glob import glob
import serial
import threading
import sys

utility_names = {"SC": "Sensor Controller",
                 "BM": "Battery Management",
                 "RA": "Robotic Arm",
                 "MC": "Motor Controller",
                 "LR": "LORA"}


class SerialNode(object):
    def __init__(self):
        self.ports = glob('/dev/ttyACM*')
        self.serials = []
        self.utilities = {}
        self.msg = None
        self.add_serials()
        self.add_utilities()
        self.run()

    def read_data(utility_name):
        while True:
            utility = self.utilities[utility_name]
            if utility.inWaiting:
                utility.flush()
                try:
                    data_array = utility.readline().split()
                    self.data = str(data_array[0])
                except Exception:
                    pass

    def write_data(self, utility_name, msg_interval):
        while True:
            utility = self.utilities[utility_name]
            if self.mgs:
                utility.write(self.msg)
                time.sleep(msg_interval)

    def add_serials(self):
        for port in self.ports:
            try:
                self.serials.append(serial.Serial(port, 115200))
            except (OSError, serial.SerialException):
                pass

    def add_utilities(self):
        print("Initializating...")
        time.sleep(1)
        serial_no = 0
        num_serials = len(self.serials)

        while serial_count != num_serials:
            serial_data = self.serials[serial_no].readline.split()
            utility_name = str(serial_data[0])

            if utility_name in utility_names:
                print(utility_name + " Identified")
                print("Connected to " +
                      utility_names[utility_names] +
                      ", initializing")

                utility = self.serials[serial_no]
                time.sleep(.5)

                utility.flushInput()
                utility.flushOutput()
                self.utilities[utility_name] = utility

                serial_no += 1

        def run(self):
            try:
                for utility_name in self.utilities:
                    try:
                        reading_thread = threading.Thread(
                            target=read_data, args=(utility_name,))
                        reading_thread.daemon = True
                        reading_thread.start()
                    except Exception:
                        pass
                for utility_name in self.utilities:
                    try:
                        writing_thread = threading.Thread(
                                target=write_data,
                                args=(utility_name, WRITE_INTERVAL))
                        writing_thread.daemon = True
                        writing_thread.start()
                    except Exception:
                        pass
                while True:
                    time.sleep(1)
            except Exception:
                print("Exiting...")
                sys.exit()
