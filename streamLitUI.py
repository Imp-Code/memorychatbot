import streamlit as st

from langchain_google_genai import GoogleGenerativeAI
Api_Key = "AIzaSyC8OJrvD6yG0tTOlFuxu8wO5omSSfZuzKM"
LLM = GoogleGenerativeAI(google_api_key=Api_Key, model="gemini-2.0-flash")

st.title("COOL AI 123")

st.write("Enter an ai prompt")

st.write("")

from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

Memory = ConversationBufferMemory()

# Check if 'conversation' is NOT in the session state
if 'conversation' not in st.session_state:
    # If it's not there, create it for the first time.
    # This code will only run ONCE per user session.
    st.session_state.conversation = ConversationChain(
        llm=LLM,
        memory=ConversationBufferMemory()
    )
prompt = st.text_input("Enter your prompt")


template = f"""
This is a chatbot specifically designed to help sarosh eat his homework,
with precise and accurate answers,
that are swift to read.
ADDRESS ME AS SIR.
answer to the following question {prompt}
"""

if st.button("Search"):
    response = st.session_state.conversation.predict(input = prompt) 
    st.write(response)
