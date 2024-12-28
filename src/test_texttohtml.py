import unittest
from htmlnode import LeafNode
from textnode import TextType,TextNode,text_node_to_html_node

class Test_text_node_to_html_node(unittest.TestCase):
    def test_text_node_to_html_node(self):
        node = TextNode("Just plain text", TextType.NORMAL)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.value, "Just plain text")

    def test_text_node_to_html_node2(self):
        node = TextNode("Bold text", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), "<b>Bold text</b>")

