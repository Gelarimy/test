import unittest
import requests


class FlaskTests(unittest.TestCase):
    def test_server(self):
        self.assertEqual(requests.get("http://localhost:8080/").status_code, 200)

    def test_contacts(self):
        self.assertEqual(requests.get("http://localhost:8080/contacts").status_code, 200)

    def test_news(self):
        self.assertEqual(requests.get("http://localhost:8080/news").status_code, 200)

    def test_documentation(self):
        self.assertEqual(requests.get("http://localhost:8080/documentation").status_code, 200)

    def test_norwayNo(self):
        self.assertEqual(requests.get("https://www.norway.no/ru/belarus/-/").status_code, 200)

if __name__ == '__main__':
    unittest.main()
