import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

    def test_basic_props(self):
        node = HTMLNode(tag='a', props={"href": "https://example.com"})
        self.assertEqual(node.props_to_html(), ' href="https://example.com"')
    
    def test_empty_props(self):
        node = HTMLNode(tag='p')
        self.assertEqual(node.props_to_html(), '')
    
    def test_multiple_props(self):
        node = HTMLNode(tag="img", props={"src": "image.jpg", "alt": "An image"})
        self.assertEqual(node.props_to_html(), ' src="image.jpg" alt="An image"')
        
    def test_children(self):
        child_node = HTMLNode(tag="span", value="Hello")
        parent_node = HTMLNode(tag="div", children=[child_node])
        self.assertEqual(parent_node.__repr__(), f'HTMLNode(div, None, children: [{child_node}], None)')
    
    def test_no_tag_or_value(self):
        node = HTMLNode()
        self.assertEqual(node.__repr__(), 'HTMLNode(None, None, children: None, None)')
        

if __name__ == "__main__":
    unittest.main()