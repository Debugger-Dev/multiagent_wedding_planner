from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

gemini_model = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.7,api_key = os.getenv("GEMINI_API_KEY")
)

