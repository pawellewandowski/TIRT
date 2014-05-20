#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ComssService.service.sync import SyncService
from ComssService.ServiceController import ServiceController
from numpy import matrix
from numpy.linalg import *


class MultiplierService(SyncService):
    def __init__(self, instance_id, inputs, outputs, exec_params, update_params_host, *args, **kwargs):
        SyncService.__init__(self, instance_id, inputs, outputs, exec_params, update_params_host, *args, **kwargs)
        self.mi = matrix([257.3289, 1891.4641, 257.3412, 1891.4578, 257.3534, 1891.0688]).transpose()
        self.cov = matrix([[2735.1732, -105164.6553, 1394.3363, -49252.3400, 1444.7696, -55889.5886],
                           [-105164.6553, 804017063.0871, -79963.4768, 9576227.3922, -76743.0733, 5355152.3607],
                           [1394.3363, -79963.4768, 2735.0429, -105187.3935, 1394.2058, -49253.1383],
                           [-49252.3400, 9576227.3922, -105187.3935, 804017086.7348, -79986.2150, 9576954.0862],
                           [1444.7696, -76743.0733, 1394.2058, -79986.2150, 2734.9122, -105188.1871],
                           [-55889.5886, 5355152.3607, -49253.1383, 9576954.0862, -105188.1871,
                            804017269.7513]]).transpose()
        self.queue = [0, 0, 0, 0, 0, 0]
        self.last_code = None
        self.last_content_length = None

    def run(self):
        print("##### Bayes Classifier Service #####")
        while True:  # będzie się wykonywać tak długo, jak będzie działać usługa
            if self.last_code is not None:
                self.last_code = self.read_object('1')  # odczytaj wejsciowy slownik
            if self.last_content_length is not None:
                self.last_content_length = self.read_object('2')  # odczytaj wejsciowy slownik
            if self.last_code is not None and self.last_content_length is not None:
                http_code = self.last_code
                http_content_length = self.last_content_length
                self.queue = self.queue[2:5] + [http_code, http_content_length]
                vect = matrix.matrix(self.queue).transpose()
                probability = (1 / (6.2831853071795862 ** 3 * det(self.cov) ** 0.5)) * exp(
                    -0.5 * (vect - self.mi).transpose() * inv(self.cov) * (vect - self.mi))
                #             print 'GOT:', received_dict
                #             curr_params = self.get_parameters()
                #             value_to_multiply = curr_params['value_to_multiply']
                #             if value_to_multiply in received_dict:
                #                 received_dict[value_to_multiply] *= curr_params['multiply_by']
                self.last_code = None
                self.last_content_length = None
                self.send_object('1', 1 - probability)  # na wyjście o id '2' wyślij przetworzony slownik


if __name__ == '__main__':
    # Uruchomienie usługi:
    desc_file_name = 'bayes_classifier_service.xml'
    s = ServiceController(MultiplierService, desc_file_name)
    s.start()

    # teraz wystarczy w kosoli uruchomić ten skrypt, aby usługa zaczęła działać
