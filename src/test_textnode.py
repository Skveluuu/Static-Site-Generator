import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_differntURLs(self):
        node3 = TextNode("This is a text node", TextType.BOLD,url="www.surya.com")
        node4 = TextNode("This is a text node", TextType.BOLD,url="www.surya2.com")
        self.assertNotEqual(node3,node4)
    
    def test_differntTextTypes(self):
        node5 = TextNode("This is a text node", TextType.BOLD,url="www.surya2.com")
        node6 = TextNode("This is a text node", TextType.NORMAL,url="www.surya2.com")
        self.assertNotEqual(node5,node6)


if __name__ == "__main__":
    unittest.main()