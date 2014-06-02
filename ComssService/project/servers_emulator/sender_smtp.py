#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ComssService.dev.control import DevServiceController
import time
import re

desc_file_name = 'servers_emulator.xml'
controller = DevServiceController(desc_file_name)
try:
    print("##### Server SMTP Start #####")

    with open('data/smtp_server.log', 'rb') as file:
        block = ''
        for line in file.readlines():
            line = line.strip()
            block_end = re.search('[-]*=_[0-9]*-[0-9]*-[0-9]*', line)
            block += line
            if block_end:
                controller.send_data('2', block)
                print "SENT:", block
                time.sleep(1)
except:
    raise
finally:
    controller.close_all_connections()
