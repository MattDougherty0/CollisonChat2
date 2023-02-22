import json
import streamlit as st
from gpt_index import GPTSimpleVectorIndex

# Load the index from disk
index = GPTSimpleVectorIndex.load_from_disk('index-4.json')

# Define the app layout
st.title('GPT Search')
query = st.text_input('Enter a query:')
if query: 
    result = index.query(query)
    st.write(result)
