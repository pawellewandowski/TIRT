#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ComssService.service.sync import SyncService
from ComssService.ServiceController import ServiceController
import re
import json    

json_data = open('default_filter.json')
filters = json.load(json_data)['filters']['filter']

class InjectionClassifierService(SyncService):
    print("##### Injection classifier service #####")
    def run(self):
        while True:
            data = self.read('1')
            status = '0'
            
            for line in filters:
                found = re.search(line['rule'], data)
                if found:
                    print data,line['description']
                    status = '1'
                    break
            
            self.send('2', status)
            
            
if __name__ == '__main__':
    # Uruchomienie usługi:
    desc_file_name = 'injection_classifier_service.xml'
    s = ServiceController(InjectionClassifierService, desc_file_name)
    s.start()