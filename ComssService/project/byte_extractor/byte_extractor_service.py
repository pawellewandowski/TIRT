#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ComssService.service.sync import SyncService
from ComssService.ServiceController import ServiceController
import re

regex = '([(\d\.)]+) - - \[(.*?)\] "([A-Z]*?) (.*?) (.*?)" (\d+) (\d+|-) "(.*?)" "(.*?)"'

class ByteExtractorService(SyncService):

    def run(self):
        while True:
            data = self.read('1')
            byte = re.match(regex, data).groups()[6]
            # bytes == "-" when for e.g. 301
            if byte == '-':
                byte='0'

            self.send('2', byte)

if __name__ == '__main__':
    # Uruchomienie usługi:
    desc_file_name = 'byte_extractor_service.xml'
    s = ServiceController(ByteExtractorService, desc_file_name)
    s.start()