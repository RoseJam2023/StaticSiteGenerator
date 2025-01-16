import unittest

from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):

    def test_create_node(self):
        node = LeafNode("p", "This is the test node's text", props={"test": "_test"})

        print(f"\nThis is the result of LeafNode test_create_node: [{repr(node)}]\n")
        print("-------------------------------------------------------")

    def test_create_node_onlyvalue(self):
        node = LeafNode("This is a test for only a value argument")

        print(f"\nThis is the result of LeafNode test_create_node_onlyvalue: [{repr(node)}]\n")
        print(f"This was the tested LeafNode: <{repr(node)}>\n")
        print("-------------------------------------------------------")

    def test_leafnode_tohtml_rawtext(self):
        node = LeafNode("This is a test for only a value argument")

        print(f"\nThis is the result of LeafNode test_tohtml_rawtext: [{node.to_html()}]")
        print(f"This was the tested LeafNode: <{repr(node)}>\n")
        print("-------------------------------------------------------")

    def test_leafnode_tohtml_p(self):
        node = LeafNode("p", "This is the test node's text")

        print(f"\nThis is the result of LeafNode test_leafnode_tohtml_p: [{node.to_html()}]")
        print(f"This was the tested LeafNode: <{repr(node)}>\n")
        print("-------------------------------------------------------")

    def test_leafnode_tohtml_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})

        print(f'\nThis is the result of LeafNode test_leafnode_tohtml_a: [{node.to_html()}]')
        print(f"This was the tested LeafNode: <{repr(node)}>\n")
        print("-------------------------------------------------------")

    def test_leafnode_tohtml_img(self):
        node = LeafNode("img", props={"src": "https://www.google.com", "alt": "This is a test image"})

        print(f"\nThis is the LeafNode being tested: <{repr(node)}>")
        print(f'This is the result of LeafNode test_leafnode_tohtml_img: [{node.to_html()}]')
        print("-------------------------------------------------------")

    def test_leafnode_img_regression(self):
        node = LeafNode("img", props={"src": "url", "alt": "alt text"})
        try:
            assert node.to_html() == '<img src="url" alt="alt text">'
        except Exception as e:
            assert False, f"Unexpected error in image node: {e}"


    '''def test_leafnode_tohtml_wild(self):
        node = LeafNode("r", "This is the test node's text")

        print(f"This is the result of LeafNode test_leafnode_tohtml_wild: {node.to_html()}")
    '''

if __name__ == "__main__":
    unittest.main()