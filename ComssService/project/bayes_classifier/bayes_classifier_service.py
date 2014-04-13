#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ComssService.service.sync import SyncService
from ComssService.ServiceController import ServiceController
from numpy import matrix
from numpy.linalg import *

class MultiplierService(SyncService):

    def __init__(self):
        self.mi = matrix.matrix([0, 0, 0, 0, 0, 0]).transpose()
        self.cov = matrix.matrix([[1, 0, 0, 0, 0, 0],
                                  [0, 1, 0, 0, 0, 0],
                                  [0, 0, 1, 0, 0, 0],
                                  [0, 0, 0, 1, 0, 0],
                                  [0, 0, 0, 0, 1, 0],
                                  [0, 0, 0, 0, 0, 1]])
        self.queue = [0, 0, 0, 0, 0, 0]

    def run(self):
        while True:  # będzie się wykonywać tak długo, jak będzie działać usługa
            if self.last_code is None:
                self.last_code = self.read_object('1')  # odczytaj wejsciowy slownik
            if self.last_content_length is None:
                self.last_content_length = self.read_object('2')  # odczytaj wejsciowy slownik
            if self.last_code is None or self.last_content_length is None:
                continue
            http_code = self.last_code
            http_content_length = self.last_content_length
            self.queue = [http_code, http_content_length] + self.queue[0:3]
            vect = matrix.matrix(self.queue).transpose()
            probability = (1/(6.2831853071795862**3 * det(self.cov)**0.5))*exp(-0.5*(vect-self.mi).transpose()*inv(self.cov)*(vect-self.mi))
#             print 'GOT:', received_dict
#             curr_params = self.get_parameters()
#             value_to_multiply = curr_params['value_to_multiply']
#             if value_to_multiply in received_dict:
#                 received_dict[value_to_multiply] *= curr_params['multiply_by']

            self.send_object('1', 1-probability)  # na wyjście o id '2' wyślij przetworzony slownik

if __name__ == '__main__':
    # Uruchomienie usługi:
    desc_file_name = 'bayes_classifier_service.xml'
    s = ServiceController(MultiplierService, desc_file_name)
    s.start()

    # teraz wystarczy w kosoli uruchomić ten skrypt, aby usługa zaczęła działać
