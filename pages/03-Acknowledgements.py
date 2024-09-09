import streamlit as st

config = {'scrollZoom': True, 'displayModeBar': True, 'displaylogo': False}
st.set_page_config(page_title="Acknowledgements", page_icon=":chat-plus-outline:", layout="wide", initial_sidebar_state="expanded", menu_items=None)
st.write("""
### Acknowledgements

NewsLetter.AI is powered by a combination of open and closed-source technologies. I am grateful for the contributions of the following initiatives and organizations:

- [Python](https://github.com/python) - The backbone of NewsLetter.AI's codebase.
- [PyPDF](https://pypdf.readthedocs.io/en/latest/index.html) - It is used for text extraction and processing from PDF documents.
- [Hugging Face](https://huggingface.co/sentence-transformers/all-mpnet-base-v2) - The `all-mpnet-base-v2` SentenceTransformer model is used to generate embeddings for semantic search.
- [Facebook](https://faiss.ai) - Facebook AI Similarity Search (FAISS) is used for performing similarity searches.
- [Langchain](https://python.langchain.com/v0.1/docs/modules/data_connection/document_transformers/recursive_text_splitter/) - This RecursiveCharacterTextSplitter is used for breaking down large text into manageable chunks, optimizing them for embedding and retrieval.
- [Google Cloud](https://cloud.google.com/) is used for deploying & hosting NewsLetter.AI. The Generative AI capabilities in NewsLetter.AI are enabled by Vertex AI.
- [Streamlit](https://streamlit.io/) - Streamlit provides the technology to build the frontend for the NewsLetter.AI chatbot.
- **The Broader AI/ML Community** - A special thanks to the AI/ML community whose ongoing research and open-source contributions have laid the foundation for this project.
""")
