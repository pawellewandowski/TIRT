#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ComssService.service.sync import SyncService
from ComssService.ServiceController import ServiceController
import re

# Regexp dla formatu Access Loga Apache'a
# Zgodny z Common Log Format (http://en.wikipedia.org/wiki/Common_Log_Format)
regex = '([(\d\.)]+) - - \[(.*?)\] "([A-Z]*?) (.*?) (.*?)" (\d+) (\d+|-) "(.*?)" "(.*?)"'

# Usługa ekstrakcji liczby przesłanych bajtów z pojedynczej linijki loga
class ByteExtractorService(SyncService):

    def run(self):
        print("##### Byte Extrator Service #####")
        while True:
            data = self.read('1')
            # Wyciąganie 6 grupy z regexpa - bajtów
            byte = re.match(regex, data).groups()[6]
            # bytes == "-" gdy odpowiedź np. typu "301"
            if byte == '-':
                byte='0'
            
            # Wysyłanie liczby bajtów na wyjście 2
            self.send('2', byte)

if __name__ == '__main__':
    # Uruchomienie usługi:
    desc_file_name = 'byte_extractor_service.xml'
    s = ServiceController(ByteExtractorService, desc_file_name)
    s.start()