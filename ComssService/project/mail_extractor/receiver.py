#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ComssService.dev.control import DevServiceController
import sys

desc_file_name = 'mail_extractor_service.xml'
controller = DevServiceController(desc_file_name)
try:
    while True:
        print controller.read_data('2')
except:
    raise
finally:
    controller.close_all_connections()