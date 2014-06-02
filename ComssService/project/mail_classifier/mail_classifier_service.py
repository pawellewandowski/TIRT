#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ComssService.service.sync import SyncService
from ComssService.ServiceController import ServiceController
import mmap


class MultiplierService(SyncService):
    print("##### Mail classifier service #####")

    def run(self):
        while True:
            received_dict = self.read('1')
            status = '0'
            with open("data/blacklist.txt", "r") as f:
                searchlines = f.readlines()
                for i, line in enumerate(searchlines):
                    if str(received_dict) in line:
                        status = '1'

            self.send('2', status)


if __name__ == '__main__':
    desc_file_name = 'mail_classifier_service.xml'
    s = ServiceController(MultiplierService, desc_file_name)
    s.start()

