from textnode import TextNode, TextType

delimiters = {"**":TextType.BOLD, "*":TextType.ITALIC, "`":TextType.CODE}

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    global delimiters

    if delimiter not in delimiters:
        raise ValueError("Invalid delimiter chosen")

    for old_node in old_nodes:
        if old_node.text_type is not TextType.TEXT:
            new_nodes.append(old_node)

        elif delimiter not in old_node.text:
            new_nodes.append(old_node)

        else:
        
            first_complete = find_first_complete_delimiter(old_node.text)
            if first_complete != delimiter:
                raise ValueError("Provided delimiter is not the first delimiter pair that exists in the text")
                
            first_index, second_index = find_delimiter_helper_function(old_node.text, delimiter)

            prior_node, delimited_node, end_node = node_creation_helper_function(old_node.text, first_index, second_index, delimiter, text_type)

            if prior_node.text != "":
                new_nodes.append(prior_node)

            new_nodes.append(delimited_node)

            for key in delimiters:

                while key in end_node.text:
                    first_index, second_index = find_delimiter_helper_function(end_node.text, key)

                    prior_node, delimited_node, end_node = node_creation_helper_function(end_node.text, first_index, second_index, key, delimiters[key])

                    if prior_node.text != "":
                        new_nodes.append(prior_node)

                    new_nodes.append(delimited_node)

            if end_node.text != "":
                new_nodes.append(end_node)

    return new_nodes



            
def find_delimiter_helper_function(string, delimiter):
    delimiter_length = len(delimiter)
    global delimiters

    

    first_index = string.find(delimiter)

    second_index = string.find(delimiter, first_index + delimiter_length)

    if second_index is -1:
            raise Exception ("Invalid Markdown syntax: No matching delimiter")

    return first_index, second_index

def node_creation_helper_function(string, first_index, second_index, delimiter, text_type):
    delimiter_length = len(delimiter)

    if first_index == 0:
        prior_node = TextNode("", text_type)
        delimited_node = TextNode(string[first_index + delimiter_length:second_index], text_type)
        end_node = TextNode(string[second_index + delimiter_length:], TextType.TEXT)

        return prior_node, delimited_node, end_node

    prior_node = TextNode(string[0:first_index], TextType.TEXT)
    delimited_node = TextNode(string[first_index + delimiter_length:second_index], text_type)

    remaining_text = string[second_index + delimiter_length:]
    if remaining_text:
        end_node = TextNode(remaining_text, TextType.TEXT)
        return prior_node, delimited_node, end_node
    else:
        end_node = TextNode("", TextType.TEXT)
        return prior_node, delimited_node, end_node
    
def find_first_complete_delimiter(text):
    first_complete_delimiter = None
    earliest_position = float('inf')
    
    for delim in delimiters:
        # Find first occurrence of delimiter
        start = text.find(delim)
        if start != -1:
            # Find matching closing delimiter
            end = text.find(delim, start + len(delim))
            if end != -1:  # If we found a complete pair
                if start < earliest_position:
                    earliest_position = start
                    first_complete_delimiter = delim

    return first_complete_delimiter




