#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ComssService.dev.control import DevServiceController
import random
import time

chars_to_send = 'qwertyQWERTY'

desc_file_name = 'log_analyzer_service.xml'
controller = DevServiceController(desc_file_name)
try:
    with open('date/access.log', 'rb') as plik:
        for linia in plik.readlines():
            linia= linia.strip()
            controller.send_data('1', linia)
            print "SENT:", linia
            time.sleep(0.5)
except:
    raise
finally:
    controller.close_all_connections()
