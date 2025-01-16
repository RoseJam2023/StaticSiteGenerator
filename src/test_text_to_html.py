import unittest
from text_to_html import text_node_to_html_node
from textnode import TextNode, TextType

class TestText_To_HTML(unittest.TestCase):
    def test_text_node_to_html_node_rawtext(self):
    # Arrange: Create a TextNode with known values
        text_node = TextNode("Hello", TextType.TEXT)
    
    # Act: Convert it to HTMLNode
        html_node = text_node_to_html_node(text_node)
    
    # Assert: Check if the conversion was correct
        assert html_node.tag == None
        assert html_node.value == "Hello"

        print(f"\nThis is the result of TestText_To_HTML conversion for raw text: [{repr(html_node)}]")
        print(f"This is the text_node that was used: [{repr(text_node)}]\n")
        print("----------------------------------------------------------")

    def test_text_node_to_html_node_bold(self):
    # Arrange: Create a TextNode with known values
        text_node = TextNode("Hello", TextType.BOLD)
    
    # Act: Convert it to HTMLNode
        html_node = text_node_to_html_node(text_node)
    
    # Assert: Check if the conversion was correct
        assert html_node.tag == "b"
        assert html_node.value == "Hello"

        print(f"\nThis is the result of TestText_To_HTML conversion for bold text: [{repr(html_node)}]")
        print(f"This is the text_node that was used: [{repr(text_node)}]\n")
        print("----------------------------------------------------------")

    def test_text_node_to_html_node_italic(self):
    # Arrange: Create a TextNode with known values
        text_node = TextNode("Hello", TextType.ITALIC)
    
    # Act: Convert it to HTMLNode
        html_node = text_node_to_html_node(text_node)
    
    # Assert: Check if the conversion was correct
        assert html_node.tag == "i"
        assert html_node.value == "Hello"

        print(f"\nThis is the result of TestText_To_HTML conversion for italics text: [{repr(html_node)}]")
        print(f"This is the text_node that was used: [{repr(text_node)}]\n")
        print("----------------------------------------------------------")

    def test_text_node_to_html_node_code(self):
    # Arrange: Create a TextNode with known values
        text_node = TextNode("Hello", TextType.CODE)
    
    # Act: Convert it to HTMLNode
        html_node = text_node_to_html_node(text_node)
    
    # Assert: Check if the conversion was correct
        assert html_node.tag == "code"
        assert html_node.value == "Hello"

        print(f"\nThis is the result of TestText_To_HTML conversion for code text: [{repr(html_node)}]")
        print(f"This is the text_node that was used: [{repr(text_node)}]\n")
        print("----------------------------------------------------------")

    def test_text_node_to_html_node_link(self):
    # Arrange: Create a TextNode with known values
        text_node = TextNode("Click me!", TextType.LINK, "www.test.com")
    
    # Act: Convert it to HTMLNode
        html_node = text_node_to_html_node(text_node)
    
    # Assert: Check if the conversion was correct
        assert html_node.tag == "a"
        assert html_node.value == "Click me!"
        assert html_node.props == {"href": "www.test.com"}

        print(f"\nThis is the result of TestText_To_HTML conversion for a link: [{repr(html_node)}]")
        print(f"This is the text_node that was used: [{repr(text_node)}]\n")
        print("----------------------------------------------------------")    
    
    def test_text_node_to_html_node_image(self):
    # Arrange: Create a TextNode with known values
        text_node = TextNode("Image description", TextType.IMAGE, "www.test.com")
    
    # Act: Convert it to HTMLNode
        html_node = text_node_to_html_node(text_node)
    
    # Assert: Check if the conversion was correct
        assert html_node.tag == "img"
        assert html_node.props == {"src": "www.test.com", "alt": "Image description"}

        print(f"\nThis is the result of TestText_To_HTML conversion for an image: [{repr(html_node)}]")
        print(f"This is the text_node that was used: [{repr(text_node)}]\n")
        print("----------------------------------------------------------")  

    def text_text_node_to_html_node_wildcardcase(self):
        with self.assertRaises(ValueError) as context:
            text_node = TextNode("This is a wildcard", TextType, "www.wildcard.com")

            html_node = text_node_to_html_node(text_node)

            print(repr(html_node))

        self.assertEqual(
            str(context.exception),
            "Unknown TextNode type"
    )