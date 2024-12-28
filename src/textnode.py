from htmlnode import LeafNode
from enum import Enum

class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC  = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(textnode1, textnode2):
        return textnode1.text == textnode2.text and \
               textnode1.text_type == textnode2.text_type and \
               textnode1.url == textnode2.url
            
    def __repr__(textnode):
        return "TextNode(" + str(textnode.text) + ", " + textnode.text_type.value + ", " + str(textnode.url) + ")"    

def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.NORMAL:
        return LeafNode(None,text_node.text)
    if text_node.text_type == TextType.BOLD:
        return LeafNode("b",text_node.text)
    if text_node.text_type == TextType.ITALIC:
        return LeafNode("i",text_node.text)
    if text_node.text_type == TextType.CODE:
        return LeafNode("code",text_node.text)
    if text_node.text_type == TextType.LINK:
        return LeafNode("a",text_node.text,{"href": text_node.url})
    if text_node.text_type == TextType.IMAGE:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    raise Exception("Unidentified text type")