import unittest
import requests
import json

class AppTest(unittest.TestCase):

    def setUp(self):
        self.url = 'http://localhost:5000'

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

    def test_ip(self):
        response = requests.get(self.url + '/status')
        status_code = response.status_code
        content = response.content.decode('ascii')

        self.assertEqual(status_code,200)
        ip_regex = 'IP address of the server is ([0-9]{1,3}\.){3}[0-9]{1,3}.'
        self.assertRegex(content, ip_regex)
    
if __name__ == "__main__":
    unittest.main()
