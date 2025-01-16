class HTMLNode:

    left_and_right = ["h1", "h2", "h3", "h4", "h5", "h6", "p", "b", "i", "code", "li"]
    self_closing = ["img"]
    container = ["ul", "ol"]
    block = ["blockquote"]
    link = ["a"]


    '''
    tag - A string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
    value - A string representing the value of the HTML tag (e.g. the text inside a paragraph)
    children - A list of HTMLNode objects representing the children of this node
    props - A dictionary of key-value pairs representing the attributes of the HTML tag. For example, a link (<a> tag) might have {"href": "https://www.google.com"}

    
    An HTMLNode without a tag will just render as raw text
    An HTMLNode without a value will be assumed to have children
    An HTMLNode without children will be assumed to have a value
    An HTMLNode without props simply won't have any attributes

    '''

    def __init__(self, tag=None, value=None, children=None, props: dict =None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __eq__(self, other):
        if (self.tag == other.tag and 
            self.value == other.value and 
            self.children == other.children and
            self.props == other.props):
            return True
    
    def to_html(self):
        raise NotImplemented
    
    def props_to_html(self):
        atb_string = ""

        if self.props is None:
            return ""
        
        for key, value in self.props.items():
            atb_string += f'{key}="{value}" '
        
        return " " + atb_string.rstrip(" ")
    
    def __repr__(self):
        return f"HTMLNode(Tag = {self.tag}, Value = {self.value}, \nChildren = {self.children}\n, Props = {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props: dict =None):
        super().__init__(tag=tag, value=value, props=props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError
        
        if self.tag is None:
            return self.value
        
        else:
            
                if self.tag in HTMLNode.left_and_right:
                    return f"<{self.tag}>{self.value}</{self.tag}>"
                
                elif self.tag in HTMLNode.link and self.props is not None:
                    props_keys = list(self.props.keys())
                    props_values = list(self.props.values())

                    return f'<a {props_keys[0]}="{props_values[0]}>{self.value}</a>'
                
                else:
                    raise Exception("Unhandled case")
                
    def __repr__(self):
        return f"LeafNode(Tag = {self.tag}, Value = {self.value}, Props = {self.props})"
        
