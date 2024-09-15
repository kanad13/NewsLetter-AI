import streamlit as st

config = {'scrollZoom': True, 'displayModeBar': True, 'displaylogo': False}
st.set_page_config(page_title="NewsLetter.AI", page_icon=":chat-plus-outline:", layout="wide", initial_sidebar_state="expanded", menu_items=None)

st.write("""
## Newsletter.AI

Company newsletters can flood employees with too much information every week.

It is hard to read everything or find past newsletters.

A tool that lets employees "chat" with current and past newsletters would be really helpful.

#### Generative AI for NewsLetters

Newsletter.AI lets you easily chat with past and present newsletters using AI:

- Ask questions and get straightforward answers.
- Find important info even if you do not use exact words.

Just type your question, and Newsletter.AI pulls the info from the newsletters for you.

#### Navigation

Click on the sidebar to interact with Newsletter.AI chatbot. \n

#### Technology

Newsletter.AI uses three key technologies:

1. Retrieval-Augmented Generation (RAG)
2. Large Language Models (LLMs)
3. Google Cloud  (Cloud Run, Cloud Build and Vertex AI)

For detailed technology deep-dive, check out the [github repo](https://github.com/kanad13/NewsLetter-AI).
				 """)
st.image("./assets/newsletter-workflow.png")
