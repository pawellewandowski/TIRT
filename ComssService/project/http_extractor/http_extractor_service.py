#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ComssService.service.sync import SyncService
from ComssService.ServiceController import ServiceController
import re

# Regexp dla formatu Access Loga Apache'a
# Zgodny z Common Log Format (http://en.wikipedia.org/wiki/Common_Log_Format)
regex = '([(\d\.)]+) - - \[(.*?)\] "([A-Z]*?) (.*?) (.*?)" (\d+) (\d+|-) "(.*?)" "(.*?)"'

# Usługa ekstrakcji kodu odpowiedzi HTTP z pojedynczej linijki loga
class HttpExtractorService(SyncService):
    print("##### Http Extrator Service #####")
    def run(self):
        while True:
            data = self.read('1')
            
            # Wyciąganie 5. grupy regexpa - kodu HTTP
            statusCode = re.match(regex, data).groups()[5]
            
            # Wysyłanie statusu HTTP na wyjście 2
            self.send('2', statusCode)

if __name__ == '__main__':
    # Uruchomienie usługi:
    desc_file_name = 'http_extractor_service.xml'
    s = ServiceController(HttpExtractorService, desc_file_name)
    s.start()