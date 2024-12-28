import unittest
from htmlnode import ParentNode,LeafNode

class TestParentNode(unittest.TestCase):
    def test_ParentNode(self):
        node = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
)
        expected =  '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>'
        self.assertEqual(node.to_html(), expected)

    def test_ParentNode2(self):
        node = ParentNode(
    "ul",
    [
        LeafNode("li", "First item"),
        LeafNode("li", "Second item")
    ]
)
 
        expected =  '<ul><li>First item</li><li>Second item</li></ul>'
        self.assertEqual(node.to_html(), expected)

    def test_ParentNode3(self):
        node = ParentNode("div", [])
        with self.assertRaises(ValueError) as context:
            node.to_html()
    
        self.assertEqual(str(context.exception), "ParentNode must have children")

    def test_ParentNode4(self):
        node = ParentNode(None, [LeafNode("p", "text")])
        with self.assertRaises(ValueError) as context:
            node.to_html()

        self.assertEqual(str(context.exception), "ParentNode must have a tag")

    def test_ParentNode5(self):
        node = ParentNode("div", [
            ParentNode("p", [
                LeafNode("b", "text")
            ])
        ]
)
        
        expected =  '<div><p><b>text</b></p></div>'
        self.assertEqual(node.to_html(), expected)

    def test_mixed_children(self):
        node = ParentNode("div", [
            LeafNode(None, "plain text"),
            LeafNode("b", "bold text"),
            ParentNode("p", [LeafNode("i", "italic")])
    ]
)
        
        expected =  '<div>plain text<b>bold text</b><p><i>italic</i></p></div>'
        self.assertEqual(node.to_html(), expected)

if __name__ == "__main__":
    unittest.main()