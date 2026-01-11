from dotenv import load_dotenv
import os
from google import genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if api_key:
    client = genai.Client(api_key=api_key)
    
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents="Compare Linux vs Windows in 2 sentences."
        )
        print("SUCCESS - Real Gemini Response:")
        print(response.text)
    except Exception as e:
        print(f"ERROR: {e}")
else:
    print("No API key found")