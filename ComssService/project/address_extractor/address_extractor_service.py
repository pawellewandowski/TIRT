#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ComssService.service.sync import SyncService
from ComssService.ServiceController import ServiceController
import re

# Regexp dla formatu Access Loga Apache'a
# Zgodny z Common Log Format (http://en.wikipedia.org/wiki/Common_Log_Format)
regex = '([(\d\.)]+) - - \[(.*?)\] "([A-Z]*?) (.*?) (.*?)" (\d+) (\d+|-) "(.*?)" "(.*?)"'

# Usługa ekstrakcji adresu żądania z pojedynczej linijki loga
class AddressExtractorService(SyncService):
    print("##### Adress Extractor Service #####")
    def run(self):
        while True:
            data = self.read('1')
            #print data
            
            # Wyciąganie adresu (path) żądania
            address = re.match(regex, data).groups()[3]
            
            # Wysyłanie na wyjście 2
            self.send('2', address)

if __name__ == '__main__':
    # Uruchomienie usługi:
    desc_file_name = 'address_extractor_service.xml'
    s = ServiceController(AddressExtractorService, desc_file_name)
    s.start()