import streamlit as st
import os
from google import genai

# 1. Securely fetch the API Key
GEMINI_API_KEY = None
try:
    if "GEMINI_API_KEY" in st.secrets:
        GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
except Exception:
    pass

if not GEMINI_API_KEY:
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError:
        pass
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# 2. Defensive Initialization
if GEMINI_API_KEY and GEMINI_API_KEY.strip():
    client = genai.Client(api_key=GEMINI_API_KEY)
else:
    client = None

def check_key():
    """Checks the status of the API key safely."""
    if client is None:
        return "API key is missing ❌. Please add it to .env file."
    try:
        # Test with Gemini 2.5 Flash
        client.models.get(model="gemini-2.5-flash")
        return "API key is valid ✅. Running on Gemini 2.5 Flash (1500+ req/day)."
    except Exception as e:
        return f"API key test failed ❌: {str(e)}"

def explain_tradeoffs(option_a: str, option_b: str, requirement: str) -> str:
    """Uses ONLY Gemini 2.5 Flash API - REAL responses only."""
    if client is None:
        return "❌ **API Client Error:** Gemini API key not found. Please check your .env file."

    prompt = (
        f"Compare '{option_a}' vs '{option_b}' focusing on '{requirement}'. "
        f"Provide a detailed analysis with comparison table, pros/cons, and recommendation. "
        f"Use markdown formatting and professional tone."
    )

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"❌ **Gemini API Error:** {str(e)}"