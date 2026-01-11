from dotenv import load_dotenv
import os

# Load .env
load_dotenv()

# Check Gemini API key
api_key = os.getenv("GEMINI_API_KEY")
if api_key:
    print("Gemini API key loaded: True")
else:
    print("Gemini API key loaded: False")
