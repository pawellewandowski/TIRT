#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ComssService.service.sync import SyncService
from ComssService.ServiceController import ServiceController

class LowerService(SyncService):

    def run(self):
        while True:
            data = self.read('1')
            self.send('2', data.lower())

if __name__ == '__main__':
    # Uruchomienie usługi:
    desc_file_name = 'log_analyzer_service.xml'
    s = ServiceController(LowerService, desc_file_name)
    s.start()

