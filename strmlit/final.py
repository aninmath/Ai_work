
import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal, Optional

# Load environment variables
load_dotenv()

# Page config
st.set_page_config(
    page_title="🐍 Python Practice App",
    page_icon="📘",
    layout="centered"
)

# Sidebar
with st.sidebar:
    st.header("🛠️ Settings")
    st.write("Choose difficulty and subject to generate a Python practice question.")
    st.markdown("---")
    st.write("Made with ❤️ using LangChain + Gemini")

# Title
st.markdown("<h1 style='text-align: center;'>🐍 Python Practice App</h1>", unsafe_allow_html=True)
st.markdown("### 🚀 Generate Python questions based on your selected topic and difficulty.")

# Select inputs
difficulty_level = st.selectbox("🎯 Select Difficulty Level", ['easy', 'medium', 'hard'])
subject = st.selectbox("📚 Select Subject", ['string manipulation', 'numpy', 'pandas', 'matplotlib', 'machine learning'])

# Model setup
model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

# Pydantic schema
class pytem(BaseModel):
    difficulty: Literal["easy", "medium", "hard"] = Field(description="Mention the difficulty level")
    Question: str = Field(description="Form the question")
    Input: Optional[str] = Field(description="Mention the input variables")
    Output: Optional[str] = Field(description="Mention the output")

parser_py = PydanticOutputParser(pydantic_object=pytem)

# Prompt for question generation
prompt1 = PromptTemplate(
    input_variables=['difficulty_level', 'subject'],
    template='Give me a Python practice question on the {subject} of difficulty level {difficulty_level}.\n{format_instruction}',
    partial_variables={'format_instruction': parser_py.get_format_instructions()}
)

# Prompt for answer checking (optional)
prompt2 = PromptTemplate(
    input_variables=['question', 'answer'],
    template='Check whether the {answer} is correct for the {question}. Mention "correct" or "wrong" based on the input.'
)

# Output parser
parser = StrOutputParser()

# Chain setup
chain = prompt1 | model | parser_py

st.button('🧪 Generate Question')

# Generate question
if st.button('🧪 Generate Question'):
    result = chain.invoke({'subject': subject, 'difficulty_level': difficulty_level})

    # Display results in styled blocks
    st.markdown("### 🧠 Difficulty Level")
    st.success(result.difficulty)

    st.markdown("### ❓ Question")
    st.info(result.Question)

    if result.Input:
        st.markdown("### 📥 Input")
        st.code(result.Input, language='python')

    if result.Output:
        st.markdown("### 📤 Expected Output")
        st.code(result.Output, language='python')




#for the second branch

class pytem2(BaseModel):
    Verdict : Literal["Correct", "Wrong"] = Field(description= "mention the Correctness of the code")
    Efficiency : int = Field (description= 'give an efficiency score out of 100 measured against the most efficient code')
    Code : Optional[str] = Field(description= "Only provide this if the verdict is Correct and efficiency is less than 100")


parser_py2 = PydanticOutputParser (pydantic_object= pytem2)


prompt2 = PromptTemplate (

    input_variable = ['question', 'answer'],
    template = 'check the  {answer} of  the question {question} and give judgement \n {format_instruction}',
    partial_variables= {'format_instruction': parser_py2.get_format_instructions()}
)



chain2 = prompt2 | model | parser_py2

# Answer input
answer = st.text_input("✍️ Write your answer here")

if st.input('🧪 Check Result'):
        result2 = chain2.invoke({'answer': answer, 'question':result.Question})
        st.markdown("### ❓ Verdict")
        st.info(result2.Verdict)










# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray;'>"
    "© 2025 Python Practice App | Built by Anindya Sarkar"
    "</div>",
    unsafe_allow_html=True
)
