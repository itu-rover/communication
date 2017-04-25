#!/usr/bin/env python
# -*- coding: utf-8 -*-

import asyncore
import logging
from server import EchoServer
from serial_com import SerialNode
from settings import *


def main():
    logging.basicConfig(filename='logs/com.log',
                        filemode='a',
                        format='%(asctime)s %(message)s',
                        level=logging.INFO)
    logging.info('Start main')
    tcp_server = EchoServer(HOST, PORT)
    serial_node = SerialNode(tcp_server)
    serial_node.run()
    logging.info('Finish')


if __name__ == "__main__":
    filename = ('logs/com.log')

    file = open(filename, "a")
    file.write('\n' + '*'*80 + '\n\n')
    file.close()

    main()
