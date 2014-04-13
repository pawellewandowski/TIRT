#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ComssService.dev.control import DevServiceController
import random
import time

desc_file_name = 'bayes_classifier_service.xml'
controller = DevServiceController(desc_file_name)

UPDATE_PARAMS_INTERVAL = 20

try:
    iters_to_update = UPDATE_PARAMS_INTERVAL
    while True:

        controller.send_object('1', 201)
        controller.send_object('2', 213123)
        print "SENT:"
        time.sleep(0.5)
except:
    raise
finally:
    controller.close_all_connections()
