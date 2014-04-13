#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ComssService.service.sync import SyncService
from ComssService.ServiceController import ServiceController
import re

class LogAnalyzerService(SyncService):

    def run(self):
        while True:
            data = self.read('1')
            http_server = re.search('HEAD|GET|POST',data)
            smtp_server = re.search('\[\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}]',data)
            if http_server:
                self.send('2', data)
            else:
                if smtp_server:
                    self.send('3', data)
                else:
                    self.send('4', data)


if __name__ == '__main__':
    # Uruchomienie usługi:
    desc_file_name = 'log_analyzer_service.xml'
    s = ServiceController(LogAnalyzerService, desc_file_name)
    s.start()

