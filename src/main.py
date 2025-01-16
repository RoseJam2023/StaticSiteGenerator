from textnode import *
from htmlnode import *
from text_to_html import text_node_to_html_node

def main():
    test_enum = TextType.TEXT
    test_node = TextNode("This is a text node", test_enum, "https://www.boot.dev")

    print(f"This is the current test text node: [{repr(test_node)}]")
    print(f"This is the conversion of that text node to an html node: [{text_node_to_html_node(test_node)}]")
    



if __name__ == "__main__":
    main()