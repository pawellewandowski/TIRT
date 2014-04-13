#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ComssService.dev.control import DevServiceController

desc_file_name = 'byte_extractor_service.xml'

controller = DevServiceController(desc_file_name)
try:
    while True:
        print controller.read_data('2')
except:
    pass
finally:
    controller.close_all_connections()
	