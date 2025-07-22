import re
from htmlnode import *
from textnode import *

def text_node_to_html_node(text_node):
        if text_node.text_type == TextType.TEXT:
            return LeafNode(None, text_node.text)
        elif text_node.text_type == TextType.BOLD_TEXT:
            return LeafNode("b", text_node.text)
        elif text_node.text_type == TextType.ITALIC_TEXT:
            return LeafNode("i", text_node.text)
        elif text_node.text_type == TextType.CODE_TEXT:
            return LeafNode("code", text_node.text)
        elif text_node.text_type == TextType.LINK:
            return LeafNode("a", text_node.text, {"href":text_node.url})
        elif text_node.text_type == TextType.IMAGE:
            return LeafNode("img", "", {"src":text_node.url, "alt":text_node.text})
        else:
            raise Exception("Incorrect Text Type")
        
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        split_nodes = []
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        elif node.text.count(delimiter) == 0:
            new_nodes.append(node)
        elif node.text.count(delimiter) != 2 and node.text.count(delimiter) != 0:
            print(node.text.count(delimiter))
            raise Exception("Missing closing delimiter")
        else:
            split = node.text.split(delimiter)
            split_nodes.append(TextNode(split[0], TextType.TEXT))
            split_nodes.append(TextNode(split[1], text_type))
            split_nodes.append(TextNode(split[2], TextType.TEXT))
            new_nodes.extend(split_nodes)
    return new_nodes


def extract_markdown_images(text):
    image_alts = re.findall(r"\[(.*?)\]" , text)
    image_links = re.findall(r"\((.*?)\)", text)
    extracted_images = []
    for alt,link in zip(image_alts,image_links):
        extracted_images.append((alt, link))
    return extracted_images

def extract_markdown_links(text):
    link_texts = re.findall(r"\[(.*?)\]" , text)
    link_hrefs = re.findall(r"\((.*?)\)", text)
    extracted_links = []
    for link_text,href in zip(link_texts,link_hrefs):
        extracted_links.append((link_text, href))
    return extracted_links


text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
print(extract_markdown_images(text))
link = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
print(extract_markdown_links(link))            