import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    # htmlnode tests
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',)
        
    def test_when_props_none(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            None
        )
        self.assertEqual(node.props_to_html(),
            "",)
        
    def test_multiple_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"src": "image.jpg", "alt": "An image"}
        )
        self.assertEqual(node.props_to_html(),
            ' src="image.jpg" alt="An image"',)

    # leafnode test
    def test_to_html_wth_props(self):
        node = LeafNode("p",'Hello',  {"src": "image.jpg", "alt": "An image"})
        self.assertEqual(node.to_html(), '<p src="image.jpg" alt="An image">Hello</p>')
    
    def test_to_html_no_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    # parentnode test
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )


if __name__ == "__main__":
    unittest.main()