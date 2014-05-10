#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ComssService.service.sync import SyncService
from ComssService.ServiceController import ServiceController
import re

class ServersEmulatorService(SyncService):

    def run(self):
        print "##### ServersEmulatorService ####"
        while True:
            data = self.read('1')
            self.send('3', data)



if __name__ == '__main__':
    # Uruchomienie usługi:
    desc_file_name = 'servers_emulator.xml'
    s = ServiceController(ServersEmulatorService, desc_file_name)
    s.start()

