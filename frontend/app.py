import streamlit as st
import httpx
import os

API_URL = os.getenv("API_URL", "http://localhost:8000/rag/query")

def layout():
    # OBS: Vi kan ändra "RAGnimals" till vad ert projekt faktiskt handlar om!
    st.markdown("# RAGnimals")
    st.markdown("Ask a question about different animals")

    text_input = st.text_input(label="ask a question")

    if st.button("send") and text_input.strip() != "":

        response = httpx.post(API_URL, json={"prompt": text_input}, timeout=120)
        data = response.json()

        st.markdown("## Question:")
        st.markdown(text_input)

        st.markdown("## Answer:")
        st.markdown(data["answer"])

        st.markdown("## Source:")
        st.markdown(data["filepath"])

if __name__ == "__main__":
    layout()