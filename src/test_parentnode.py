import unittest

from htmlnode import *

class TestParentNode(unittest.TestCase):

    def test_create_node(self):
        child_node_one = LeafNode("b", "This is child node one's text")
        child_node_two = LeafNode("This is child node two's text")
        child_node_three = LeafNode("i", "This is child node three's text")
        children = [child_node_one, child_node_two, child_node_three]

        parent = ParentNode("p", children)

        print(f"\nThis is the result of Parent Node test_create_node: [{repr(parent)}]\n")
        print("-------------------------------------------------------")

    def test_parentnode_tohtml(self):
        child_node_one = LeafNode("b", "This is child node one's text")
        child_node_two = LeafNode("This is child node two's text")
        child_node_three = LeafNode("i", "This is child node three's text")
        children = [child_node_one, child_node_two, child_node_three]

        parent = ParentNode("p", children)

        print(f"\nThis is the result of Parent Node test_parentnode_tohtml: [{parent.to_html()}]\n")
        print(f"This was the tested ParentNode: <{repr(parent)}>\n")
        print("-------------------------------------------------------")