import streamlit as st
import httpx
import os
import base64
from fpdf import FPDF

# Configuration
API_URL = os.getenv("API_URL", "http://localhost:8000/rag/query")

def get_base64_of_bin_file(bin_file):
    """Encodes a local file to base64 for CSS injection."""
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    """
    Injects CSS to set a background image and styles all components.
    """
    try:
        bin_str = get_base64_of_bin_file(png_file)
        page_bg_img = f'''
        <style>
        /* 1. Main Background */
        .stApp {{
            background-image: url("data:image/png;base64,{bin_str}");
            background-size: cover;
            background-attachment: fixed;
            background-position: center;
        }}

        /* 2. Main Glassmorphism Container */
        .block-container {{
            background-color: rgba(255, 255, 255, 0.45); 
            backdrop-filter: blur(8px); 
            padding: 2rem 2.5rem 0.5rem 2.5rem !important; 
            border-radius: 20px;
            margin-top: 2rem;
            border: 1px solid rgba(255, 255, 255, 0.4);
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.2);
        }}

        .block-container > div:last-child {{
            margin-bottom: 0 !important;
            padding-bottom: 0 !important;
        }}

        /* 3. Göm Streamlits footers och knappar i högra hörnet */
        footer {{
            display: none !important;
        }}
        .stDeployButton {{
            display: none !important;
        }}
        #MainMenu {{
            visibility: hidden;
        }}

        /* 4. Sidebar Styling */[data-testid="stSidebar"] {{
            background-color: transparent !important;
            background-image: none !important;
        }}
        [data-testid="stSidebar"] > div:first-child {{
            background-color: rgba(255, 255, 255, 0.25) !important; 
            backdrop-filter: blur(10px);
            border-right: 1px solid rgba(255, 255, 255, 0.2);
        }}

        /* 5. GENERAL TEXT COLORS */
        h1, h2, h3, span, label, p, li, .stMarkdown p, .stMarkdown li {{
            color: #1E1E1E !important;
            text-shadow: 0px 0px 10px rgba(255,255,255,0.5); 
        }}

        /* 6. BUTTON STYLING */
        div.stButton > button, div.stDownloadButton > button {{
            background-color: #1E1E1E !important; 
            border-radius: 10px !important;
            border: 1px solid rgba(255, 255, 255, 0.5) !important;
            padding: 0.5rem 1rem !important;
            transition: all 0.3s ease;
        }}
        
        div.stButton > button p, div.stDownloadButton > button p, 
        div.stButton > button span, div.stDownloadButton > button span {{
            color: #FFFFFF !important; 
            font-weight: 600 !important;
            text-shadow: none !important; 
        }}

        div.stButton > button:hover, div.stDownloadButton > button:hover {{
            background-color: #333333 !important; 
            border-color: #FFFFFF !important;
            box-shadow: 0 4px 10px rgba(0,0,0,0.3) !important;
        }}

        /* 7. INPUT FIELD */
        div[data-baseweb="input"], div[data-baseweb="base-input"] {{
            background-color: #1E1E1E !important; 
            border-radius: 8px !important;
            border: 1px solid #555555 !important;
        }}
        
        div[data-baseweb="base-input"] input {{
            color: #FFFFFF !important; 
            -webkit-text-fill-color: #FFFFFF !important; 
            font-weight: 500 !important;
        }}
        
        div[data-baseweb="base-input"] input::placeholder {{
            color: #AAAAAA !important; 
            -webkit-text-fill-color: #AAAAAA !important;
            opacity: 1 !important;
        }}

        /* 8. Reset to avoid nested boxes */
        [data-testid="stVerticalBlock"] > div {{
            background-color: transparent !important;
        }}

        /* 9. EXPANDER FIX */
        [data-testid="stExpander"] summary {{
            background-color: #1E1E1E !important;
            border-radius: 8px !important;
            padding: 0.5rem 1rem !important;
            border: 1px solid rgba(255,255,255,0.2) !important;
        }}[data-testid="stExpander"] summary p,[data-testid="stExpander"] summary span {{
            color: #FFFFFF !important; 
            font-weight: 600 !important;
            text-shadow: none !important;
        }}

        [data-testid="stExpander"] summary:hover {{
            background-color: #333333 !important;
        }}
        </style>
        '''
        st.markdown(page_bg_img, unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning(f"Background image '{png_file}' not found.")

def create_pdf(text, title="Study Material"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("helvetica", 'B', 16)
    pdf.cell(0, 10, txt=title, ln=True, align='C')
    pdf.ln(10)
    pdf.set_font("helvetica", size=11)
    clean_text = text.encode('latin-1', 'ignore').decode('latin-1')
    pdf.multi_cell(0, 10, txt=clean_text)
    return bytes(pdf.output())

def layout():
    st.set_page_config(page_title="Study Buddy", page_icon="🎓", layout="centered")
    
    set_background("background.jpg")

    # --- SIDEBAR ---
    with st.sidebar:
        st.title("🎓 Study Tools")
        st.markdown("""
        **Quick Commands:**
        - `What is a Sigmoid function?`
        - `Give me a quiz about Transformers`
        - `Create flashcards for Regression`
        """)
        
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        st.caption("Powered by Streamlit, FastAPI & Pydantic AI")

    # --- MAIN UI ---
    st.title("🎓 Study Buddy")
    st.markdown("Your interactive AI-powered learning assistant.")
    
    user_input = st.text_input("Enter your request:", placeholder="e.g. Give me a quiz about Logistic Regression")

    if st.button("🚀 Send") and user_input.strip() != "":
        try:
            with st.spinner("🧠 Thinking..."):
                response = httpx.post(API_URL, json={"prompt": user_input}, timeout=300.0)
                response.raise_for_status()
                data = response.json()

            answer = data.get("answer", "")
            st.markdown("---")
            st.markdown("### 🤖 Response")

            if "---FACIT---" in answer:
                parts = answer.rsplit("---FACIT---", 1)
                st.markdown(parts[0].strip())
                st.balloons()
                with st.expander("🔍 Reveal Answer Key (Facit)"):
                    st.success(parts[1].strip())
                pdf_data = create_pdf(answer, title="Study Quiz")
                st.download_button("📥 Download Quiz PDF", pdf_data, "quiz.pdf", "application/pdf")

            elif "Q:" in answer and "|" in answer:
                st.info("💡 Click on a question to reveal the answer!")
                lines = answer.split('\n')
                for line in lines:
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
