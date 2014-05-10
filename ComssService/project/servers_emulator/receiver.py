#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ComssService.dev.control import DevServiceController
import sys

desc_file_name = 'servers_emulator.xml'
controller = DevServiceController(desc_file_name)
try:
    print("##### RECEIVER #####")
    while True:
        print controller.read_data('3')
except:
    raise
finally:
    controller.close_all_connections()