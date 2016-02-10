#!/usr/bin/env python
import tornado.web

class BaseHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(str(dir(self)))

    def post(self):
        self.write(str(dir(self)))
