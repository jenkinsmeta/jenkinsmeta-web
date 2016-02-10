#!/usr/bin/env python
from handlers.base import BaseHandler
from handlers.computers import ComputersHandler

base_urls = [
    (r"/", BaseHandler),
    (r"/computers", ComputersHandler),]
