import unittest
import os
import bottle
from bottle.ext import werkzeug as bw

class WerkzeugTest(unittest.TestCase):
    def setUp(self):
        self.app = bottle.Bottle(catchall=False)
        self.plugin = self.app.install(bw.WerkzeugPlugin())

    def test_resquest_obj(self):
        request = self.plugin.request
        @self.app.get('/')
        def test():
            self.assertEqual(request.environ, bottle.request.environ)
            self.assertNotEqual(request, bottle.request)
            self.assertEqual(request.accept_languages.best, 'de')
            return repr(self.plugin.request)
        self.app({'PATH_INFO':'/', 'REQUEST_METHOD':'GET',
                  'HTTP_ACCEPT_LANGUAGE': 'de, en;q=0.7'}, lambda x, y: None)

    def test_response_obj(self):
        response_plugin = self.plugin.response
        response_source = bw.Response()
        @self.app.get('/')
        def test():
            self.assertTrue(hasattr(response_plugin, 'headers'))
            self.assertFalse(hasattr(response_plugin, 'header_list'))
            self.assertTrue(hasattr(response_source, 'headers'))
            self.assertFalse(hasattr(response_source, 'header_list'))
            return repr(self.plugin.response)
        self.app({'PATH_INFO':'/', 'REQUEST_METHOD':'GET',
                  'HTTP_ACCEPT_LANGUAGE': 'de, en;q=0.7'}, lambda x, y: None)



if __name__ == '__main__':
    unittest.main()
