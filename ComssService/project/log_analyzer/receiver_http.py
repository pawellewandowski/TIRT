#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ComssService.dev.control import DevServiceController
import sys

desc_file_name = 'log_analyzer_service.xml'
controller = DevServiceController(desc_file_name)
try:
    print("##### HTTP RECEIVER #####")
    while True:
        print controller.read_data('2')
except:
    raise
finally:
    controller.close_all_connections()