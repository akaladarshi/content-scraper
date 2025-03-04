import re


def clean_text(self, text):
    """
    Cleans and normalizes text by:
    - Removing extra spaces and newlines
    - Removing HTML tags if any remain
    """
    # Remove HTML tags (if any)
    cleaned = re.sub(r"<.*?>", "", text)
    # Remove extra whitespace
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    return cleaned