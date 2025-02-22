from enum import Enum

class TextType(Enum):
    TEXT = "Normal text"
    BOLD = "Bold text"
    ITALIC = "Italic text"
    CODE = "Code text"
    LINK = "Link"
    IMAGE = "Image"

class TextNode:
    def __init__(self, text, text_type: TextType, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if (self.text == other.text and 
            self.text_type == other.text_type and 
            self.url == other.url):
            return True
        
        
    def __repr__(self):
        return f"TextNode(Text = {self.text}, TextType = {self.text_type.value}, URL = {self.url})"