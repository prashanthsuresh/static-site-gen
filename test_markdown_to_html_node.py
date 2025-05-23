from markdown_to_html_node import *
import unittest

class TestMarkdownToHtmlNode(unittest.TestCase):
    def test_basic_paragraph(self):
        markdown = "Hello, world!"
        expected = HTMLNode("div", [HTMLNode("p", text_to_children("Hello, world!"))])
        self.assertEqual(markdown_to_html_node(markdown), expected)

    def test_multiple_paragraphs(self):
        markdown = "First paragraph.\n\nSecond paragraph."
        expected = HTMLNode("div", [
            HTMLNode("p", text_to_children("First paragraph.")),
            HTMLNode("p", text_to_children("Second paragraph."))
        ])
        self.assertEqual(markdown_to_html_node(markdown), expected)

    def test_code_block(self):
        markdown = "```\ncode example\n```"
        expected = HTMLNode("div", [HTMLNode("pre", [text_node_to_html_node("code example")])])
        self.assertEqual(markdown_to_html_node(markdown), expected)

    def test_heading(self):
        markdown = "# Heading"
        expected = HTMLNode("div", [HTMLNode("h1", text_to_children("Heading"))])
        self.assertEqual(markdown_to_html_node(markdown), expected)

    def test_mixed_content(self):
        markdown = "# Title\n\nParagraph text.\n\n```\ncode snippet\n```"
        expected = HTMLNode("div", [
            HTMLNode("h1", text_to_children("Title")),
            HTMLNode("p", text_to_children("Paragraph text.")),
            HTMLNode("pre", [text_node_to_html_node("code snippet")])
        ])
        self.assertEqual(markdown_to_html_node(markdown), expected)

if __name__ == "__main__":
    unittest.main()
