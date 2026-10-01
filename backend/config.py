import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MONGODB_URI = os.getenv("MONGODB_URI")

LANGSMITH_TRACING = os.getenv("LANGSMITH_TRACING", "false")
LANGSMITH_API_KEY = os.getenv("LANGSMITH_API_KEY")
LANGSMITH_PROJECT = os.getenv("LANGSMITH_PROJECT", "callcart-ai")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY is missing in .env")

if not MONGODB_URI:
    raise ValueError("MONGODB_URI is missing in .env")