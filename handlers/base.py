#!/usr/bin/env python
import tornado.web
import tornado.escape

class SPAHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('index.html')

    def post(self):
        try:
            handler = tornado.escape.json_decode(self.request.body)
        except:
            handler = None
        payload = []
        content = handler.get('content')
        if content == 'jobs':
            #testing
            payload = [{
                'name': 'Another',
                'url': 'http://'
                },
                {
                'name': 'Second',
                'url': 'http://'
                }]
        self.write(tornado.escape.json_encode(payload))
