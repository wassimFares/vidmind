
import streamlit as st
from youtube_utils import get_transcript
from chunking import chunk_text
from vector_store import create_index, search
from llm import ask

st.set_page_config(
    page_title="VidMind",
    page_icon="🧠"
)

with st.spinner("Loading model..."):
    from embeddings import create_embeddings, embed_query

st.title("VidMind 🧠")
st.caption("Ask anything about a YouTube video")

video_url = st.text_input("YouTube URL")
query = st.text_input("Your question")

if video_url and query:
    with st.spinner("Thinking..."):
        try:
            transcript = get_transcript(video_url)
        except ValueError as e:
            st.error(str(e))
            st.stop()
        except Exception:
            st.error("Something went wrong. Please check the URL and try again.")
            st.stop()
        chunks = chunk_text(transcript)
        vectors = create_embeddings(chunks)
        index = create_index(vectors)
        matched_chunks = search(index, chunks, embed_query(query))
        answer = ask(query, matched_chunks)
    st.write(answer)