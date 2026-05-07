import streamlit as st
import httpx
import os

API_URL = os.getenv("API_URL", "http://localhost:8000/rag/query")

def layout():
    st.markdown("#  Study buddy with LLM")
    st.markdown("Ask a question about LLM projects and get an answer!")

    text_input = st.text_input(label="Ask a question")

    if st.button("send") and text_input.strip() != "":

        try:

            with st.spinner("Thinking..."):
                response = httpx.post(API_URL, json={"prompt": text_input}, timeout=300)
                response.raise_for_status()
                data = response.json()

            st.markdown("## Question:")
            st.markdown(text_input)

            st.markdown("## Answer:")
            st.markdown(data["answer"])

            st.markdown("## Source:")
            st.markdown(data["filepath"])
        except httpx.ReadTimeout:
            st.error("⏳ The request took too long. Try a simpler question.")

        except httpx.RequestError:
            st.error("⚠️ Cannot connect to the backend. Is your server running?")

        except Exception as e:
            st.error(f"❌ Unexpected error: {str(e)}")



if __name__ == "__main__":
    layout()
