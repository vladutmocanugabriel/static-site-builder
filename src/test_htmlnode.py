import unittest

from htmlnode import *



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


    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_tag_error(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode(None, [child_node])
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_to_html_children_error(self):
        parent_node = ParentNode("div", None)
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        grandchild_node2 = LeafNode("b", "grandchild2")
        grandchild_node3 = LeafNode("b", "grandchild3")
        child_node = ParentNode("span", [grandchild_node, grandchild_node2])
        child_node2 = ParentNode("span", [grandchild_node3])
        parent_node = ParentNode("div", [child_node, child_node2])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b><b>grandchild2</b></span><span><b>grandchild3</b></span></div>",
        )

    def test_to_html_with_empty_children(self):
        parent_node = ParentNode("div", [ ])
        with self.assertRaises(ValueError):
            parent_node.to_html()

if __name__ == "__main__":
    unittest.main()