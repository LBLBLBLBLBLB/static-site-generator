from textnode import TextNode
from htmlnode import HTMLNode
from leafnode import LeafNode

text_node_obj = ('This is a text node', 'bold',' https://www.boot.dev')
# print(text_node_obj)



leafobj2 = LeafNode(None, 'a', {'fdsa: fad'})


print(leafobj2.to_html())   # Expected: <a href="https://www.google.com">Click me!</a>
