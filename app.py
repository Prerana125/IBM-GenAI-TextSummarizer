import streamlit as st
import cohere
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
cohere_api_key = os.getenv("DZJ7lBAZanbfVjbYS1kcdm6alEizoO1gw6Yt6SgU")

# Initialize Cohere client
co = cohere.Client(cohere_api_key)

# Streamlit UI
st.set_page_config(page_title="Text Summarizer with Cohere", layout="centered")
st.title("📝 Cohere AI Text Summarizer")

text = st.text_area("Enter text to summarize", height=200)

if st.button("Summarize"):
    if not text.strip():
        st.warning("Please enter some text to summarize.")
    else:
        with st.spinner("Summarizing..."):
            try:
                response = co.summarize(
                    text=text,
                    length='medium',       # other options: 'short', 'long'
                    format='paragraph',    # or 'bullets'
                    model='summarize-xlarge'  # or 'command-xlarge' for broader use
                )
                summary = response.summary
                st.success("Summary:")
                st.write(summary)
            except Exception as e:
                st.error(f"Error: {e}")
