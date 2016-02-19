#!/usr/bin/env python
from tornado.log import enable_pretty_logging
from endpoints import Endpoints, jobs_handler
import tornado.ioloop
import tornado.web
import settings
import logging
import urls

enable_pretty_logging()
endpoints = Endpoints()

endpoints.register('jobs', jobs_handler) 

def create_app():
    return tornado.web.Application(urls.base_urls, **settings.APP)

if __name__ == '__main__':
    app = create_app()
    app.listen(settings.PORT)
    tornado.ioloop.IOLoop.current().start()
