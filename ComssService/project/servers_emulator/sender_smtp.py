#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ComssService.dev.control import DevServiceController
import random
import time
desc_file_name = 'servers_emulator.xml'
controller = DevServiceController(desc_file_name)
try:
    print("##### Server SMTP Start #####")
    with open('data/smtp_server.log', 'rb') as file:
        for line in file.readlines():
            line= line.strip()
            controller.send_data('2', line)
            print "SENT:", line
            time.sleep(0.5)
except:
    raise
finally:
    controller.close_all_connections()
