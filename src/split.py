import re
import unittest

class TextType:
    TEXT = "text"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (
            isinstance(other, TextNode)
            and self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        )

    def __repr__(self):
        return f'TextNode("{self.text}", {self.text_type}, {self.url})'

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes


def split_nodes_link(old_nodes):
    """Splits text nodes into separate nodes for markdown links."""
    new_nodes = []
    pattern = r'\[([^\]]+)\]\((https?://[^\)]+)\)'

    for node in old_nodes:
        parts = re.split(pattern, node.text)
        i = 0
        while i < len(parts):
            if i + 2 < len(parts):  # Link found
                new_nodes.append(TextNode(parts[i], TextType.TEXT))
                new_nodes.append(TextNode(parts[i + 1], TextType.LINK, parts[i + 2]))
                i += 3
            else:  # Remaining text
                new_nodes.append(TextNode(parts[i], TextType.TEXT))
                i += 1

    return [node for node in new_nodes if node.text]  # Remove empty nodes

def split_nodes_image(old_nodes):
    """Splits text nodes into separate nodes for markdown images."""
    new_nodes = []
    pattern = r'!\[([^\]]+)\]\((https?://[^\)]+)\)'

    for node in old_nodes:
        parts = re.split(pattern, node.text)
        i = 0
        while i < len(parts):
            if i + 2 < len(parts):  # Image found
                new_nodes.append(TextNode(parts[i], TextType.TEXT))
                new_nodes.append(TextNode(parts[i + 1], TextType.IMAGE, parts[i + 2]))
                i += 3
            else:  # Remaining text
                new_nodes.append(TextNode(parts[i], TextType.TEXT))
                i += 1

    return [node for node in new_nodes if node.text]  # Remove empty nodes
