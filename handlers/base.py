#!/usr/bin/env python
import tornado.web

class BaseHandler(tornado.web.RequestHandler):
    def get(self):
        content = {
                'message': 'Hello from Tornado!', 
        }
        self.render("base.html", **content)

    def post(self):
        self.write(self.request.body)
