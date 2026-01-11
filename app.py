import streamlit as st
from gemini_utils import explain_tradeoffs, check_key
from config import REQUIREMENTS

# Page setup - wide layout
st.set_page_config(page_title="Why-Choose Referee AI", layout="wide")

st.title("Why-Choose Referee AI")

# System Status at the top
api_status = check_key()
st.info(f"🔑 System Status: {api_status}")

st.write("Fill out any one category below to compare two options side-by-side.")

# Three column layout with paired inputs
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("AWS/Jobs")
    job_a = st.text_input("Job Position A", key="job_a")
    job_b = st.text_input("Job Position B", key="job_b")

with col2:
    st.subheader("Software/Hardware")
    software_a = st.text_input("Software/Hardware A", key="software_a")
    software_b = st.text_input("Software/Hardware B", key="software_b")

with col3:
    st.subheader("Products")
    product_a = st.text_input("Product A", key="product_a")
    product_b = st.text_input("Product B", key="product_b")

# Centered compare button
st.markdown("<br>", unsafe_allow_html=True)  # Add some spacing
col_center = st.columns([1, 1, 1])
with col_center[1]:
    compare_button = st.button("Compare Everything", use_container_width=True)

# Analysis logic
if compare_button:
    # Find the first category with both inputs filled (process only one at a time)
    comparison_made = False
    
    if job_a.strip() and job_b.strip() and not comparison_made:
        with st.spinner("Generating job position trade-off analysis..."):
            result = explain_tradeoffs(job_a, job_b, "career prospects and job benefits")
            st.subheader(f"Job Position Analysis: {job_a} vs {job_b}")
            st.markdown(result)
            comparison_made = True
    
    elif software_a.strip() and software_b.strip() and not comparison_made:
        with st.spinner("Generating software/hardware trade-off analysis..."):
            result = explain_tradeoffs(software_a, software_b, "performance and usability")
            st.subheader(f"Software/Hardware Analysis: {software_a} vs {software_b}")
            st.markdown(result)
            comparison_made = True
    
    elif product_a.strip() and product_b.strip() and not comparison_made:
        with st.spinner("Generating product trade-off analysis..."):
            result = explain_tradeoffs(product_a, product_b, "value and features")
            st.subheader(f"Product Analysis: {product_a} vs {product_b}")
            st.markdown(result)
            comparison_made = True
    
    if not comparison_made:
        st.error("Please fill in both options for at least one category to compare.")
    elif job_a.strip() and job_b.strip() and software_a.strip() and software_b.strip():
        st.info("💡 Tip: Only one comparison processed at a time to avoid rate limits. Clear other fields or click again for additional comparisons.")