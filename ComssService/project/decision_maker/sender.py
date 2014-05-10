#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ComssService.dev.control import DevServiceController
import random
import time

desc_file_name = 'decision_maker_service.xml'
controller = DevServiceController(desc_file_name)

UPDATE_PARAMS_INTERVAL = 20

try:
    iters_to_update = UPDATE_PARAMS_INTERVAL
    while True:
        controller.send_data('2', '1')
        print '1'
        time.sleep(0.5)
except:
    raise
finally:
    controller.close_all_connections()
