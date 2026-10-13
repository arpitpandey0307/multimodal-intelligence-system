import langchain
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()
print(langchain.__version__)

model = ChatGroq(model="openai/gpt-oss-20b")
result = model.invoke("What is the capital of India?")
print(result.content)