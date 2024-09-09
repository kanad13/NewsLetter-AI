import os
import vertexai
from vertexai.generative_models import GenerationConfig, GenerativeModel, HarmBlockThreshold, HarmCategory
from typing import List
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from pypdf import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import json
import logging
from dotenv import load_dotenv
import streamlit as st
import hashlib
import time

# I have loaded environment variables here to keep sensitive information secure and flexible across different environments. This is to be used primarily when running on local machine.
load_dotenv()

# I have set up logging here to track the application's execution and help debug issues, crucial for production monitoring.
logging.basicConfig(level=logging.INFO)

# Here I have initialized Vertex AI with credentials from environment variables, enabling access to Google Cloud resources.
PROJECT_ID = os.environ.get("GCP_PROJECT")
LOCATION = os.environ.get("GCP_REGION")
vertexai.init(project=PROJECT_ID, location=LOCATION)

# I have loaded a pre-trained sentence transformer model to generate text embeddings.
# The 'all-mpnet-base-v2' model offers a good balance between performance and accuracy.
# This model is crucial for converting text to vector representations for similarity search.
model_name = 'all-mpnet-base-v2'
model = SentenceTransformer(model_name)

@st.cache_resource
def load_models():
    """Load Gemini 1.5 Flash and Pro models for generating content."""
    # Caching ensures models are loaded once and reused, boosting performance.
    # https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/inference#supported-models
    return GenerativeModel("gemini-1.5-flash-001"), GenerativeModel("gemini-1.5-pro-001")

def get_gemini_response(model, contents, generation_config=None, stream=False):
    """Generate a response from the specified Gemini model."""
    # Default configuration setup for response generation, ensuring controlled output.
    if generation_config is None:
        generation_config = GenerationConfig(temperature=0.7, max_output_tokens=1024)

    # Here I have defined safety settings to handle harmful content.
    # https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/inference#request
    safety_settings = {
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_ONLY_HIGH,
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_ONLY_HIGH,
        HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_ONLY_HIGH,
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_ONLY_HIGH,
    }

    responses = model.generate_content(
        contents,
        generation_config=generation_config,
        safety_settings=safety_settings,
        stream=stream,
    )

    # I have handled both streaming and batch responses to accommodate different use cases.
    if not stream:
        return responses.text

    final_response = []
    for r in responses:
        try:
            final_response.append(r.text)
        except IndexError:
            final_response.append("")
    return " ".join(final_response)

def extract_text_from_pdf(pdf_path):
    # I have extracted text from PDF files to facilitate text-based searches and analysis.
    # This enables the system to handle diverse document formats.
    with open(pdf_path, 'rb') as file:
        reader = PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text() + '\n'
    return text

def create_chunks(text, chunk_size=1000, chunk_overlap=200):
    # Here I have split long texts into manageable chunks, ensuring they fit within model token limits.
    # Overlapping chunks preserve context for improved retrieval accuracy.
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
    )
    chunks = text_splitter.split_text(text)
    return chunks

def get_files_hash(directory):
    # I have used a hashing mechanism to detect changes in input files.
    # This approach ensures the knowledge base stays current without unnecessary reprocessing.
    hash_md5 = hashlib.md5()
    for filename in sorted(os.listdir(directory)):
        if filename.endswith('.pdf'):
            with open(os.path.join(directory, filename), "rb") as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    hash_md5.update(chunk)
    return hash_md5.hexdigest()

@st.cache_data
def process_pdfs(_hash=None):
    # Caching helps avoid reprocessing PDFs on every run, significantly boosting performance for repeated queries.
    pdf_directory = './input_files/'
    current_hash = get_files_hash(pdf_directory)

    # I have set up cache clearance when input files change, ensuring data accuracy and relevance.
    if _hash is not None and _hash != current_hash:
        st.cache_data.clear()
        st.cache_resource.clear()  # Clear the FAISS index cache

    all_chunks = []
    chunk_to_doc = {}
    for filename in os.listdir(pdf_directory):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(pdf_directory, filename)
            text = extract_text_from_pdf(pdf_path)
            chunks = create_chunks(text)
            all_chunks.extend(chunks)
            for chunk in chunks:
                chunk_to_doc[chunk] = filename

    # Logging the chunking process helps in debugging and monitoring stages.
    logging.info(f"Total chunks: {len(all_chunks)}")
    logging.info(f"Sample chunk: {all_chunks[0][:100]}...")

    return all_chunks, chunk_to_doc, current_hash

