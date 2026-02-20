import re

def tokenize(text, lowercase=True):
    if lowercase:
        text = text.lower()
    return re.findall(r"\b\w+\b", text)

if __name__ == "__main__":
    sample = "Hello, World! Tokenization concept in a professional way."
    print(tokenize(sample))