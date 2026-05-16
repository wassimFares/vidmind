from groq import Groq
import os
from dotenv import load_dotenv
load_dotenv()

client = Groq(api_key=os.getenv('GROQ_API_KEY'))

def ask(query, matched_chunks):
    print("started ask function")
    context = "\n\n".join(matched_chunks)
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are an AI assistant that answers questions about YouTube videos. Answer based only on the provided video content. If the answer is not in the video, say so naturally. Never use words like 'transcript', 'context', or 'document' in your response — speak as if you watched the video yourself."},
            {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {query}"}
        ]
    )
    return response.choices[0].message.content