# I have deployed FAISS for efficient similarity search, which is critical for retrieving relevant text rapidly.
@st.cache_resource
def create_faiss_index(all_chunks, _hash=None):
    # The _hash parameter is used to invalidate the cache when files change
    embeddings = model.encode(all_chunks)
    dimension = embeddings.shape[1]
    num_chunks = len(all_chunks)

    # Selecting index type dynamically optimizes search performance based on dataset size.
    if num_chunks < 100:
        logging.info("Using FlatL2 index due to small number of chunks")
        index = faiss.IndexFlatL2(dimension)
    else:
        logging.info("Using IVFFlat index")
        n_clusters = min(int(np.sqrt(num_chunks)), 100)
        quantizer = faiss.IndexFlatL2(dimension)
        index = faiss.IndexIVFFlat(quantizer, dimension, n_clusters)
        index.train(embeddings.astype('float32'))

    index.add(embeddings.astype('float32'))
    return index

# I have initialized a cache system for storing query results, ensuring faster response times for repeat queries.
cache_file = 'semantic_cache.json'

def load_cache():
    # Here I have loaded the cache from a file to maintain session state, which aids system efficiency over time.
    try:
        with open(cache_file, 'r') as f:
            cache = json.load(f)
            # Resetting the cache if the embedding model changes ensures data consistency.
            if cache.get('model_name') != model_name:
                logging.info("Embedding model changed. Resetting cache.")
                return {"queries": [], "embeddings": [], "responses": [], "model_name": model_name}
            return cache
    except FileNotFoundError:
        return {"queries": [], "embeddings": [], "responses": [], "model_name": model_name}

def save_cache(cache):
    # Regularly saving the cache prevents loss of valuable precomputed results, enhancing reliability.
    with open(cache_file, 'w') as f:
        json.dump(cache, f)

cache = load_cache()

def retrieve_from_cache(query_embedding, threshold=0.5):
    # I have used semantic caching to repurpose results for similar queries, reducing API calls and improving efficiency.
    for i, cached_embedding in enumerate(cache['embeddings']):
        if len(cached_embedding) != len(query_embedding):
            logging.warning("Cached embedding dimension mismatch. Skipping cache entry.")
            continue
        distance = np.linalg.norm(query_embedding - np.array(cached_embedding))
        if distance < threshold:
            return cache['responses'][i]
    return None

def update_cache(query, query_embedding, response):
    # Adding new queries to the cache continually improves response times as more data is accumulated.
    cache['queries'].append(query)
    cache['embeddings'].append(query_embedding.tolist())
    cache['responses'].append(response)
    cache['model_name'] = model_name
    save_cache(cache)

def retrieve_relevant_chunks(query, index, all_chunks, top_k=10):
    # Using vector similarity, I identify the most relevant chunks, which provides superior context recognition than mere keyword matching.
    query_vector = model.encode([query])[0]

    cached_response = retrieve_from_cache(query_vector)
    if cached_response:
        logging.info("Answer recovered from Cache.")
        return cached_response

    # Ensuring top_k doesn't exceed available chunks prevents errors during retrieval.
    top_k = min(top_k, len(all_chunks))
    D, I = index.search(np.array([query_vector]).astype('float32'), top_k)
    relevant_chunks = [all_chunks[i] for i in I[0]]

    update_cache(query, query_vector, relevant_chunks)
    return relevant_chunks

