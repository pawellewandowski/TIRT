#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ComssService.dev.control import DevServiceController

desc_file_name = 'decision_maker_service.xml'

controller = DevServiceController(desc_file_name)
try:
    while True:
        print controller.read_data('4')
except:
    pass
finally:
    controller.close_all_connections()