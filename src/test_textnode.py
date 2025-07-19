import unittest

from textnode import *
from main import text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)

        self.assertEqual(node,node2)

    def test_repr_function(self):
        text_node_test =TextNode("Test", TextType.LINK, "https://www.boot.dev")
        self.assertEqual(text_node_test.__repr__(), "TextNode(Test, [anchor text](url), https://www.boot.dev)" )

    def test_eq_function_true(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        
        self.assertEqual(node.__eq__(node2), True)

    def test_eq_function_false(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.ITALIC_TEXT)

        self.assertEqual(node.__eq__(node2), False)

    def test_url_default(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node.url, None)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        print(html_node.to_html())
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        html_node = text_node_to_html_node(node)
        print(html_node.to_html())
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a text node")

    def test_italic(self):
        node = TextNode("This is a text node", TextType.ITALIC_TEXT)
        html_node = text_node_to_html_node(node)
        print(html_node.to_html())
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is a text node")

    def test_code(self):
        node = TextNode("print(test)", TextType.CODE_TEXT)
        html_node = text_node_to_html_node(node)
        print(html_node.to_html())
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "print(test)")

    def test_link(self):
        node = TextNode("CLICK HERE", TextType.LINK, url="https://test.url.com")
        html_node = text_node_to_html_node(node)
        print(html_node.to_html())
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "CLICK HERE")

    def test_image(self):
        node = TextNode("", TextType.IMAGE, url="https://test.image.com")
        html_node = text_node_to_html_node(node)
        print(html_node.to_html())
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")

    def test_text_node_to_html_node_error(self):
        node = TextNode("This is a text node", "TextType.ERROR")
        with self.assertRaises(Exception):
            text_node_to_html_node(node)

if __name__ == "__main__":
    unittest.main()