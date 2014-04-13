#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ComssService.dev.control import DevServiceController
import fileinput

desc_file_name = 'http_extractor_service.xml'
controller = DevServiceController(desc_file_name)

try:
    for line in fileinput.input(['../servers_emulator/data/http_server.log']):
        controller.send_data('1', line)
        print line
except:
    raise
finally:
    controller.close_all_connections()