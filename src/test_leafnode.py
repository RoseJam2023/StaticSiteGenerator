import unittest

from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):

    def test_create_node(self):
        node = LeafNode("p", "This is the test node's text", props={"test": "_test"})

        print(f"\nThis is the result of LeafNode test_create_node: [{repr(node)}]")

    def test_leafnode_tohtml_p(self):
        node = LeafNode("p", "This is the test node's text")

        print(f"\nThis is the result of LeafNode test_leafnode_tohtml_p: [{node.to_html()}]")

    def test_leafnode_tohtml_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})

        print(f'\nThis is the result of LeafNode test_leafnode_tohtml_a: [{node.to_html()}]')

    '''def test_leafnode_tohtml_wild(self):
        node = LeafNode("r", "This is the test node's text")

        print(f"This is the result of LeafNode test_leafnode_tohtml_wild: {node.to_html()}")
    '''

if __name__ == "__main__":
    unittest.main()