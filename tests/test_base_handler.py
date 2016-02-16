#!/usr/bin/env python2
from tornado.testing import AsyncHTTPTestCase, gen_test
from app import create_app


class TestBaseHandler(AsyncHTTPTestCase):
    _ok_code = 200

    def get_app(self):
        return create_app()

    def test_base_handler_get(self):
        response = self.fetch('/', method="GET")
        self.assertEqual(response.code, self._ok_code)

    def test_base_handler_post(self):
        body = "THIS IS JUST A TEST"
        response = self.fetch('/', method="POST", body=body)
        self.assertEqual(response.code, self._ok_code)
