from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="zai-org/GLM-5.3-Flash",
    temperature=0.5
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("hiiii!!! how are you?")