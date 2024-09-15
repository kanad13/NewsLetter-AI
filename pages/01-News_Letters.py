import streamlit as st

config = {'scrollZoom': True, 'displayModeBar': True, 'displaylogo': False}
st.set_page_config(page_title="News Letters", page_icon=":chat-plus-outline:", layout="wide", initial_sidebar_state="expanded", menu_items=None)
st.write("""
### Sample Documents for NewsLetter.AI

To showcase how NewsLetter.AI works with Generative AI on custom documents, I created fictional NewsLetters for 4 departments viz. Sales, Networks, COPS & IT.

The chatbot answers questions based on these newsletters.\n

So for example, if an employee wants to know what are "current month's customer satisfaction scores", then they can just ask the chatbot that question and get the answer using the power of Generative AI.

As fresh newsletters get published or old newsletters get corrected, you just need to place them in the [input_files folder](./input_files).\n
No code changes needed to the chatbot. The chatbot starts providing answers based on latest information.\n
This is on account of the **intelligent hash-based cache management** implemented in NewsLetter.AI. You can find more details - [here](./readme.md##what-sets-newsletterai-apart)
				 """)
