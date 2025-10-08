
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
chain = prompt1 | model | parser

# Answer input
answer = st.text_input("✍️ Write your answer here")

# Generate question
if st.button('🧪 Generate Question'):
    result = chain.invoke({'subject': subject, 'difficulty_level': difficulty_level})
    parsed_result = parser_py.parse(result)

    # Display results in styled blocks
    st.markdown("### 🧠 Difficulty Level")
    st.success(parsed_result.difficulty)

    st.markdown("### ❓ Question")
    st.info(parsed_result.Question)

    if parsed_result.Input:
        st.markdown("### 📥 Input")
        st.code(parsed_result.Input, language='python')

    if parsed_result.Output:
        st.markdown("### 📤 Expected Output")
        st.code(parsed_result.Output, language='python')

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray;'>"
    "© 2025 Python Practice App | Built by Anindya Sarkar"
    "</div>",
    unsafe_allow_html=True
)
