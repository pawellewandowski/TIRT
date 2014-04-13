#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ComssService.dev.control import DevServiceController
import fileinput

desc_file_name = 'injection_classifier_service.xml'
controller = DevServiceController(desc_file_name)

try:
    for line in fileinput.input(['address.txt']):
        controller.send_data('1', line)
        print line
except:
    raise
finally:
    controller.close_all_connections()