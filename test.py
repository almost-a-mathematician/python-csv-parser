import unittest
from py2 import parse_URI


class GetDomainTestCase(unittest.TestCase):

    def test_get_domain(self):
        url = "https://www.example.com/page.html?param=value"
        expected_result = "www.example.com"
        result = parse_URI(url)
        self.assertEqual(expected_result, result)

        url = "https://sub.example.com/page.html?param=value"
        expected_result = "sub.example.com"
        result = parse_URI(url)
        self.assertEqual(expected_result, result)

        url = "https://www.example.com:8080/page.html?param=value"
        expected_result = "www.example.com:8080"
        result = parse_URI(url)
        self.assertEqual(expected_result, result)

        url = "https://www.example.com/"
        expected_result = "www.example.com"
        result = parse_URI(url)
        self.assertEqual(expected_result, result)

        url = "https://192.168.0.1/"
        expected_result = "192.168.0.1"
        result = parse_URI(url)
        self.assertEqual(expected_result, result)

if __name__ == '__main__':
    unittest.main()