#!/usr/bin/env python
import tornado.web

class SPAHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('index.html')

    def post(self):
        self.write(self.request.body)
