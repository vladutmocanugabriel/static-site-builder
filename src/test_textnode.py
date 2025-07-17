import unittest

from textnode import TextNode, TextType


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

if __name__ == "__main__":
    unittest.main()