import streamlit as st
from summarizer import summarize_text

st.title("📝 AI Text Summarizer")
st.write("Paste any long text below and click 'Summarize'")

user_input = st.text_area("Enter your text here:", height=300)

if st.button("Summarize"):
    if user_input:
        summary = summarize_text(user_input)
        st.subheader("Summary")
        st.success(summary)
    else:
        st.warning("Please enter some text first.")
