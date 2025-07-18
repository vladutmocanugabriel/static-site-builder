import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        html_node_test = HTMLNode("<a>", "Click Here", props={"href": "https://www.google.com", "target": "_blank"})

        self.assertEqual(html_node_test.props_to_html(), 'href="https://www.google.com" target="_blank"' )
    
    def test_empty_props(self):
        html_node_test = HTMLNode("<a>", "Click Here")
        self.assertEqual(html_node_test.props_to_html(), None )

    def test_props_to_html_tag(self):
        html_node_test = HTMLNode("<img>", props={"src":"img_girl.jpg", "alt":"Girl in a jacket", "width":"500", "height":"600"})
        self.assertEqual(html_node_test.props_to_html(), 'src="img_girl.jpg" alt="Girl in a jacket" width="500" height="600"' )

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

if __name__ == "__main__":
    unittest.main()