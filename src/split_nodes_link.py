from textnode import *
from extract_markdown_links import *
import re

def split_nodes_link(old_nodes):
    new_nodes = []
    splitting_pattern = r"(.*?)(\[[^\[\]]*\]\([^\(\)]*\))(.*)"

    for old_node in old_nodes:

        link_match = re.match(splitting_pattern, old_node.text)

        '''link_match.group(1) = Everything before the instance of a markdown link
        link_match.group(2) = The Markdown link itself
        link_match.group(3) = Everything after the Markdown link including additional links
        '''
        
        
        if not link_match:
            new_nodes.append(old_node)
            continue
        
        prior_node, link_node, end_node = node_creation_helper_function(link_match.group(1), link_match.group(2), link_match.group(3))

        print(f"link_match group(1) is {link_match.group(1)}")
        print(f"link_match group(2) is {link_match.group(2)}")
        print(f"link_match group(3) is {link_match.group(3)}")

        print(f"link_match prior node is {repr(prior_node)}")
        print(f"link_match link node is {repr(link_node)}")
        print(f"link_match end node is {repr(end_node)}")
        

        if prior_node and prior_node.text != "":
            new_nodes.append(prior_node)

        new_nodes.append(link_node)

        recursive_match = re.match(splitting_pattern, end_node.text)

        while recursive_match:
            
            prior_node, link_node, end_node = node_creation_helper_function(
                recursive_match.group(1), recursive_match.group(2), recursive_match.group(3)
                )
        
            print(f"Recursive_match prior node is {repr(prior_node)}")
            print(f"Recursive_match link node is {repr(link_node)}")
            print(f"Recursive_match end node is {repr(end_node)}")

            if prior_node.text != "":
                new_nodes.append(prior_node)

            new_nodes.append(link_node)

            recursive_match = re.match(splitting_pattern, end_node.text)

        if end_node.text != "":
                new_nodes.append(end_node)

    return new_nodes

def node_creation_helper_function(before_link, link, after_link):

    prior_node = TextNode(before_link, TextType.TEXT)

    extracted_link = extract_markdown_links(link)

    link_node = TextNode(extracted_link[0][0], TextType.LINK, extracted_link[0][1])

    end_node = TextNode(after_link, TextType.TEXT)

    return prior_node, link_node, end_node