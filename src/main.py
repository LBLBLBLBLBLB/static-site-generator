from textnode import TextNode
from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
)
from inline_markdown import split_nodes_delimiter


def main():
    # node = TextNode("This is text with a `code block` word", 'text')
    # print(node)

    node = TextNode("**bold** and *italic*", text_type_text)
    new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
    new_nodes = split_nodes_delimiter(new_nodes, "*", text_type_italic)
    print(new_nodes)


main()