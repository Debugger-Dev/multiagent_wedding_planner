from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

gemini_model = ChatGroq(
    model="qwen/qwen3.8-27b",
    temperature=0.7,api_key = os.getenv("GEMINI_API_KEY")
)

