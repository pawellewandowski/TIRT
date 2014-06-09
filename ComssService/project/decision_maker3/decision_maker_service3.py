#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ComssService.service.sync import SyncService
from ComssService.ServiceController import ServiceController
from numpy import matrix
from numpy.linalg import *

class MultiplierService(SyncService):

    def run(self):
		print("##### Decision Maker Service 3 #####")
		while True:
			#pobierz odczyt spamu
			spam = self.read('1')
			print spam
			#jeśli wystąpił spam, powiadom dalej
			if(spam == 1):
				self.send('2', "SPAM DETECTED!")

if __name__ == '__main__':
    # Uruchomienie usługi:
    desc_file_name = 'decision_maker_service3.xml'
    s = ServiceController(MultiplierService, desc_file_name)
    s.start()

    # teraz wystarczy w kosoli uruchomić ten skrypt, aby usługa zaczęła działać
