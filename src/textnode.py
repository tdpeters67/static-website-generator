text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"


class TextNode:
    def __init__(self, text, text_type, url):
        self.text = text
        self.text_type = text_type
        self.url = url
    def __eg__(self, node):
        return (
            node.text == self.text 
            and node.text_type == self.text_type 
            and node.url == self.url)  
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"