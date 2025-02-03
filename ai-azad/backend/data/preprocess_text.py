import re

def preprocess_text(text):
    # Remove noise
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^\w\s]', '', text)
    return text