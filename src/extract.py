import re
import unittest

def extract_markdown_images(text):
    """Extracts markdown images from text, returning a list of tuples (alt text, URL)."""
    pattern = r'!\[([^\]]+)\]\((https?://[^\)]+)\)'
    return re.findall(pattern, text)

def extract_markdown_links(text):
    """Extracts markdown links from text, returning a list of tuples (anchor text, URL)."""
    pattern = r'\[([^\]]+)\]\((https?://[^\)]+)\)'
    return re.findall(pattern, text)
