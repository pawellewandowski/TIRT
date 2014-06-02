#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ComssService.service.sync import SyncService
from ComssService.ServiceController import ServiceController
from numpy import matrix
from numpy.linalg import *

class MultiplierService(SyncService):

    def run(self):
        while True:  # będzie się wykonywać tak długo, jak będzie działać usługa
            sqlinjection = self.read_object('1')

            if sqlinjection is not None:
                if(sqlinjection == 1):
                    self.send('1', "SQLINJECTION DETECTED!")
#             print 'GOT:', received_dict
#             curr_params = self.get_parameters()
#             value_to_multiply = curr_params['value_to_multiply']
#             if value_to_multiply in received_dict:
#                 received_dict[value_to_multiply] *= curr_params['multiply_by']

if __name__ == '__main__':
    # Uruchomienie usługi:
    desc_file_name = 'decision_maker_service2.xml'
    s = ServiceController(MultiplierService, desc_file_name)
    s.start()

    # teraz wystarczy w kosoli uruchomić ten skrypt, aby usługa zaczęła działać
