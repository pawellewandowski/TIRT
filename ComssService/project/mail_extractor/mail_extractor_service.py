#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ComssService.service.sync import SyncService
from ComssService.ServiceController import ServiceController
import re

class MailExtractorService(SyncService):

    def run(self):
        while True:
            data = self.read('1')
            print(data)


if __name__ == '__main__':
    # Uruchomienie usługi:
    desc_file_name = 'mail_extractor_service.xml'
    s = ServiceController(MailExtractorService, desc_file_name)
    s.start()

