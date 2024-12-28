import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq2(self):
        node = TextNode("This is another text node", TextType.ITALIC)
        node2 = TextNode("This is another text node", TextType.ITALIC)
        self.assertEqual(node, node2)

    def test_eq3(self):
        node = TextNode("This is another text node", TextType.ITALIC,"www.clownpenis.fart")
        node2 = TextNode("This is another text node", TextType.ITALIC,"www.clownpenis.fart")
        self.assertEqual(node, node2)

    def test_eq4(self):
        node = TextNode("This is another text node", TextType.BOLD,"www.clownpenis.fart")
        node2 = TextNode("This is another text node", TextType.ITALIC,"www.clownpenis.fart")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()