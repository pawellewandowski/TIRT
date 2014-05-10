#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ComssService.service.sync import SyncService
from ComssService.ServiceController import ServiceController
import re

class MailExtractorService(SyncService):
    print("##### Mail Extractor Service #####")
    def run(self):
        while True:
            data = self.read('1')
            print(data)


if __name__ == '__main__':
    desc_file_name = 'mail_extractor_service.xml'
    s = ServiceController(MailExtractorService, desc_file_name)
    s.start()

