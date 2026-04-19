import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_mistralai import ChatMistralAI

# ------------------ Setup ------------------
load_dotenv()

st.set_page_config(
    page_title="CineSage 🎬",
    page_icon="🎬",
    layout="centered"
)

# ------------------ Styling ------------------
st.markdown("""
<style>
.big-title {
    font-size: 36px;
    font-weight: bold;
    text-align: center;
}
.sub-text {
    text-align: center;
    color: gray;
}
.result-box {
    padding: 20px;
    border-radius: 12px;
    background-color: #0e1117;
    border: 1px solid #333;
}
</style>
""", unsafe_allow_html=True)

# ------------------ Header ------------------
st.markdown('<div class="big-title">🎬 CineSage</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-text">Smart Movie Info Extractor</div>', unsafe_allow_html=True)

st.divider()

# ------------------ Sidebar ------------------
with st.sidebar:
    st.header("⚙️ Options")

    if st.button("Load Sample"):
        st.session_state.sample = """Directed by Rajkumar Hirani and released in 2009, 3 Idiots is a beloved Indian film blending comedy, drama, and social commentary to critique the oppressive Indian education system..."""

    st.markdown("### 💡 Tips")
    st.markdown("""
- Paste a movie paragraph  
- Click extract  
- Download results  
""")

# ------------------ Model ------------------
model = ChatMistralAI(model="mistral-small-2506", temperature=0)

# ------------------ Prompt ------------------
prompt = ChatPromptTemplate.from_messages([
    ("system", """
You are an expert information extraction system.

Your task is to extract useful and relevant information from the given text.

Instructions:
- Do NOT hallucinate.
- Keep answers concise.
- Use clear headings.
- If missing, write "Not mentioned".

Format:

Title:
Type:
Release Year:
Director:

Main Cast:
- 

Genre:
- 

Summary:

Key Themes:
- 

Important Events:
- 

Awards & Recognition:
- 

Source Material:

Filming Locations:
- 

Unique Facts:
- 

Text:
{input_text}
"""),
    ("human", "Extract from:\n{paragraph}")
])

# ------------------ Input ------------------
text_input = st.text_area(
    "📥 Enter Movie Paragraph",
    value=st.session_state.get("sample", ""),
    height=220
)

# ------------------ Buttons ------------------
col1, col2 = st.columns(2)

with col1:
    generate = st.button("✨ Extract Info")

with col2:
    clear = st.button("🧹 Clear")

if clear:
    st.session_state.sample = ""
    st.rerun()

# ------------------ Processing ------------------
if generate and text_input.strip():
    with st.spinner("Extracting insights... 🎥"):
        final_prompt = prompt.format_messages(
            input_text=text_input,
            paragraph=text_input
        )

        response = model.invoke(final_prompt)

    st.success("Extraction Complete ✅")

    # ------------------ Output ------------------
    st.markdown("### 📊 Extracted Information")

    st.markdown(
        f'<div class="result-box">{response.content.replace("\n", "<br>")}</div>',
        unsafe_allow_html=True
    )

    # ------------------ Download ------------------
    st.download_button(
        label="📄 Download Result",
        data=response.content,
        file_name="movie_info.txt",
        mime="text/plain"
    )

else:
    st.info("Enter a paragraph and click 'Extract Info'")