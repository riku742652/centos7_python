# -*- coding: utf-8 -*-
"""
    Flaskr Tests
    ~~~~~~~~~~~~
    Tests the Flaskr application.
    :copyright: (c) 2010 by Armin Ronacher.
    :license: BSD, see LICENSE for more details.
"""
import os
from app import app
import unittest
import tempfile
from flask_xmlrpcre.xmlrpcre import XMLRPCTester, Fault


class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        """Before each test, set up a blank database"""
        self.app = app.test_client()

    # testing functions

    def test_empty_db(self):
        """Start with a blank database"""
        rv = self.app.get('/')
        assert rv.json == {"statusCode": 200, "msg": "ok"}

    def test_xmlrpc(self):
        """Verify that the API methods work"""
        tester = XMLRPCTester(self.app, '/api')

        assert tester('new_post', 'API Post') == {"statusCode": 200, "msg": "API Post"}

if __name__ == '__main__':
    unittest.main()
