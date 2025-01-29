import re

def extract_markdown_images(text):
    # This pattern captures both alt text and URL together
    image_pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    
    # findall will return a list of tuples already!
    matches = re.findall(image_pattern, text)
    
    if not matches:
        raise Exception("No valid markdown images found")
    
    return matches