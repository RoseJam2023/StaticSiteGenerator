import unittest

from htmlnode import *

class TestParentNode(unittest.TestCase):

    def test_create_node_nochildren(self):
        with self.assertRaises(ValueError) as context:
            ParentNode("p", [])

        self.assertEqual(
            str(context.exception),
            "ParentNode must have at least one child."
    )
    
    def test_create_node_onechild(self):
        child_node_one = LeafNode("b", "This is child node one's text")
        children = [child_node_one]

        parent = ParentNode("p", children)

        print(f"\nThis is the result of Parent Node test_create_node_onechild: [{repr(parent)}]\n")
        print("-------------------------------------------------------")

    def test_create_node_multichild(self):
        child_node_one = LeafNode("b", "This is child node one's text")
        child_node_two = LeafNode("This is child node two's text")
        child_node_three = LeafNode("i", "This is child node three's text")
        children = [child_node_one, child_node_two, child_node_three]

        parent = ParentNode("p", children)

        print(f"\nThis is the result of Parent Node test_create_node_multichild: [{repr(parent)}]\n")
        print("-------------------------------------------------------")

    def test_create_node_multiparent(self):
        child_node_one = LeafNode("b", "This is child node one's text")
        child_node_two = LeafNode("This is child node two's text")
        child_node_three = LeafNode("i", "This is child node three's text")
        
        grandchildren = [child_node_one, child_node_two, child_node_three]

        parent = ParentNode("p", grandchildren)

        children = [parent]

        grandparent = ParentNode("p", children)

        print(f"\nThis is the result of Parent Node test_create_node_multiparent: [{repr(grandparent)}]\n")
        print("-------------------------------------------------------")

    def test_parentnode_tohtml_onechild(self):
        child_node_one = LeafNode("b", "This is child node one's text")

        children = [child_node_one]

        parent = ParentNode("p", children)

        print(f"\nThis is the result of Parent Node test_parentnode_tohtml_onechild: [{parent.to_html()}]\n")
        print(f"This was the tested ParentNode: <{repr(parent)}>\n")
        print("-------------------------------------------------------")

    def test_parentnode_tohtml_multichild(self):
        child_node_one = LeafNode("b", "This is child node one's text")
        child_node_two = LeafNode("This is child node two's text")
        child_node_three = LeafNode("i", "This is child node three's text")
        children = [child_node_one, child_node_two, child_node_three]

        parent = ParentNode("p", children)

        print(f"\nThis is the result of Parent Node test_parentnode_tohtml: [{parent.to_html()}]\n")
        print(f"This was the tested ParentNode: <{repr(parent)}>\n")
        print("-------------------------------------------------------")

    def test_parentnode_tohtml_multiparent(self):
        child_node_one = LeafNode("b", "This is child node one's text")
        child_node_two = LeafNode("This is child node two's text")
        child_node_three = LeafNode("i", "This is child node three's text")
        
        grandchildren = [child_node_one, child_node_two, child_node_three]

        parent = ParentNode("p", grandchildren)

        children = [parent]

        grandparent = ParentNode("p", children)

        print(f"\nThis is the result of Parent Node test_parentnode_tohtml_multiparent: [{grandparent.to_html()}]\n")
        print(f"This was the tested ParentNode: <{repr(grandparent)}>\n")
        print("-------------------------------------------------------")