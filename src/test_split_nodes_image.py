import unittest
from textnode import TextNode, TextType
from split_nodes_image import *

class TestSplit_Nodes_Image(unittest.TestCase):
    def test_split_nodes_image(self):
        test_node = TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and nothing else.", TextType.TEXT)
        test_nodes = [test_node]

        result = split_nodes_image(test_nodes)

        assert len(result) == 3, f"The resulting list should have 3 nodes, but instead split into {len(result)}"

        assert result[0].text == "This is text with a ", f"The text for result[0] should have been 'This is text with a ', but instead reads {result[0]}"
        assert result[0].text_type == TextType.TEXT, f"The TextType for result[0] should have been TextType.TEXT, but was instead {result[0].text_type}"

        assert result[1].text == "rick roll", f"The text for result[1] should have been 'rick roll', but instead reads {result[1].text}"
        assert result[1].text_type == TextType.IMAGE, f"The TextType for result[1] should have been TextType.IMAGE, but was instead {result[1].text_type}"
        assert result[1].url == "https://i.imgur.com/aKaOqIh.gif", f"The URL for result[1] should have been 'https://i.imgur.com/aKaOqIh.gif', but was instead {result[1].url}"

        assert result[2].text == " and nothing else.", f"The text for result[2] should have been ' and nothing else.', but instead reads {result[2].text}"
        assert result[2].text_type == TextType.TEXT, f"The TextType for result[2] should have been TextType.TEXT, but was instead {result[2].text_type}"

        print(f"\nThis is the result of TestSplit_Nodes_Image: {result}\n")
        print(f"\nThis is the test_node that was used: [{repr(test_node)}]\n")
        print(f"\nThis was the test_nodes list used: [{test_nodes}]")
        print("----------------------------------------------------------")

    def test_split_nodes_image_multiple_images(self):
        test_node = TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and an additional ![image](www.imgur.com) as well.", TextType.TEXT)
        test_nodes = [test_node]

        result = split_nodes_image(test_nodes)

        assert len(result) == 5, f"The resulting list should have 5 nodes, but instead split into {len(result)}"

        assert result[0].text == "This is text with a ", f"The text for result[0] should have been 'This is text with a ', but instead reads {result[0]}"
        assert result[0].text_type == TextType.TEXT, f"The TextType for result[0] should have been TextType.TEXT, but was instead {result[0].text_type}"

        assert result[1].text == "rick roll", f"The text for result[1] should have been 'rick roll', but instead reads {result[1].text}"
        assert result[1].text_type == TextType.IMAGE, f"The TextType for result[1] should have been TextType.IMAGE, but was instead {result[1].text_type}"
        assert result[1].url == "https://i.imgur.com/aKaOqIh.gif", f"The URL for result[1] should have been 'https://i.imgur.com/aKaOqIh.gif', but was instead {result[1].url}"

        assert result[2].text == " and an additional ", f"The text for result[2] should have been ' and an additional ', but instead reads {result[2].text}"
        assert result[2].text_type == TextType.TEXT, f"The TextType for result[2] should have been TextType.TEXT, but was instead {result[2].text_type}"

        assert result[3].text == "image", f"The text for result[3] should have been 'image', but instead reads {result[3].text}"
        assert result[3].text_type == TextType.IMAGE, f"The TextType for result[3] should have been TextType.IMAGE, but was instead {result[3].text_type}"
        assert result[3].url == "www.imgur.com", f"The URL for result[3] should have been 'www.imgur.com', but was instead {result[3].url}"

        assert result[4].text == " as well.", f"The text for result[4] should have been ' as well.', but instead reads {result[4].text}"
        assert result[4].text_type == TextType.TEXT, f"The TextType for result[4] should have been TextType.TEXT, but was instead {result[4].text_type}"


        print(f"\nThis is the result of TestSplit_Nodes_Image_Multiple_Images: {result}\n")
        print(f"\nThis is the test_node that was used: [{repr(test_node)}]\n")
        print(f"\nThis was the test_nodes list used: [{test_nodes}]")
        print("----------------------------------------------------------")

    def test_split_nodes_image_mixednodes(self):
        test_node1 = TextNode("This is text without an image present", TextType.TEXT)
        test_node2 = TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and nothing else.", TextType.TEXT)
        test_node3 = TextNode("This is text with a ![different rick roll](http://rick.roll.com) and an additional ![image](www.imgur.com) as well.", TextType.TEXT)

        test_nodes = [test_node1, test_node2, test_node3]

        result = split_nodes_image(test_nodes)

        assert len(result) == 9, f"The resulting list should have 9 nodes, but instead split into {len(result)}"

        assert result[0].text == "This is text without an image present", f"The text for result[0] should have been 'This is text without an image present', but instead reads {result[0]}"
        assert result[0].text_type == TextType.TEXT, f"The TextType for result[0] should have been TextType.TEXT, but was instead {result[0].text_type}"

        assert result[1].text == "This is text with a ", f"The text for result[1] should have been 'This is text with a ', but instead reads {result[1]}"
        assert result[1].text_type == TextType.TEXT, f"The TextType for result[1] should have been TextType.TEXT, but was instead {result[1].text_type}"

        assert result[2].text == "rick roll", f"The text for result[2] should have been 'rick roll', but instead reads {result[2].text}"
        assert result[2].text_type == TextType.IMAGE, f"The TextType for result[2] should have been TextType.IMAGE, but was instead {result[2].text_type}"
        assert result[2].url == "https://i.imgur.com/aKaOqIh.gif", f"The URL for result[2] should have been 'https://i.imgur.com/aKaOqIh.gif', but was instead {result[2].url}"

        assert result[3].text == " and nothing else.", f"The text for result[3] should have been ' and nothing else.', but instead reads {result[3].text}"
        assert result[3].text_type == TextType.TEXT, f"The TextType for result[3] should have been TextType.TEXT, but was instead {result[3].text_type}"

        assert result[4].text == "This is text with a ", f"The text for result[4] should have been 'This is text with a ', but instead reads {result[4]}"
        assert result[4].text_type == TextType.TEXT, f"The TextType for result[4] should have been TextType.TEXT, but was instead {result[4].text_type}"

        assert result[5].text == "different rick roll", f"The text for result[5] should have been 'different rick roll', but instead reads {result[5].text}"
        assert result[5].text_type == TextType.IMAGE, f"The TextType for result[5] should have been TextType.IMAGE, but was instead {result[5].text_type}"
        assert result[5].url == "http://rick.roll.com", f"The URL for result[5] should have been 'http://rick.roll.com', but was instead {result[5].url}"

        assert result[6].text == " and an additional ", f"The text for result[6] should have been ' and an additional ', but instead reads {result[6].text}"
        assert result[6].text_type == TextType.TEXT, f"The TextType for result[6] should have been TextType.TEXT, but was instead {result[6].text_type}"

        assert result[7].text == "image", f"The text for result[7] should have been 'image', but instead reads {result[7].text}"
        assert result[7].text_type == TextType.IMAGE, f"The TextType for result[7] should have been TextType.IMAGE, but was instead {result[7].text_type}"
        assert result[7].url == "www.imgur.com", f"The URL for result[7] should have been 'www.imgur.com', but was instead {result[7].url}"

        assert result[8].text == " as well.", f"The text for result[8] should have been ' as well.', but instead reads {result[8].text}"
        assert result[8].text_type == TextType.TEXT, f"The TextType for result[8] should have been TextType.TEXT, but was instead {result[8].text_type}"

        print(f"\nThis is the result of TestSplit_Nodes_Image_Mixednodes: {result}\n")
        print(f"\nThis was the test_nodes list used: [{test_nodes}]")
        print("----------------------------------------------------------")


    def test_split_nodes_image_noimage(self):
        test_node = TextNode("This is text without an image present", TextType.TEXT)
        test_nodes = [test_node]

        result = split_nodes_image(test_nodes)

        assert len(result) == 1, f"The resulting list should have 1 nodes, but instead split into {len(result)}"

        assert result[0].text == "This is text without an image present", f"The text for result[0] should have been 'This is text without an image present', but instead reads {result[0]}"
        assert result[0].text_type == TextType.TEXT, f"The TextType for result[0] should have been TextType.TEXT, but was instead {result[0].text_type}"

        print(f"\nThis is the result of TestSplit_Nodes_Image_Noimage: {result}\n")
        print(f"\nThis is the test_node that was used: [{repr(test_node)}]\n")
        print(f"\nThis was the test_nodes list used: [{test_nodes}]")
        print("----------------------------------------------------------")