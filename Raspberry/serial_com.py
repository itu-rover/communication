#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import asyncore
from glob import glob
import serial
import threading
import sys
from settings import *


utility_names = {"SC": "Sensor Controller",
                 "BM": "Battery Management",
                 "RA": "Robotic Arm",
                 "MC": "Motor Controller",
                 "LR": "LORA"}


class SerialNode(object):
    def __init__(self, server):
        self.ports = glob('/dev/ttyACM*')
        self.server = server
        self.serials = []
        self.utilities = {}
        self.msg = None
        self.msg_interval = WRITE_INTERVAL
        self.add_serials()
        self.add_utilities()
        self.run()

    def read_data(self, utility_name):
        print("*** reading...")
        while True:
            utility = self.utilities[utility_name]
            if utility.inWaiting:
                utility.flush()
                try:
                    data_array = utility.readline().split()
                    try:
                        serial_data = " ".join(data_array) + "\n"
                        self.server.handler.serial_data = serial_data
                    except Exception:
                        print("No connection detected!")
                        time.sleep(3)
                except Exception:
                    pass

    def write_data(self, utility_name):
        print("*** writing...")
        while True:
            utility = self.utilities[utility_name]
            try:
                self.msg = self.server.handler.data
            except:
                self.msg = None
            if self.msg:
                print("writing...")
                print self.msg
                utility.write(self.msg)
                time.sleep(self.msg_interval)

    def add_serials(self):
        print("*** Adding serials...")
        for port in self.ports:
            try:
                self.serials.append(serial.Serial(port, 115200))
            except Exception as e:
                print e

    def add_utilities(self):
        print("*** Initializating...")
        time.sleep(1)
        serial_no = 0
        num_serials = len(self.serials)

        while serial_no != num_serials:
            serial_data = self.serials[serial_no].readline().split("\r\n")
            serial_data = serial_data[0].split(',')
            utility_name = str(serial_data[0])

            if utility_name in utility_names:
                print(utility_name + " Identified")
                print("Connected to " +
                      utility_names[utility_name] +
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
                        target=self.read_data, args=(utility_name, ))
                    reading_thread.daemon = True
                    reading_thread.start()
                except Exception as e:
                    print e

            for utility_name in self.utilities:
                try:
                    writing_thread = threading.Thread(
                        target=self.write_data,
                        args=(utility_name, ))
                    writing_thread.daemon = True
                    writing_thread.start()
                except Exception as e:
                    print e

            try:
                server_thread = threading.Thread(
                    target=asyncore.loop,
                    args=())
                server_thread.daemon = True
                server_thread.start()
            except Exception as e:
                print e

            while True:
                time.sleep(1)
        except Exception:
            print("Exiting...")
            sys.exit()
