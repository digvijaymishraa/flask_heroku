#!/usr/bin/env python

"""Tests for the Flask Heroku template."""

import unittest
from app import app


class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_api_hello_world(self):
        rv = self.app.get('/api/hello_world')
        self.assertEqual(rv.data, b'Hello World')
        self.assertTrue(rv.status_code == 200)

    def test_api_hello_digvijay(self):
        rv = self.app.get('/api/hello_digvijay')
        self.assertEqual(rv.data, b'Hello World by digvijay')
        self.assertTrue(rv.status_code == 200)


if __name__ == '__main__':
    unittest.main()
