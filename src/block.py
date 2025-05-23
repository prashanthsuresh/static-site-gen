from enum import Enum

class BlockType(Enum):
    HEADING = "heading"
    CODE_BLOCK = "code_block"
    QUOTE_BLOCK = "quote_block"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"
    PARAGRAPH = "paragraph"

def block_to_block_type(block: str) -> BlockType:
    lines = block.split("\n")

    if block.startswith("#") and block.lstrip("#").startswith(" "):
        return BlockType.HEADING

    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE_BLOCK

    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE_BLOCK

    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST

    if all(line.startswith(f"{i}. ") for i, line in enumerate(lines, start=1)):
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH
