import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq_nourl(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.test.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://www.test.com")
        self.assertEqual(node, node2)

    def test_uneq_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_uneq_textwithurl(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.test.com")
        node2 = TextNode("This is a different text node", TextType.BOLD, "https://www.test.com")
        self.assertNotEqual(node, node2)
        
    def test_uneq_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.CODE)
        self.assertNotEqual(node, node2)

    def test_uneq_typewithurl(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.test.com")
        node2 = TextNode("This is a text node", TextType.CODE, "https://www.test.com")
        self.assertNotEqual(node, node2)

    def test_uneq_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.test.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://www.unequaltest.com")
        self.assertNotEqual(node, node2)

    def test_uneq_nourl(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.test.com")
        node2 = TextNode("This is a text node", TextType.BOLD,)
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()