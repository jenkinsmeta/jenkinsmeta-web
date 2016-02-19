#!/usr/bin/env python
from jenkinsmeta_pb2.job_pb2 import Job

def jobs_handler(request, *args, **kwargs): 
    return [{'name': 'Testing', 'url': 'http://'}]

class Endpoints(object):
    endpoints = {}

    def register(self, name, callback):
        if name not in self.endpoints:
            self.endpoints[name] = callback
    
    def delete(self, name):
        if name in self.endpoints:
            del(self.endpoints[name])

    def match(self, parent, name):
        if name in self.endpoints:
            callback = self.endpoints.get(name)
            return callback(parent)

