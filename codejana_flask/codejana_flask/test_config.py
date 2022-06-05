from codejana_flask import app
import unittest

class TestConfig(unittest.TestCase):
    # def test_config_loading(self):
    #     assert app.config['DEBUG'] is True
    #     assert app.config['SQLALCHEMY_DATABASE_URI']=='sqlite:///database/theDataBase.db'

    # check if response is 200 or 404
    # def test_index(self):
    #     tester = app.test_client(self)
    #     response = tester.get("/homepage")
    #     statuscode = response.status_code
    #     self.assertEqual(statuscode, 404)

    # check if content return is application/json
    # def test_index_content(self):
    #     tester = app.test_client(self)
    #     response = tester.get("/homepage")
    #     self.assertEqual(response.content_type, 'text/html')

    # check for Data returned
    def test_index_data(self):
        tester = app.test_client(self)
        response = tester.get("/homepage")
        self.assertTrue(b'Message' in response.data)

    

