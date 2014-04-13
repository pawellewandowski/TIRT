#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ComssService.dev.control import DevServiceController
import sys

desc_file_name = 'log_analyzer_service.xml'
controller = DevServiceController(desc_file_name)
try:
    while True:
        sys.stdout.write(controller.read_data('2', 1024))
        sys.stdout.flush()
except:
    raise
finally:
    controller.close_all_connections()