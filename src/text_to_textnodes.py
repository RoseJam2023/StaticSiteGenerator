from textnode import TextNode, TextType
from split_nodes_delimiter import split_nodes_delimiter, find_first_complete_delimiter
from split_nodes_image import split_nodes_image
from split_nodes_link import split_nodes_link

def text_to_textnodes(text):


    initial_node = TextNode(text, TextType.TEXT)
    initial_list = [initial_node]

    '''first_delimiter = find_first_complete_delimiter(text)

    if first_delimiter == "**":
        delimiter_type = TextType.BOLD

    elif first_delimiter == "*":
        delimiter_type = TextType.ITALIC
    
    else:
        delimiter_type = TextType.CODE'''

    bold_split = split_nodes_delimiter(initial_list, "**", TextType.BOLD)
    code_split = split_nodes_delimiter(bold_split, "`", TextType.CODE)
    italic_split = split_nodes_delimiter(code_split, "*", TextType.ITALIC)
    image_split = split_nodes_image(italic_split)
    final_split = split_nodes_link(image_split)



    return final_split

