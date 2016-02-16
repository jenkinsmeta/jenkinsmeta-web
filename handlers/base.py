#!/usr/bin/env python
import tornado.web

class BaseHandler(tornado.web.RequestHandler):
    def get(self):
        content = {
                'message': 'Hello from Tornado!', 
                'jobs': [
                    {'name': 'Example1', 'url': 'http://some.jenkins/job/Example1'},
                    {'name': 'Example2', 'url': 'http://some.jenkins/job/Example2'},
                    {'name': 'Example3', 'url': 'http://some.jenkins/job/Example3'},
                    {'name': 'Example4', 'url': 'http://some.jenkins/job/Example4'},
                    {'name': 'Example5', 'url': 'http://some.jenkins/job/Example5'}
                ]
        }
        self.render("index.html", **content)

    def post(self):
        self.write(self.request.body)
