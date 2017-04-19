#!/usr/bin/env python
# -*- coding: utf-8 -*-

import asyncore
from server import EchoServer
from serial_com import SerialNode
from settings import *


def main():
    tcp_server = EchoServer(HOST, PORT)
    serial_node = SerialNode(tcp_server)


if __name__ == "__main__":
    main()
