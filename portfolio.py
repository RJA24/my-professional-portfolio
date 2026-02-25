import streamlit as st

st.set_page_config(page_title="Space Portfolio | Ron Jay C. Ayup", layout="wide", page_icon="🚀")

# --- CLEANED & ENHANCED CSS ---
st.markdown("""
    <style>
    /* 1. Deep Space Background with Figma-inspired Gradient */
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(180deg, #0D0221 0%, #16213e 50%, #0f3460 100%);
        background-attachment: fixed;
        color: #ffffff;
    }

    /* 2. Floating Animation */
    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-15px); }
        100% { transform: translateY(0px); }
    }
    .floating-img {
        animation: float 4s ease-in-out infinite;
    }

    /* 3. Enhanced Glassmorphism */
    .glass-card {
        background: rgba(255, 255, 255, 0.07);
        backdrop-filter: blur(15px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 25px;
        transition: transform 0.3s ease;
    }
    .glass-card:hover {
        transform: scale(1.02);
        border: 1px solid #4cc9f0;
    }

    /* 4. Glowing Typography */
    h1, h2, h3 {
        color: #4cc9f0 !important;
        text-shadow: 0 0 15px rgba(76, 201, 240, 0.6);
    }
    
    .stButton>button {
        background: linear-gradient(45deg, #7209b7, #3f37c9);
        color: white;
        border: none;
        border-radius: 50px;
        padding: 10px 25px;
        font-weight: bold;
    }

    /* Hide standard Streamlit header */
    [data-testid="stHeader"] { background: rgba(0,0,0,0); }
    footer { visibility: hidden; }
    </style>
    """, unsafe_allow_html=True)

# --- HERO SECTION ---
col1, col2 = st.columns([1, 2])

with col1:
    # Profile Picture with Neon Glow & Floating Effect
    st.markdown("""
        <div style="display: flex; justify-content: center;">
            <img src="https://github.com/RJA24/my-professional-portfolio/blob/main/dohis%201%20(1)%20-%20Copy.png?raw=true" 
            class="floating-img"
            style="border-radius: 50%; border: 4px solid #4cc9f0; width: 260px; height: 260px; object-fit: cover; box-shadow: 0 0 30px rgba(76, 201, 240, 0.5);">
        </div>
        """, unsafe_allow_html=True)

with col2:
    st.markdown('<p style="color:#BC13FE; letter-spacing:3px; font-weight:bold;">A MESSAGE FROM EARTH</p>', unsafe_allow_html=True)
    st.title("Ron Jay C. Ayup")
    st.subheader("🌌 Data Analyst & Cosmic Problem Solver")
    st.write("Turning vast 'data galaxies' into actionable insights with Python and a touch of stardust.")
    st.button("Download Mission Log (Resume)")

st.markdown("<br>", unsafe_allow_html=True)

# --- FEATURED PROJECT ---
st.markdown('<div class="glass-card">', unsafe_allow_html=True)
c1, c2 = st.columns([2, 1])
with c1:
    st.header("🛸 Project: Abra SBI Dashboard")
    st.write("""
    A real-time geospatial monitoring system built to track provincial vaccination coverage. 
    Synchronizing complex datasets into interactive Plotly maps for high-stakes decision making.
    """)
    st.markdown("**Core Engines:** `Python` • `Streamlit` • `Plotly` • `Google Cloud API`")
with c2:
    st.write("<br>", unsafe_allow_html=True)
    st.link_button("Launch Dashboard 🚀", "https://your-dashboard-link.streamlit.app/")
st.markdown('</div>', unsafe_allow_html=True)

# --- SKILLS GRID ---
st.header("🛠️ Tech Stack")
s1, s2, s3, s4 = st.columns(4)
skills = ["Python", "Pandas", "Plotly", "SQL"]
cols = [s1, s2, s3, s4]

for col, skill in zip(cols, skills):
    with col:
        st.markdown(f'<div class="glass-card" style="text-align:center;"><b>{skill}</b></div>', unsafe_allow_html=True)
