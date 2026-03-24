import streamlit as st
from crew import run_research_crew
import os, glob
from datetime import datetime

# Page config
st.set_page_config(
    page_title="AI Research Agent",
    page_icon="🔍",
    layout="wide"
)

# Custom CSS for a cleaner look
st.markdown("""
<style>
    .main { max-width: 1000px; margin: auto; }
    .stButton button { width: 100%; height: 50px; font-size: 18px; }
    .report-box { background: #1e1e2e; padding: 24px; border-radius: 8px; }
</style>
""", unsafe_allow_html=True)

# ── Header ───────────────────────────────────────
st.title("🤖 Multi-Agent AI Research Generator")
st.markdown("*Powered by CrewAI + Groq + Tavily*")
st.divider()

# ── Input Section ────────────────────────────────
col1, col2 = st.columns([3, 1])
with col1:
    topic = st.text_input(
        "📌 Research Topic",
        placeholder="e.g., AI trends in Indian fintech 2026",
        help="Be specific for better results"
    )
with col2:
    st.write("")
    st.write("")
    generate_btn = st.button("🚀 Generate Report", type="primary")

# Show example topics
st.caption("💡 Try: 'Generative AI in Indian healthcare 2025' | 'Electric vehicles adoption India 2026' | 'UPI payment trends Q1 2026'")

# ── Agent Progress ───────────────────────────────
if generate_btn and topic:
    st.divider()
    st.subheader("⚙️ Agent Pipeline Running...")
    
    # Show progress steps
    progress_container = st.container()
    with progress_container:
        col1, col2, col3, col4 = st.columns(4)
        s1 = col1.status("🔍 Researcher", state="running")
        s2 = col2.status("✍️ Writer", state="complete")  
        s3 = col3.status("✏️ Editor", state="complete")
        s4 = col4.status("✅ Fact-Checker", state="complete")
    
    # Run the crew
    with st.spinner("Running 4 AI agents... this takes ~2 minutes"):
        try:
            result, filepath = run_research_crew(topic)
            st.session_state["last_result"] = result
            st.session_state["last_file"] = filepath
            st.success(f"✅ Report generated! Saved to {filepath}")
        except Exception as e:
            st.error(f"Error: {e}")

# ── Display Result ───────────────────────────────
if "last_result" in st.session_state:
    st.divider()
    
    tab1, tab2 = st.tabs(["📄 Rendered Report", "📝 Raw Markdown"])
    
    with tab1:
        st.markdown(st.session_state["last_result"])
    
    with tab2:
        st.code(st.session_state["last_result"], language="markdown")
    
    # Download button
    st.download_button(
        label="⬇️ Download Report (.md)",
        data=st.session_state["last_result"],
        file_name=f"report_{topic[:30].replace(' ','_')}.md",
        mime="text/markdown"
    )

# ── Past Reports Sidebar ─────────────────────────
with st.sidebar:
    st.header("📁 Past Reports")
    reports = glob.glob("outputs/*.md")
    if reports:
        for r in sorted(reports, reverse=True)[:5]:
            if st.button(os.path.basename(r), key=r):
                with open(r) as f:
                    st.session_state["last_result"] = f.read()
    else:
        st.info("No reports yet. Generate one!")
    
    st.divider()
    st.caption("🔑 API Status")
    st.success("Groq: Connected") if os.getenv("GROQ_API_KEY") else st.error("Groq: Missing key")
    st.success("Tavily: Connected") if os.getenv("TAVILY_API_KEY") else st.error("Tavily: Missing key")
