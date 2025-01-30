from textnode import *
from extract_markdown_images import *
import re

def split_nodes_image(old_nodes):
    new_nodes = []
    splitting_pattern = r"(.*?)(!\[[^\[\]]*\]\([^\(\)]*\))(.*)"

    for old_node in old_nodes:

        image_match = re.match(splitting_pattern, old_node.text)

        '''image_match.group(1) = Everything before the instance of a markdown image
        image_match.group(2) = The Markdown image itself
        image_match.group(3) = Everything after the Markdown image including additional images
        '''
        
        
        if not image_match:
            new_nodes.append(old_node)
            continue
        
        prior_node, image_node, end_node = node_creation_helper_function(image_match.group(1), image_match.group(2), image_match.group(3))

        print(f"Image_match group(1) is {image_match.group(1)}")
        print(f"Image_match group(2) is {image_match.group(2)}")
        print(f"Image_match group(3) is {image_match.group(3)}")

        print(f"Image_match prior node is {repr(prior_node)}")
        print(f"Image_match image node is {repr(image_node)}")
        print(f"Image_match end node is {repr(end_node)}")
        

        if prior_node and prior_node.text != "":
            new_nodes.append(prior_node)

        new_nodes.append(image_node)

        recursive_match = re.match(splitting_pattern, end_node.text)

        while recursive_match:
            
            prior_node, image_node, end_node = node_creation_helper_function(
                recursive_match.group(1), recursive_match.group(2), recursive_match.group(3)
                )
        
            print(f"Recursive_match prior node is {repr(prior_node)}")
            print(f"Recursive_match image node is {repr(image_node)}")
            print(f"Recursive_match end node is {repr(end_node)}")

            if prior_node.text != "":
                new_nodes.append(prior_node)

            new_nodes.append(image_node)

            recursive_match = re.match(splitting_pattern, end_node.text)

        if end_node.text != "":
                new_nodes.append(end_node)

    return new_nodes

def node_creation_helper_function(before_image, image, after_image):

    prior_node = TextNode(before_image, TextType.TEXT)

    extracted_image = extract_markdown_images(image)

    image_node = TextNode(extracted_image[0][0], TextType.IMAGE, extracted_image[0][1])

    end_node = TextNode(after_image, TextType.TEXT)

    return prior_node, image_node, end_node
