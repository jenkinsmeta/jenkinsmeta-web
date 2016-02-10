#!/usr/bin/env python
import tornado.ioloop
import tornado.web
import settings
import urls

def create_app():
    return tornado.web.Application(urls.base_urls)

if __name__ == '__main__':
    app = create_app()
    app.listen(settings.PORT)
    tornado.ioloop.IOLoop.current().start()
