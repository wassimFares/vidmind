# VidMind 🧠
> Ask anything about a YouTube video using AI

VidMind is a RAG (Retrieval-Augmented Generation) pipeline that lets you ask natural language questions about any YouTube video. Paste a link, ask a question, get an accurate answer grounded in the video's transcript.

## How It Works

```
YouTube URL → Transcript → Chunks → Embeddings → FAISS Index
                                                       ↓
                                          Query → Search → LLM → Answer
```

1. Fetches the video transcript
2. Splits it into sentence-based chunks
3. Embeds chunks using `all-MiniLM-L6-v2`
4. Stores vectors in a FAISS index
5. Embeds the user query and retrieves the most relevant chunks
6. Passes chunks to an LLM to generate a grounded answer

## Tech Stack

- **Embeddings:** `sentence-transformers` (all-MiniLM-L6-v2)
- **Vector Search:** FAISS
- **LLM:** LLaMA 3.3 70B via Groq
- **Transcript:** `youtube-transcript-api`
- **UI:** Streamlit

## Setup

**1. Clone the repo**
```bash
git clone https://github.com/wassimFares/vidmind.git
cd vidmind
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Add your Groq API key**

Create a `.env` file:
```
GROQ_API_KEY=your_key_here
```

Get a free key at [console.groq.com](https://console.groq.com)

**4. Run**
```bash
streamlit run app.py
```

## Usage

1. Paste a YouTube URL (supports `youtube.com` and `youtu.be` links)
2. Type your question
3. Get an answer based on what was actually said in the video

## Project Structure

```
vidmind/
    app.py              # Streamlit UI
    chunking.py         # Sentence-based text chunking
    embeddings.py       # Sentence transformer embeddings
    vector_store.py     # FAISS index creation and search
    youtube_utils.py    # Transcript fetching and URL parsing
    llm.py              # Groq LLM integration
    requirements.txt
```
