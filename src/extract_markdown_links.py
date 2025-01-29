import re

def extract_markdown_links(text):
    link_pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(link_pattern, text)
    
    if not matches:
        raise Exception("No valid markdown links found")
    
    return matches