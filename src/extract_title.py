import re

def extract_title(markdown):
    """Extracts the first H1 header from markdown."""
    for line in markdown.split("\n"):
        if line.strip().startswith("# "):
            return line.strip()[2:].strip()  # Remove `#` and leading/trailing whitespace
    raise ValueError("No H1 header found in the markdown")
