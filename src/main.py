

from textnode import TextNode,TextType
from htmlnode import HTMLNode

def main():
    props1 = {
    "href": "https://www.google.com",
    "target": "_blank",
}
    print(HTMLNode(props=props1))


    
main()