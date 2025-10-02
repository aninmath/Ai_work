from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate, load_prompt


load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')


import streamlit as st
st.title("My Joke app")


joke_type = st.selectbox("select joke type",['adult','dad joke','nerdy','political'])
language_type = st.selectbox ('select language', ['english', 'hindi', 'bengali'])

#

template = load_prompt('template.json')



if st.button("check"):
    chain = template | model
    result = chain.invoke({
    'joke_type' : joke_type,
    'language_type' : language_type,})    
    st.write(result.content)

 