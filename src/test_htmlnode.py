import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

    def test_create_node(self):
        testchild1 = HTMLNode("a","This is the child node's test text", 
                              props={"href": "https://google.com", "target": "_blank", "test": "_test"})
        testchild2 = HTMLNode("h1","This is the child node's test text", 
                              props={"href": "https://google.com", "test": "_test"})
        testchildren = [testchild1, testchild2]
        
        testnode = HTMLNode("p", "This is the test node's text", testchildren, props={"href": "https://google.com"})

        print(f"\nThis is the result of HTMLNode test_create_node:\n {repr(testnode)}\n")
        print("-------------------------------------------------------")

    def test_eq_noargs(self):
        node = HTMLNode()
        node2 = HTMLNode()
        self.assertEqual(node, node2)

    def test_eq_tag(self):
        node = HTMLNode("h1")
        node2 = HTMLNode("h1")
        self.assertEqual(node, node2)

    def test_eq_value(self):
        node = HTMLNode(value="This is the test text")
        node2 = HTMLNode(value="This is the test text")
        self.assertEqual(node, node2)

    def test_eq_children(self):
        testchildren = [HTMLNode("h1","This is the test text", props={"href": "https://google.com", "target": "_blank", "test": "_test"}), 
                        HTMLNode("h1","This is the test text", props={"href": "https://google.com", "target": "_blank", "test": "_test"})]
        
        node = HTMLNode(children= testchildren)
        node2 = HTMLNode(children= testchildren)
        self.assertEqual(node, node2)

    def test_eq_props(self):
        node = HTMLNode(props={"href": "https://google.com", "target": "_blank", "test": "_test"})
        node2 = HTMLNode(props={"href": "https://google.com", "target": "_blank", "test": "_test"})
        self.assertEqual(node, node2)

    def test_uneq_tag(self):
        node = HTMLNode("h1")
        node2 = HTMLNode("p")
        self.assertNotEqual(node, node2)
    
    def test_uneq_value(self):
        node = HTMLNode(value= "This is test node one's text")
        node2 = HTMLNode(value= "This is test node two's text")
        self.assertNotEqual(node, node2)

    def test_uneq_children(self):
        testchildren1 = [HTMLNode("h1","This is the first node's child test text", props={"href": "https://google.com", "target": "_blank", "test": "_test"}), 
                        HTMLNode("This is the first node's child test text", props={"href": "https://google.com", "target": "_blank", "test": "_test"})]
        
        testchildren2 = [HTMLNode("h1","This is the second node's child test text", props={"href": "https://google.com", "target": "_blank", "test": "_test"}), 
                        HTMLNode("This is the second node's child test text", props={"href": "https://google.com", "target": "_blank", "test": "_test"})]
        
        node = HTMLNode(children= testchildren1)
        node2 = HTMLNode(children= testchildren2)
        self.assertNotEqual(node, node2)

    def test_uneq_props(self):
        node = HTMLNode(props={"href": "https://google.com", "target": "_blank"})
        node2 = HTMLNode(props={"href": "https://google.com", "target": "_blank", "test": "_test"})
        self.assertNotEqual(node, node2)

    def test_props_to_html(self):
        node = HTMLNode(props={"href": "https://google.com", "target": "_blank", "test": "_test"})

        print(f"\nThis is the result of HTML Node test_props_to_html: [{node.props_to_html()}]\n")
        print(f"This was the tested HTMLNode: <{repr(node)}>\n")
        print(f"-------------------------------------------------------")

