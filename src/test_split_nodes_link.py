import unittest
from textnode import TextNode, TextType
from split_nodes_link import *

'''Additional tests to be implemented:
Testing node with no links
Testing mixed nodes
'''

class TestSplit_Nodes_link(unittest.TestCase):
    def test_split_nodes_link(self):
        test_node = TextNode(
    "This is text with a link [to boot dev](https://www.boot.dev) and nothing else.",
    TextType.TEXT)
        
        test_nodes = [test_node]

        result = split_nodes_link(test_nodes)

        assert len(result) == 3, f"The resulting list should have 3 nodes but instead has {len(result)}"

        assert result[0].text == "This is text with a link ", f"The text for result[0] should read 'This is text with a link ', but instead reads {result[0].text}"
        assert result[0].text_type == TextType.TEXT, f"The TextType for result[0] should be TextType.TEXT, but is instead {result[0].text_type}"

        assert result[1].text == "to boot dev", f"The text for result[1] should read 'to boot dev' but instead reads {result[1].text}"
        assert result[1].text_type == TextType.LINK, f"The TextType for result[1] should be TextType.LINK, but is instead {result[1].text_type}"
        assert result[1].url == "https://www.boot.dev", f"The URL for result[1] should read 'https://www.boot.dev', but instead reads {result[1].url}"

        assert result[2].text == " and nothing else.", f"The text for result[2] should read ' and nothing else.', but instead reads {result[2].text}"
        assert result[2].text_type == TextType.TEXT, f"The TextType for result[2] should be TextType.TEXT, but is instead {result[2].text_type}"

        print(f"\nThis is the result of Test_Split_Nodes_Link: {result}\n")
        print(f"\nThis is the test_node that was used: [{repr(test_node)}]\n")
        print(f"\nThis was the test_nodes list used: [{test_nodes}]")
        print("----------------------------------------------------------")

    def test_split_nodes_link_multiple_links(self):
        test_node = TextNode(
    "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev) as well.",
    TextType.TEXT,
)
        
        test_nodes = [test_node]

        result = split_nodes_link(test_nodes)

        assert len(result) == 5, f"The resulting list should have 5 nodes but instead has {len(result)}"

        assert result[0].text == "This is text with a link ", f"The text for result[0] should read 'This is text with a link ', but instead reads {result[0].text}"
        assert result[0].text_type == TextType.TEXT, f"The TextType for result[0] should be TextType.TEXT, but is instead {result[0].text_type}"

        assert result[1].text == "to boot dev", f"The text for result[1] should read 'to boot dev' but instead reads {result[1].text}"
        assert result[1].text_type == TextType.LINK, f"The TextType for result[1] should be TextType.LINK, but is instead {result[1].text_type}"
        assert result[1].url == "https://www.boot.dev", f"The URL for result[1] should read 'https://www.boot.dev', but instead reads {result[1].url}"

        assert result[2].text == " and ", f"The text for result[2] should read ' and ', but instead reads {result[2].text}"
        assert result[2].text_type == TextType.TEXT, f"The TextType for result[2] should be TextType.TEXT, but is instead {result[2].text_type}"

        assert result[3].text == "to youtube", f"The text for result[3] should read 'to youtube' but instead reads {result[3].text}"
        assert result[3].text_type == TextType.LINK, f"The TextType for result[3] should be TextType.LINK, but is instead {result[3].text_type}"
        assert result[3].url == "https://www.youtube.com/@bootdotdev", f"The URL for result[3] should read 'https://www.youtube.com/@bootdotdev', but instead reads {result[3].url}"

        assert result[4].text == " as well.", f"The text for result[4] should read ' as well.', but instead reads {result[4].text}"
        assert result[4].text_type == TextType.TEXT, f"The TextType for result[4] should be TextType.TEXT, but is instead {result[4].text_type}"

        print(f"\nThis is the result of Test_Split_Nodes_Link_Multiple_Links: {result}\n")
        print(f"\nThis is the test_node that was used: [{repr(test_node)}]\n")
        print(f"\nThis was the test_nodes list used: [{test_nodes}]")
        print("----------------------------------------------------------")