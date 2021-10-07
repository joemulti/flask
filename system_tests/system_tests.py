import unittest
import requests
import json
import re

class AppTest(unittest.TestCase):

    def setUp(self):
        self.url = 'http://localhost:8282'

    def test_welcome(self):
        response = requests.get(self.url)
        status_code = response.status_code
        content = response.content.decode('ascii')

        self.assertEqual(status_code,200)
        self.assertIn('Hallo', content)

    def test_addition(self):
        response = requests.get(self.url + '/add?zahleins=1&zahlzwei=2')
        status_code = response.status_code
        json_data = response.json()
        self.assertEqual(status_code,200)  
        self.assertIn('ergebnis', json_data)
    
    def test_nginx(self):
        response = requests.get(self.url)
        status_code = response.status_code
        headers = response.headers
        server_header = headers.get('Server')

        self.assertEqual(status_code, 200)
        self.assertIsNot(server_header, None)
        self.assertIn('nginx', server_header)

    def test_lb(self):
        response1 = requests.get(self.url + '/status')
        response2 = requests.get(self.url + '/status')

        content1 = response1.content.decode('ascii')
        content2 = response2.content.decode('ascii')

        ip_regex = '([0-9]{1,3}\.){3}[0-9]{1,3}.'

        ip_search1 = re.search(ip_regex, content1)
        ip_search2 = re.search(ip_regex, content2)

        self.assertIsNot(ip_search1, None)
        self.assertIsNot(ip_search2, None)
        self.assertNotEqual(ip_search1.group(), ip_search2.group())
    
if __name__ == "__main__":
    unittest.main()
