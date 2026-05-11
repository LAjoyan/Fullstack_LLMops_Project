import streamlit as st
import httpx
import os
import base64
from fpdf import FPDF

# Configuration
API_URL = os.getenv("API_URL", "http://localhost:8000/rag/query")

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file, theme):
    try:
        bin_str = get_base64_of_bin_file(png_file)

        # Define CSS for both light and dark themes
        light_theme_css = f'''
        <style>
        /* General App Style */
        .stApp {{
            background-image: url("data:image/png;base64,{bin_str}");
            background-size: cover;
        }}
        /* Main content block with blur effect */
        .block-container {{
            background-color: rgba(255, 255, 255, 0.45);
            backdrop-filter: blur(8px);
            border: 1px solid rgba(255, 255, 255, 0.4);
        }}
        /* General text color */
        h1, h2, h3, span, label, p, .stMarkdown p {{
            color: #1E1E1E !important;
        }}
        /* Input box styling for light mode */
        div[data-baseweb="input"] {{
            background-color: rgba(255, 255, 255, 0.8) !important;
            border: 1px solid rgba(0, 0, 0, 0.2) !important;
        }}
        div[data-baseweb="base-input"] input {{
            color: #000000 !important;
            -webkit-text-fill-color: #000000 !important;
        }}
        </style>
        '''

        dark_theme_css = f'''
        <style>
        /* General App Style */
        .stApp {{
            background-image: url("data:image/png;base64,{bin_str}");
            background-size: cover;
        }}
        /* Main content block with blur effect */
        .block-container {{
            background-color: rgba(30, 30, 30, 0.6);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.2);
        }}
        /* General text color */
        h1, h2, h3, span, label, p, .stMarkdown p {{
            color: #FFFFFF !important;
        }}
        /* Input box styling for dark mode */
        div[data-baseweb="input"] {{
            background-color: #2E2E2E !important;
            border: 1px solid rgba(255,255,255,0.3) !important;
        }}
        div[data-baseweb="base-input"] input {{
            color: #FFFFFF !important;
            -webkit-text-fill-color: #FFFFFF !important;
        }}
        </style>
        '''

        # Select and apply the theme's CSS
        if theme == 'dark':
            st.markdown(dark_theme_css, unsafe_allow_html=True)
        else:
            st.markdown(light_theme_css, unsafe_allow_html=True)

        # Apply any other common CSS here if you refactor it out
        # For simplicity, common styles are duplicated in the strings above

    except FileNotFoundError:
        st.warning("Background image 'background.jpg' not found.")

def create_pdf(text, title="Study Material"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("helvetica", 'B', 16)
    pdf.cell(0, 10, txt=title, ln=True, align='C')
    pdf.ln(10)
    pdf.set_font("helvetica", size=11)
    clean_text = text.encode('latin-1', 'ignore').decode('latin-1')
    pdf.multi_cell(0, 10, txt=clean_text)
    return pdf.output(dest="S").encode("latin-1")

def layout():

    st.set_page_config(page_title="Study Buddy", page_icon="🎓", layout="centered")

    if 'theme' not in st.session_state:
        st.session_state.theme = 'light'  # Default to light mode

    set_background("background.jpg", st.session_state.theme)

    with st.sidebar:
        st.title("🎓 Study Tools")
        if st.session_state.theme == 'light':
            if st.button('🌙 Switch to Dark Mode'):
                st.session_state.theme = 'dark'
                st.rerun() # Use st.rerun() for newer Streamlit versions
        else:
            if st.button('☀️ Switch to Light Mode'):
                st.session_state.theme = 'light'
                st.rerun() # Use st.rerun() for newer Streamlit versions

        st.markdown("---") # Optional: adds a divider
        # --- END OF ADDED CODE BLOCK ---

        st.markdown("""
        **Subjects you can ask about:**
        - Python
        ...
        """)
        st.markdown("""
        **Subjects you can ask about:**
        - Python
        - Packaging in Python
        - Pydantic AI
        - Logistic Regression
        - LanceDB
        - Docker
        - LLM
        - Azure
        """)
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        st.caption("Powered by Streamlit, FastAPI & Pydantic AI")

    st.title("🎓 Study Buddy")
    st.markdown("Your interactive AI-powered learning assistant.")

    user_input = st.text_input("Enter your request:", placeholder="e.g. Generate a quiz about Logistic Regression")

    if st.button("🚀 Send") and user_input.strip() != "":
        try:
            with st.spinner("🧠 Thinking..."):
                response = httpx.post(f"{API_URL}/rag/query", json={"prompt": user_input}, timeout=300.0)
                response.raise_for_status()
                data = response.json()

            answer = data.get("answer", "")
            st.markdown("---")
            st.markdown("### 🤖 Response")

            if "---FACIT---" in answer:
                parts = answer.rsplit("---FACIT---", 1)
                st.markdown(parts[0].strip())
                st.balloons()
                with st.expander("🔍 Reveal Answer Key"):
                    st.success(parts[1].strip())
                pdf_data = create_pdf(answer, title="Study Quiz")
                st.download_button("📥 Download Quiz PDF", pdf_data, "quiz.pdf", "application/pdf")

            elif "Q:" in answer and "|" in answer:
                st.info("💡 Click on a question to reveal the answer!")
                for line in answer.split('\n'):
                    if "Q:" in line and "|" in line:
                        parts = line.split("|", 1)
                        if len(parts) == 2:
                            with st.expander(f"❓ {parts[0].replace('Q:', '').strip()}"):
                                st.write(parts[1].replace('A:', '').strip())
                pdf_data = create_pdf(answer.replace("|", "\n"), title="Study Flashcards")
                st.download_button("📥 Download Flashcards PDF", pdf_data, "flashcards.pdf", "application/pdf")

            else:
                st.markdown(answer)
                pdf_data = create_pdf(answer, title="Study Note")
                st.download_button("📥 Download Answer PDF", pdf_data, "answer.pdf", "application/pdf")

            st.divider()
            st.caption(f"📂 **Source:** {data.get('filename', 'Internal Database')}")

        except Exception as e:
            st.error(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    layout()