#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ComssService.service.sync import SyncService
from ComssService.ServiceController import ServiceController


class MultiplierService(SyncService):

    def run(self):
        print("##### Decision Maker Service #####")
        while True:  # będzie się wykonywać tak długo, jak będzie działać usługa
            bayes = self.read('1')
            print bayes
            if bayes is not None:
                if(bayes>0.5):
                    self.send('1', "ANOMALY DETECTED!")
#             print 'GOT:', received_dict
#             curr_params = self.get_parameters()
#             value_to_multiply = curr_params['value_to_multiply']
#             if value_to_multiply in received_dict:
#                 received_dict[value_to_multiply] *= curr_params['multiply_by']

if __name__ == '__main__':
    # Uruchomienie usługi:
    desc_file_name = 'decision_maker_service1.xml'
    s = ServiceController(MultiplierService, desc_file_name)
    s.start()

    # teraz wystarczy w kosoli uruchomić ten skrypt, aby usługa zaczęła działać
