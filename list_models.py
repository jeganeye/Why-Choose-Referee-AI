from dotenv import load_dotenv
import os
from google import genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if api_key:
    client = genai.Client(api_key=api_key)
    
    try:
        models = client.models.list()
        print("Available models:")
        for model in models:
            print(f"- {model.name}")
    except Exception as e:
        print(f"ERROR: {e}")
else:
    print("No API key found")