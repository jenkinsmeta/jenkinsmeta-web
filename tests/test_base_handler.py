#!/usr/bin/env python2
from tornado.testing import AsyncHTTPTestCase, gen_test
from app import create_app


class TestBaseHandler(AsyncHTTPTestCase):
    _ok_code = 200

    def get_app(self):
        return create_app()

    def test_base_handler(self):
        response = self.fetch('/')
        self.assertEqual(response.code, self._ok_code)
