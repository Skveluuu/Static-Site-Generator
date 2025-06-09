import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        props1 = {
    "href": "https://www.google.com",
    "target": "_blank",
}
        testing_html_node = HTMLNode(props=props1)
        result = testing_html_node.props_to_html()
        self.assertIn('href="https://www.google.com"',result)
        self.assertIn('target="_blank"',result)
    
    def test_emptyprops(self):
        props2 = {}
        testing_html_node = HTMLNode(props=props2)
        result = testing_html_node.props_to_html()
        self.assertEqual(result,"")

    def test_emptyprops(self):
        props3 = None
        testing_html_node = HTMLNode(props=props3)
        result = testing_html_node.props_to_html()
        self.assertEqual(result,"")
        
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
