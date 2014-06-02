#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ComssService.service.sync import SyncService
from ComssService.ServiceController import ServiceController
import re

regex = '([(\d\.)]+) - - \[(.*?)\] "([A-Z]*?) (.*?) (.*?)" (\d+) (\d+|-) "(.*?)" "(.*?)"'

class AddressExtractorService(SyncService):
    print("##### Adress Extractor Service #####")
    def run(self):
        while True:
            data = self.read('1')
            #print data
            byte = re.match(regex, data).groups()[3]
            self.send('2', byte)

if __name__ == '__main__':
    # Uruchomienie usługi:
    desc_file_name = 'address_extractor_service.xml'
    s = ServiceController(AddressExtractorService, desc_file_name)
    s.start()