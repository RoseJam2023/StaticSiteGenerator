class HTMLNode:

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

        if self.props == None:
            return ""
        
        for key, value in self.props.items():
            atb_string += f'{key}="{value}" '
        
        return " " + atb_string.rstrip(" ")
    
    def __repr__(self):
        return f"HTMLNode(Tag = {self.tag}, Value = {self.value}, \nChildren = {self.children}\n, Props = {self.props})"