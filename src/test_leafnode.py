import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("This is a paragraph of text.", "p")
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")
    
    def test_with_attributes(self):
        node = LeafNode("Click me!", "a", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')
    
    def test_without_tag(self):
        node = LeafNode("Raw text with no tag")
        self.assertEqual(node.to_html(), "Raw text with no tag")
    
    def test_nested_tags_in_value(self):
        node = LeafNode("<b>bold text</b>", "p")
        self.assertEqual(node.to_html(), "<p><b>bold text</b></p>")