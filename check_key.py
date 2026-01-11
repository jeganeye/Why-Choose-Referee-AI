# app.py
import streamlit as st
from utils import explain_tradeoffs, check_key
from config import REQUIREMENTS

# -----------------------------
# Page setup
# -----------------------------
st.set_page_config(page_title="Why-Choose Referee AI", layout="centered")

# Title and description
st.title("Why-Choose Referee AI")
st.write(
    "This tool uses AI to explain the **trade-offs** between any two choices "
    "based on your selected requirement."
)

# -----------------------------
# Sidebar: API key status
# -----------------------------
st.sidebar.header("API Key Status")
api_status = check_key()
st.sidebar.info(api_status)

# -----------------------------
# User inputs
# -----------------------------
option_a = st.text_input("Option A")
option_b = st.text_input("Option B")
requirement = st.selectbox("Select your requirement", REQUIREMENTS)

# -----------------------------
# Trigger AI analysis
# -----------------------------
if st.button("Analyze Trade-offs"):
    if option_a and option_b and requirement:
        with st.spinner("Generating trade-off analysis..."):
            result = explain_tradeoffs(option_a, option_b, requirement)
            st.subheader(f"Trade-off Analysis for '{requirement}'")
            st.write(result)
    else:
        st.error("Please fill in Option A, Option B, and the requirement.")
