import unittest
from textnode import TextNode, TextType
from split_nodes_delimiter import split_nodes_delimiter
from split_nodes_image import split_nodes_image
from split_nodes_link import split_nodes_link
from text_to_textnodes import text_to_textnodes

'''
Test cases still to implement:
Test text with only delimiters
Test text with only an image
Test text with only a link
Test text with delimiters and an image
Test text with delimiters and a link
test text with an image and a link
Test text with no markdown syntax
'''

class TestText_To_Textnodes(unittest.TestCase):
    def test_text_to_textnodes(self):
        result = []
        test_text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"

        result = text_to_textnodes(test_text)

        assert len(result) == 10, f"Should split into 10 nodes, but instead split into {len(result)}.\n Please review result nodes: {result}"

        assert result[0].text == "This is ", f"result[0].text should be 'This is ', but instead is [{result[0].text}]"
        assert result[0].text_type == TextType.TEXT, f"result[0].text_type should be TEXT but is instead: [{result[0].text_type}]"

        assert result[1].text == "text", f"result[1].text should be 'text', but instead is [{result[1].text}]"
        assert result[1].text_type == TextType.BOLD, f"result[1].text_type should be BOLD but is instead: [{result[1].text_type}]"

        assert result[2].text == " with an ", f"result[2].text should be ' with an ', but instead is [{result[2].text}]"
        assert result[2].text_type == TextType.TEXT, f"result[2].text_type should be TEXT but is instead: [{result[2].text_type}]"

        assert result[3].text == "italic", f"result[3].text should be 'italic', but instead is [{result[3].text}]"
        assert result[3].text_type == TextType.ITALIC, f"result[3].text_type should be ITALIC but is instead: [{result[3].text_type}]"

        assert result[4].text == " word and a ", f"result[4].text should be ' word and a ', but instead is [{result[4].text}]"
        assert result[4].text_type == TextType.TEXT, f"result[4].text_type should be TEXT but is instead: [{result[4].text_type}]"

        assert result[5].text == "code block", f"result[5].text should be 'code block', but instead is [{result[5].text}]"
        assert result[5].text_type == TextType.CODE, f"result[5].text_type should be CODE but is instead: [{result[5].text_type}]"

        assert result[6].text == " and an ", f"result[6].text should be ' and an ', but instead is [{result[6].text}]"
        assert result[6].text_type == TextType.TEXT, f"result[6].text_type should be TEXT but is instead: [{result[6].text_type}]"

        assert result[7].text == "obi wan image", f"result[7].text should be 'obi wan image', but instead is [{result[7].text}]"
        assert result[7].text_type == TextType.IMAGE, f"result[7].text_type should be IMAGE but is instead: [{result[7].text_type}]"
        assert result[7].url == "https://i.imgur.com/fJRm4Vk.jpeg", f"The URL for result[7] should have been 'https://i.imgur.com/fJRm4Vk.jpeg', but was instead {result[7].url}"

        assert result[8].text == " and a ", f"result[8].text should be ' and a ', but instead is [{result[8].text}]"
        assert result[8].text_type == TextType.TEXT, f"result[8].text_type should be TEXT but is instead: [{result[8].text_type}]"

        assert result[9].text == "link", f"result[9].text should be 'link', but instead is [{result[9].text}]"
        assert result[9].text_type == TextType.LINK, f"result[9].text_type should be LINK but is instead: [{result[9].text_type}]"
        assert result[9].url == "https://boot.dev", f"The URL for result[9] should read 'https://boot.dev', but instead reads {result[9].url}"

        print(f"\nThis is the result of TestText_To_TextNodes: [{result}]\n")
        print(f"\nThis is the test_text that was used: [{test_text}]\n")
        print("----------------------------------------------------------")

    def test_text_to_textnodes_reversed(self):
            result = []
            test_text = "This is a [link](https://boot.dev) and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a `code block` with an *italic* word and a bold **word.**"

            result = text_to_textnodes(test_text)

            assert len(result) == 10, f"Should split into 10 nodes, but instead split into {len(result)}.\n Please review result nodes: {result}"

            assert result[0].text == "This is a ", f"result[0].text should be 'This is a', but instead is [{result[0].text}]"
            assert result[0].text_type == TextType.TEXT, f"result[0].text_type should be TEXT but is instead: [{result[0].text_type}]"

            assert result[1].text == "link", f"result[1].text should be 'link', but instead is [{result[1].text}]"
            assert result[1].text_type == TextType.LINK, f"result[1].text_type should be LINK but is instead: [{result[1].text_type}]"
            assert result[1].url == "https://boot.dev", f"The URL for result[1] should read 'https://boot.dev', but instead reads {result[1].url}"

            assert result[2].text == " and an ", f"result[2].text should be ' and an ', but instead is [{result[2].text}]"
            assert result[2].text_type == TextType.TEXT, f"result[2].text_type should be TEXT but is instead: [{result[2].text_type}]"

            assert result[3].text == "obi wan image", f"result[3].text should be 'obi wan image', but instead is [{result[3].text}]"
            assert result[3].text_type == TextType.IMAGE, f"result[3].text_type should be IMAGE but is instead: [{result[3].text_type}]"
            assert result[3].url == "https://i.imgur.com/fJRm4Vk.jpeg", f"The URL for result[3] should have been 'https://i.imgur.com/fJRm4Vk.jpeg', but was instead {result[3].url}"

            assert result[4].text == " and a ", f"result[4].text should be ' and a ', but instead is [{result[4].text}]"
            assert result[4].text_type == TextType.TEXT, f"result[4].text_type should be TEXT but is instead: [{result[4].text_type}]"

            assert result[5].text == "code block", f"result[5].text should be 'code block', but instead is [{result[5].text}]"
            assert result[5].text_type == TextType.CODE, f"result[5].text_type should be CODE but is instead: [{result[5].text_type}]"

            assert result[6].text == " with an ", f"result[6].text should be ' with an ', but instead is [{result[6].text}]"
            assert result[6].text_type == TextType.TEXT, f"result[6].text_type should be TEXT but is instead: [{result[6].text_type}]"

            assert result[7].text == "italic", f"result[7].text should be 'italic', but instead is [{result[7].text}]"
            assert result[7].text_type == TextType.ITALIC, f"result[7].text_type should be ITALIC but is instead: [{result[7].text_type}]"

            assert result[8].text == " word and a bold ", f"result[8].text should be ' word and a bold ', but instead is [{result[8].text}]"
            assert result[8].text_type == TextType.TEXT, f"result[8].text_type should be TEXT but is instead: [{result[8].text_type}]"

            assert result[9].text == "word.", f"result[9].text should be 'word.', but instead is [{result[9].text}]"
            assert result[9].text_type == TextType.BOLD, f"result[9].text_type should be BOLD but is instead: [{result[9].text_type}]"

            print(f"\nThis is the result of TestText_To_TextNodes_Reverse: [{result}]\n")
            print(f"\nThis is the test_text that was used: [{test_text}]\n")
            print("----------------------------------------------------------")