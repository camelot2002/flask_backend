import unittest
from flask import Flask
from app import receive_query

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_receive_query_valid_query1(self):
        response = self.client.post('/query', data={'query': 'query1'})
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertIn('triples', data)

    def test_receive_query_valid_query2(self):
        response = self.client.post('/query', data={'query': 'query2'})
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertIn('triples', data)

    def test_receive_query_valid_query3(self):
        response = self.client.post('/query', data={'query': 'query3'})
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertIn('triples', data)

    def test_receive_query_valid_query4(self):
        response = self.client.post('/query', data={'query': 'query4'})
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertIn('triples', data)

    def test_receive_query_invalid_query(self):
        response = self.client.post('/query', data={'query': 'invalid_query'})
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertIn('error', data)

if __name__ == '__main__':
    unittest.main()