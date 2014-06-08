#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ComssService.service.sync import SyncService
from ComssService.ServiceController import ServiceController
import re

#Usługa ekstrachująca domene z adresy mailwoego

class MailExtractorService(SyncService):
    print("##### Mail Extractor Service #####")
    def run(self):
        while True:
            data = self.read('1')
            if data is not None:
                email = re.search("([a-zA-Z][\w\.-]*[a-zA-Z0-9])@([a-zA-Z0-9][\w\.-]*[a-zA-Z0-9]\.[a-zA-Z][a-zA-Z\.]*[a-zA-Z])", data) # Regex do ekstrakcji adresu email
                if email is not None:
                    domain=email.group(2) #ekstrakcja domeny
                    if domain:
                        print(domain)
                        self.send('2', domain)


if __name__ == '__main__':
    desc_file_name = 'mail_extractor_service.xml'
    s = ServiceController(MailExtractorService, desc_file_name)
    s.start()