def generate_response(query: str, relevant_chunks: List[str], model: GenerativeModel, max_retries: int = 3):
    # I have employed a language model to generate responses, leveraging context from retrieved chunks to ensure natural language delivery.
    context = "\n".join(relevant_chunks)
    prompt = f"""Based on the following context, please answer the question. If the answer is not fully contained in the context, provide the most relevant information available and indicate any uncertainty.

Context:
{context}

Question: {query}

Answer:"""

    generation_config = GenerationConfig(temperature=0.7, max_output_tokens=1024)

    for attempt in range(max_retries):
        try:
            response = get_gemini_response(model, prompt, generation_config, stream=False)
            return response, relevant_chunks
        except Exception as e:
            logging.error(f"Error occurred: {str(e)}")
            if attempt == max_retries - 1:
                raise e
            time.sleep(5)

    raise Exception("Failed to generate response after maximum retries.")

def rag_query(query: str, index, all_chunks, chunk_to_doc, model: GenerativeModel, top_k: int = 10) -> tuple:
    # This function orchestrates retrieval and generation, ensuring well-informed, coherent user responses.
    relevant_chunks = retrieve_relevant_chunks(query, index, all_chunks, top_k)
    response, used_chunks = generate_response(query, relevant_chunks, model)

    source_docs = {}
    for chunk in used_chunks:
        doc_name = chunk_to_doc.get(chunk, "Unknown Source")
        if doc_name not in source_docs:
            source_docs[doc_name] = []
        source_docs[doc_name].append(chunk)

    return response, source_docs

# I have configured the Streamlit app, utilizing it for a rapid-prototyping-friendly and deployable user interface.
st.set_page_config(page_title="NewsLetter.AI", page_icon=":soccer:", layout="wide", initial_sidebar_state="expanded", menu_items=None)

def main():
    st.write("Search about desired topics within the newsletters:")

    # Processing PDFs and creating the index at application start ensures users interact with updated data immediately.
    all_chunks, chunk_to_doc, current_hash = process_pdfs()
    index = create_faiss_index(all_chunks, _hash=current_hash)  # Pass the hash to create_faiss_index
    gemini_15_flash, gemini_15_pro = load_models()

    # Default questions are provided to guide users and showcase system functionality.
    default_questions = [
        "Select a question",
        "what is the UltraFiber 2.0 service?",
        "current month's customer satisfaction scores",
        "who won 'employee of month'?",
        "Back-to-School Bonanza promotion status",
        "latest technology news",
        "any new trainings or learnings planned?",
        "Other (Type your own question)"
    ]

    # Here I have used a dropdown for user-friendliness while allowing custom queries for flexibility.
    selected_question = st.selectbox("Choose a question or select 'Other' to type your own:", default_questions)

    if selected_question == "Other (Type your own question)":
        user_query = st.text_input("Enter your question:")
    elif selected_question != "Select a question":
        user_query = selected_question
    else:
        user_query = ""

    selected_model = st.radio(
        "Select Gemini Model:",
        [gemini_15_flash, gemini_15_pro],
        format_func=lambda x: x._model_name.replace("publishers/google/models/", ""),
        horizontal=True,
    )

    if st.button("Get Answer"):
        if user_query and user_query != "Select a question":
            with st.spinner("Generating answer..."):
                # Re-checking PDF changes ensures responses rely on the latest data.
                all_chunks, chunk_to_doc, _ = process_pdfs(current_hash)
                index = create_faiss_index(all_chunks)
                response, source_docs = rag_query(user_query, index, all_chunks, chunk_to_doc, selected_model)

            # Displaying responses, sources, and usage data promotes transparency with users.
            st.subheader("Answer:")
            st.write(response)

            st.subheader("Source Documents:")
            for doc_name, chunks in source_docs.items():
                with st.expander(f"This is the text used from {doc_name}"):
                    for chunk in chunks:
                        st.markdown(chunk)

        else:
            st.warning("Please select a question or enter your own.")

if __name__ == "__main__":
    main()
