import unittest
from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_LeafNode(self):
        node = LeafNode("p", "This is a paragraph of text.")
        expected =  '<p>This is a paragraph of text.</p>'
        self.assertEqual(node.to_html(), expected)
    def test_LeafNode2(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        expected =  '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(node.to_html(), expected)


if __name__ == "__main__":
    unittest.main()