import streamlit as st
import plotly.express as px
import pandas as pd

# MUST BE FIRST
st.set_page_config(page_title="Space Portfolio | Ron Jay C. Ayup", layout="wide", page_icon="🚀")

# --- DATA FOR RADAR CHART ---
df = pd.DataFrame(dict(
    r=[90, 85, 70, 80, 75],
    theta=['Python','Pandas','SQL','Plotly','ETL']))

fig = px.line_polar(df, r='r', theta='theta', line_close=True)
fig.update_traces(fill='toself', line_color='#4cc9f0', fillcolor='rgba(76, 201, 240, 0.3)')
fig.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font_color="white",
    polar=dict(bgcolor='rgba(0,0,0,0)', radialaxis=dict(visible=False)),
    margin=dict(l=40, r=40, t=20, b=20),
    height=350
)

# --- DUMMY RESUME DATA ---
# Right now, this creates a blank text file. 
# We will swap this out for your actual PDF later!
dummy_resume = b"This is a placeholder for your stellar resume."

# --- COSMIC CSS ---
st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(180deg, #0D0221 0%, #16213e 50%, #0f3460 100%);
        background-attachment: fixed;
        color: #ffffff;
    }
    [data-testid="stSidebar"] { background-color: rgba(26, 26, 46, 0.8); }
    
    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-15px); }
        100% { transform: translateY(0px); }
    }
    .floating-img { animation: float 4s ease-in-out infinite; }
    
    .glass-card {
        background: rgba(255, 255, 255, 0.07);
        backdrop-filter: blur(15px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 25px;
        margin-bottom: 20px;
    }
    h1, h2, h3 { color: #4cc9f0 !important; text-shadow: 0 0 15px rgba(76, 201, 240, 0.6); }
    
    /* Ensure BOTH regular buttons and download buttons get the cool gradient */
    .stButton>button, [data-testid="stDownloadButton"] button { 
        background: linear-gradient(45deg, #7209b7, #3f37c9); 
        color: white; 
        border-radius: 50px; 
        border: none;
        padding: 10px 20px;
        transition: 0.3s ease;
    }
    .stButton>button:hover, [data-testid="stDownloadButton"] button:hover {
        box-shadow: 0 0 20px rgba(114, 9, 183, 0.7);
        color: white;
    }

    [data-testid="stHeader"] { background: rgba(0,0,0,0); }
    footer { visibility: hidden; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2026/2026462.png", width=80)
    st.markdown("### 📡 Mission Control")
    st.markdown("---")
    st.markdown("📫 [Email](mailto:rj.ayup24@gmail.com)")
    st.markdown("🐙 [GitHub](https://github.com/RJA24)")
    st.markdown("💼 [LinkedIn](https://linkedin.com/)")

# --- HERO SECTION ---
col1, col2 = st.columns([1, 2])
with col1:
    st.markdown(f"""
        <div style="display: flex; justify-content: center;">
            <img src="https://github.com/RJA24/my-professional-portfolio/blob/main/dohis%201%20(1).png?raw=true" 
            class="floating-img"
            style="border-radius: 50%; border: 4px solid #4cc9f0; width: 260px; height: 260px; object-fit: cover; box-shadow: 0 0 30px rgba(76, 201, 240, 0.5);">
        </div>
        """, unsafe_allow_html=True)

with col2:
    st.markdown('<p style="color:#BC13FE; letter-spacing:3px; font-weight:bold; margin-bottom:0px;">A MESSAGE FROM EARTH</p>', unsafe_allow_html=True)
    st.title("Ron Jay C. Ayup")
    st.subheader("🌌 Data Analyst & Cosmic Problem Solver")
    st.write("Turning vast 'data galaxies' into actionable insights with Python and a touch of stardust.")
    
    # NEW: Functional Download Button
    st.download_button(
        label="Download Mission Log (Resume)",
        data=dummy_resume,
        file_name="Ron_Jay_Resume.pdf",
        mime="application/pdf"
    )

st.markdown("<br>", unsafe_allow_html=True)

# --- SKILL UNIVERSE & PROJECT ---
c1, c2 = st.columns([1, 1])

with c1:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.subheader("📊 Skill Universe")
    st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with c2:
    st.markdown('<div class="glass-card" style="height: 100%;">', unsafe_allow_html=True)
    st.header("🛸 Project: Abra SBI")
    
    # NEW: Added a sleek preview image of a dashboard to fill the empty space!
    st.image("https://images.unsplash.com/photo-1551288049-bebda4e38f71?q=80&w=2070&auto=format&fit=crop", use_container_width=True)
    
    st.write("A real-time geospatial monitoring system built to track provincial vaccination coverage.")
    st.markdown("**Core Engines:** `Python` • `Streamlit` • `Plotly` • `Google API`")
    st.link_button("Launch Dashboard 🚀", "https://your-dashboard-link.streamlit.app/")
    st.markdown('</div>', unsafe_allow_html=True)

# --- CONTACT SECTION ---
st.header("📬 Contact the Bridge")
with st.form("contact_form"):
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    name = st.text_input("Name")
    msg = st.text_area("Message")
    submitted = st.form_submit_button("Send Signal 🛸")
    if submitted:
        st.success("Signal sent into the deep!")
    st.markdown('</div>', unsafe_allow_html=True)
