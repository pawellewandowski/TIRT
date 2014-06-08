#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ComssService.service.sync import SyncService
from ComssService.ServiceController import ServiceController
import re

# Funkcja analizuje wejście i rozdziela strumień danych na odpowiednie wyjścia

class LogAnalyzerService(SyncService):
    def run(self):
        print("##### Log Analyzer Service #####")
        while True:
            data = self.read('1')
            #print(data)
            http_server = re.search('HEAD|GET|POST',data) # Identyfikacja serwera http na podstawie regexu
            smtp_server = re.search('\[\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}]',data) # Identyfikacja serwera pocztowego na podstawie regexu
            if http_server:
                self.send('2', data) #127.0.0.1:5560 - http_extractor
                self.send('3', data) #127.0.0.1:5570 - byte_extractor
                self.send('4', data) #127.0.0.1:5580 - address_extractor
            else:
                self.send('5', data) #127.0.0.1:5590 - mail_extractor


if __name__ == '__main__':
    # Uruchomienie usługi:
    desc_file_name = 'log_analyzer_service.xml'
    s = ServiceController(LogAnalyzerService, desc_file_name)
    s.start()

