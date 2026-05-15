import re

def chunk_text(text, chunk_size=5):
    sentences = re.split(r'(?<=[.!?]) +', text)
    chunks = [" ".join(sentences[i:i+chunk_size])
              for i in range(0, len(sentences), chunk_size)]
    return chunks

