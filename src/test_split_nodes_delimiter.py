import unittest
from textnode import TextNode, TextType
from split_nodes_delimiter import *

'''Additional possible test cases:

    Multiple instances of the same delimiter
    Different delimiters in reverse order
    Incomplete delimiter pairs
    Empty text
    Text with no delimiters
'''

class TestSplit_Nodes_Delimiter(unittest.TestCase):
    def test_split_nodes_delimiter_bold(self):
        text_node = TextNode("This is a text line with a **bold** word inside.", TextType.TEXT)
        old_nodes = [text_node]

        result = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)

        # Check we got the expected number of nodes
        assert len(result) == 3, "Should split into 3 nodes"
    
        # Check the content and type of each node
        assert result[0].text == "This is a text line with a ", f"result[0].text should be 'This is a text line with a ', but is instead [{result[0].text}]"
        assert result[0].text_type == TextType.TEXT
    
        assert result[1].text == "bold", f"result[1].text should be 'bold', but is instead [{result[1].text}]"
        assert result[1].text_type == TextType.BOLD
    
        assert result[2].text == " word inside.", f"result[2].text should be 'word inside.' but is instead [{result[2].text}]"
        assert result[2].text_type == TextType.TEXT

        print(f"\nThis is the result of TestSplit_Nodes_Delimiter with bold text: [{result}]\n")
        print(f"\nThis is the text_node that was used: [{repr(text_node)}]\n")
        print(f"\nThis was the old_nodes list used: [{old_nodes}]")
        print("----------------------------------------------------------")

    def test_split_nodes_delimiter_multiple_bold(self):
        
        text_node = TextNode("This is a text line with two **bold** words **inside**.", TextType.TEXT)
        old_nodes = [text_node]

        result = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)

        assert len(result) == 5, f"Should split into 5 nodes, but instead split into {len(result)}.\n Please review result nodes: [{result}]"

        assert result[0].text == "This is a text line with two ", f"result[0].text should be 'This is a text line with two ', but instead is [{result[0].text}]"
        assert result[0].text_type == TextType.TEXT

        assert result[1].text == "bold", f"result[1].text should be 'bold', but instead is [{result[1].text}]"
        assert result[1].text_type == TextType.BOLD

        assert result[2].text == " words ", f"result[2].text should be ' words ', but instead is [{result[2].text}]"
        assert result[2].text_type == TextType.TEXT

        assert result[3].text == "inside", f"result[3].text should be 'inside', but instead is [{result[3].text}]"
        assert result[3].text_type == TextType.BOLD

        assert result[4].text == ".", f"result[4].text should be '.', but instead is [{result[4].text}]"
        assert result[4].text_type == TextType.TEXT

        print(f"\nThis is the result of TestSplit_Nodes_Delimiter with multiple bolded text: [{result}]\n")
        print(f"\nThis is the text_node that was used: [{repr(text_node)}]\n")
        print(f"\nThis was the old_nodes list used: [{old_nodes}]")
        print("----------------------------------------------------------")


    def test_split_nodes_delimiter_italics(self):
        
        text_node = TextNode("This is a text line with a *italic* word inside.", TextType.TEXT)
        old_nodes = [text_node]

        result = split_nodes_delimiter(old_nodes, "*", TextType.ITALIC)

        # Check we got the expected number of nodes
        assert len(result) == 3, "Should split into 3 nodes"
    
        # Check the content and type of each node
        assert result[0].text == "This is a text line with a ", f"result[0].text should be 'This is a text line with a ', but is instead [{result[0].text}]"
        assert result[0].text_type == TextType.TEXT
    
        assert result[1].text == "italic", f"result[1].text should be 'italic', but is instead [{result[1].text}]"
        assert result[1].text_type == TextType.ITALIC
    
        assert result[2].text == " word inside.", f"result[2].text should be 'word inside.' but is instead [{result[2].text}]"
        assert result[2].text_type == TextType.TEXT

        print(f"\nThis is the result of TestSplit_Nodes_Delimiter with italic text: [{result}]\n")
        print(f"\nThis is the text_node that was used: [{repr(text_node)}]\n")
        print(f"\nThis was the old_nodes list used: [{old_nodes}]")
        print("----------------------------------------------------------")   

    def test_split_nodes_delimiter_code(self):
        
        text_node = TextNode("`This` is a text line with a code word inside.", TextType.TEXT)
        old_nodes = [text_node]

        result = split_nodes_delimiter(old_nodes, "`", TextType.CODE)

        # Check we got the expected number of nodes
        assert len(result) == 2, f"Should split into 2 nodes, but actually split into [{len(result)}]"
    
        # Check the content and type of each node
        assert result[0].text == "This", f"result[0].text should be 'This', but is instead [{result[0].text}]"
        assert result[0].text_type == TextType.CODE
    
        assert result[1].text == " is a text line with a code word inside.", f"result[1].text should be 'is a text line with a code word inside.', but is instead [{result[1].text}]"
        assert result[1].text_type == TextType.TEXT, f"This text node should be TextType.TEXT, but is instead [{result[1].text_type}] "

        print(f"\nThis is the result of TestSplit_Nodes_Delimiter with code text: [{result}]\n")
        print(f"\nThis is the text_node that was used: [{repr(text_node)}]\n")
        print(f"\nThis was the old_nodes list used: [{old_nodes}]")
        print("----------------------------------------------------------")

    def test_split_nodes_delimiter_mixed_delimiters(self):
        
        text_node = TextNode("This is a text line with one **bold** word and one *italics* word.", TextType.TEXT)
        old_nodes = [text_node]

        result = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)

        assert len(result) == 5, f"Should split into 5 nodes, but instead split into {len(result)}.\n Please review result nodes: [{result}]"

        assert result[0].text == "This is a text line with one ", f"result[0].text should be 'This is a text line with one ', but instead is [{result[0].text}]"
        assert result[0].text_type == TextType.TEXT

        assert result[1].text == "bold", f"result[1].text should be 'bold', but instead is [{result[1].text}]"
        assert result[1].text_type == TextType.BOLD

        assert result[2].text == " word and one ", f"result[2].text should be ' word and one ', but instead is [{result[2].text}]"
        assert result[2].text_type == TextType.TEXT

        assert result[3].text == "italics", f"result[3].text should be 'italics', but instead is [{result[3].text}]"
        assert result[3].text_type == TextType.ITALIC

        assert result[4].text == " word.", f"result[4].text should be 'word.', but instead is [{result[4].text}]"
        assert result[4].text_type == TextType.TEXT

        print(f"\nThis is the result of TestSplit_Nodes_Delimiter with mixed bold and italic delimiters: [{result}]\n")
        print(f"\nThis is the text_node that was used: [{repr(text_node)}]\n")
        print(f"\nThis was the old_nodes list used: [{old_nodes}]")
        print("----------------------------------------------------------")
    
    def test_split_nodes_delimiter_start_and_end_delimiters(self):
        text_node = TextNode("**This** is a text line with a bold delimiter at the front and an italics delimiter at the *end.*", TextType.TEXT)
        old_nodes = [text_node]

        result = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)

        assert len(result) == 3, f"Should split into 3 nodes, but instead split into [{len(result)}]"

        assert result[0].text == "This", f"result[0] should be 'This', but instead reads: [{result[0]}]"
        assert result[0].text_type == TextType.BOLD

        assert result[1].text == " is a text line with a bold delimiter at the front and an italics delimiter at the "
        assert result[1].text_type == TextType.TEXT
        
        assert result[2].text == "end.", f"result[2] should be 'end.', but instead reads: [{result[2]}]"
        assert result[2].text_type == TextType.ITALIC

        print(f"\nThis is the result of TestSplit_Nodes_Delimiter with delimiters at the start and end: [{result}]\n")
        print(f"\nThis is the text_node that was used: [{repr(text_node)}]\n")
        print(f"\nThis was the old_nodes list used: [{old_nodes}]")
        print("----------------------------------------------------------")

    def test_split_nodes_delimiter_invalid_delimiter(self):
        with self.assertRaises(ValueError) as context:

            text_node = TextNode("This is a text line with an invalid [link](https://www.google.com) delimiter", TextType.TEXT)
            old_nodes = [text_node]

            result = split_nodes_delimiter(old_nodes, "[]", TextType.LINK)

            print(result)

        self.assertEqual(
            str(context.exception),
            "Invalid delimiter chosen"
        )

    def test_split_nodes_delimiter_delimiter_out_of_order(self):
        with self.assertRaises(ValueError) as context:

            text_node = TextNode("This is a text line with one **bold** word and one *italics* word.", TextType.TEXT)
            old_nodes = [text_node]

            result = split_nodes_delimiter(old_nodes, "*", TextType.ITALIC)

            print(result)

        self.assertEqual(
            str(context.exception),
            "Provided delimiter is not the first delimiter pair that exists in the text"
        )
