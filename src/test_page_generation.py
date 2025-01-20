import unittest
from page_generation import *

class TestPageGeneration(unittest.TestCase):
    def test_eq(self):
        markdown = "# Markdown doc!!!"
        expected = "Markdown doc!!!"
        self.assertEqual(extract_title(markdown), expected)

    def test_eq2(self):
        markdown = "# Markdown doc!!!\nthen stome stuff\nthen some more stufffffff"
        expected = "Markdown doc!!!"
        self.assertEqual(extract_title(markdown), expected)