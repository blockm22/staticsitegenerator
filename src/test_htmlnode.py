import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(props = {"href": "https://www.google.com", "target": "_blank"})
        expected =  ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected)

    def test_props_to_html2(self):
        node = HTMLNode(props = {})
        expected =  ""
        self.assertEqual(node.props_to_html(), expected)

    def test_props_to_html3(self):
        node = HTMLNode(props = {"href": "https://www.google.com"})
        expected =  ' href="https://www.google.com"'
        self.assertEqual(node.props_to_html(), expected)

if __name__ == "__main__":
    unittest.main()