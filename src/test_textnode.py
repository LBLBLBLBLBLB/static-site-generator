import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
        
    def test_eq_with_same_url(self):
        node1 = TextNode("This is a text node", "bold")
        node1.url = "http://example.com"
        node2 = TextNode("This is a text node", "bold")
        node2.url = "http://example.com"
        self.assertEqual(node1, node2)
    
    def test_neq_different_text(self):
        node1 = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a different text node", "bold")
        self.assertNotEqual(node1, node2)
    
    def test_neq_different_text_type(self):
        node1 = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italic")
        self.assertNotEqual(node1, node2)
    
    def test_neq_url_none(self):
        node1 = TextNode("This is a text node", "bold")
        node1.url = None
        node2 = TextNode("This is a text node", "bold")
        node2.url = "http://example.com"
        self.assertNotEqual(node1, node2)
 


if __name__ == "__main__":
    unittest.main()