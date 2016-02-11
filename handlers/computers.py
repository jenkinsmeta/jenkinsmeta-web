#!/usr/bin/env python
import tornado.web
from jenkinsmeta_pb2 import computers_pb2

class ComputersHandler(tornado.web.RequestHandler):
    def get(self):
                
        return self.write('')
