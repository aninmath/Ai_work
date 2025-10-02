from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
# from langchain_core.prompts import PromptTemplate, load_prompt


load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')


history= [
    SystemMessage(content= "you are a chatbot who talks like chandler bing in friend, but keep it short, crips")
]

while True:
    user_input= input("you: ")
    history.append(HumanMessage(content=user_input))
    if user_input == 'exit':
        break
    result = model.invoke(history)
    history.append(AIMessage(content=result.content))

    print("AI:" , result.content)
