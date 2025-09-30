from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

# result = model.invoke('What is the capital of India')

# print(result.content)

import streamlit as st
st.title("My Joke app")

# prm = st.text_input("## Give your prompt")

joke_type = st.selectbox("select joke type",['adult','dad joke','nerdy','political'])
language_type = st.selectbox ('select language', ['english', 'hindi', 'bengali'])

#
from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    
    input_variables=["joke_type", "language_type"],
    template="""
        You are a witty joke generator.

        Generate a {joke_type} joke in {language_type}.

        Make sure the joke is short, funny, and hilarious...sarcastic.
        """
        )

prm = template.invoke({
    'joke_type' : joke_type,
    'language_type' : language_type,
})


if st.button("check"):
    result = model.invoke(prm)
    st.write(result.content)
