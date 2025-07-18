from textnode import *
from htmlnode import *

def main():
    text_node_test =TextNode("Test", TextType.LINK, "https://www.boot.dev")
    print(text_node_test)

    html_node_test = HTMLNode("<img>", props={"src":"img_girl.jpg", "alt":"Girl in a jacket", "width":"500", "height":"600"})
    print(html_node_test)

    node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    print(node.to_html())


main()
