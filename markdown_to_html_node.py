class HTMLNode:
    def __init__(self, tag, children=None, text=""):
        self.tag = tag
        self.children = children if children else []
        self.text = text

    def __repr__(self):
        return f"<{self.tag}>{self.text}{''.join(map(str, self.children))}</{self.tag}>"

def markdown_to_html_node(markdown):
    """Converts a full markdown document into a single parent HTMLNode."""
    
    blocks = split_into_blocks(markdown)  # Assuming you have this function
    parent_node = HTMLNode("div")

    for block in blocks:
        block_type = determine_block_type(block)  # Assuming you have this function
        
        if block_type == "code":
            node = HTMLNode("pre", [text_node_to_html_node(block)])  # No inline parsing
        else:
            node = HTMLNode(block_type, text_to_children(block))  # Inline markdown processing

        parent_node.children.append(node)

    return parent_node
