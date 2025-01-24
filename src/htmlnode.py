class HTMLNode:

    left_and_right = ["h1", "h2", "h3", "h4", "h5", "h6", "p", "b", "i", "code", "li"]
    #self_closing = ["img"]
    container = ["ul", "ol"]
    block = ["blockquote"]
    #link = ["a"]


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
    def __init__(self, tag=None, value=None, props: dict =None):
        
        # Accounts for nodes that are created with only a value eg. raw text
        if value is None and tag is not None and props is None:
            value = tag
            tag = None

        # For image tags, ensure necessary attributes exist
        if tag == "img":
            if props is None or "src" not in props or "alt" not in props:
                raise ValueError("Image nodes must have 'src' and 'alt' attributes")
            # Treat `alt` as the value for consistency of args across different node types
            value = props["alt"]

        if tag == "a":
            if props is None or "href" not in props:
                raise ValueError("Link nodes must have 'href' attribute")
        
        if value is None:
            raise ValueError("LeafNode type requires a non-optional 'value' argument")
        
        super().__init__(tag=tag, value=value, props=props)
    
    def to_html(self):
        print(f"[DEBUG: LeafNode to_html] tag: {self.tag}, value: {self.value}, props: {self.props}")
        if self.value is None:
            raise ValueError
        
        if self.tag is None:
            return self.value
        
        else:
            
                if self.tag in HTMLNode.left_and_right:
                    return f"<{self.tag}>{self.value}</{self.tag}>"
                
                elif self.tag == "a" and self.props is not None:
                    props_keys = list(self.props.keys())
                    props_values = list(self.props.values())

                    return f'<a {props_keys[0]}="{props_values[0]}>{self.value}</a>'
                
                elif self.tag == "img":
                    return f'<img src="{self.props["src"]}" alt="{self.value}">'


                #elif self.tag in HTMLNode.container:
                
                else:
                    raise Exception("Unhandled case")
                
    def __repr__(self):
        return f"LeafNode(Tag = {self.tag}, Value = {self.value}, Props = {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children: list, props: dict = None):

        if children is None or len(children) == 0:
            raise ValueError("ParentNode must have at least one child.")
        
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        print(f"[DEBUG: ParentNode to_html] tag: {self.tag}, children: {self.children}, props: {self.props}")
        html_string = f"<{self.tag}>"

        if self.tag is None:
            raise ValueError("ParentNode must have at least one tag")
        
        if self.children is None or len(self.children) == 0:
            raise ValueError("ParentNode must have at least one child.")

        for child in self.children:
            html_string += child.to_html()

        return html_string + f"</{self.tag}>"
        
    def __repr__(self):
        return f"ParentNode(Tag = {self.tag}, Children = \n{self.children}), Props = {self.props})"