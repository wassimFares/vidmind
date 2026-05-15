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
            {"role": "system", "content": "Answer questions based only on the provided video transcript context."},
            {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {query}"}
        ]
    )
    return response.choices[0].message.content