#!/usr/bin/env python
from endpoints import Endpoints
import tornado.web
import tornado.escape
import settings
import urlparse
import requests



def worker_request(endpoint):
    host = settings.WORKER.get('host')
    port = settings.WORKER.get('port')
    url = 'http://{host}:{port}/{endpoint}'.format(**locals())
    response = requests.get(url)
    return response


class SPAHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('index.html')

    def post(self):
        endpoints = Endpoints()
        payload = []
        try:
            handler = tornado.escape.json_decode(self.request.body)
        except:
            handler = {}
        endpoint = handler.get('endpoint')
        payload = endpoints.match(self, endpoint)
        self.write(tornado.escape.json_encode(payload))
