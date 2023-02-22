import json
import streamlit as st
from gpt_index import GPTSimpleVectorIndex
import os

env:
  OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
   
# Load the index from disk
index = GPTSimpleVectorIndex.load_from_disk('index.json')

# Set the API key as an environment variable
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

# Define the app layout
st.title('GPT Search')
query = st.text_input('Enter a query:')
if query: 
    result = index.query(query)
    st.write(result)
