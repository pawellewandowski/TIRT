#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ComssService.service.sync import SyncService
from ComssService.ServiceController import ServiceController


class MultiplierService(SyncService):

    def run(self):
		print("##### Decision Maker Service 1 #####")
		while True:  # będzie się wykonywać tak długo, jak będzie działać usługa
			#pobierz prawdopodobieństwo
			bayes = float(self.read('1'))/100
			print str(bayes)
			#sprawdzamy jaka jest szansa na anomalie
			if(bayes>0.5):
				pass
				#trzeba najpierw jakieś wyjście dopisać
				# self.send('2', "ANOMALY DETECTED!")

if __name__ == '__main__':
	# Uruchomienie usługi:
	desc_file_name = 'decision_maker_service1.xml'
	s = ServiceController(MultiplierService, desc_file_name)
	s.start()

    # teraz wystarczy w kosoli uruchomić ten skrypt, aby usługa zaczęła działać
