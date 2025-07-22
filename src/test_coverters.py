import unittest

from htmlnode import *
from textnode import *
from converters import *


class TestTextNode(unittest.TestCase):
    def test_split_nodes_delimiter_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE_TEXT)

        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE_TEXT),
            TextNode(" word", TextType.TEXT),
            ])
        
    def test_split_nodes_delimiter_bold(self):
        node = TextNode("This is text with a **bold block** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)

        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bold block", TextType.BOLD_TEXT),
            TextNode(" word", TextType.TEXT),
            ])
        
    def test_split_nodes_delimiter_italic(self):
        node = TextNode("This is text with a _italic block_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC_TEXT)

        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("italic block", TextType.ITALIC_TEXT),
            TextNode(" word", TextType.TEXT),
            ])
        
    def test_split_nodes_delimiter_error(self):
        node = TextNode("This is text with a _italic block word", TextType.TEXT)

        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "_", TextType.ITALIC_TEXT)

    def test_split_nodes_delimiter_multiple_nodes(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        node2 = TextNode("This is text with a **code block** word", TextType.BOLD_TEXT)
        node3 = TextNode("This is another text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node, node2, node3], "`", TextType.CODE_TEXT)

        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.TEXT, None),
            TextNode("code block", TextType.CODE_TEXT, None),
            TextNode(" word", TextType.TEXT, None),
            TextNode("This is text with a **code block** word", TextType.BOLD_TEXT, None),
            TextNode("This is another text with a ", TextType.TEXT, None),
            TextNode("code block", TextType.CODE_TEXT, None),
            TextNode(" word", TextType.TEXT, None)
        ])

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        )
        self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)

    

if __name__ == "__main__":
    unittest.main()