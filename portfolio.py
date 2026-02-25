import streamlit as st

st.set_page_config(page_title="Space Portfolio | Ron Jay C. Ayup", layout="wide", page_icon="🚀")

# --- SPACE THEME CSS ---
st.markdown("""
    <style>
    /* 1. Deep Space Background */
    [data-testid="stAppViewContainer"] {
        background: radial-gradient(circle at top right, #1a1a2e, #16213e, #0f3460);
        background-attachment: fixed;
        color: #ffffff;
    }

    /* 2. Glassmorphism Card Effect */
    .glass-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 30px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        margin-bottom: 25px;
    }

    /* 3. Glowing Text & Buttons */
    h1, h2, h3 {
        color: #4cc9f0 !important;
        text-shadow: 0 0 10px rgba(76, 201, 240, 0.5);
    }
    
    .stButton>button {
        background: linear-gradient(45deg, #7209b7, #3f37c9);
        color: white;
        border: none;
        border-radius: 50px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        box-shadow: 0 0 20px #7209b7;
        transform: translateY(-2px);
    }

    /* Hide standard Streamlit header/footer for clean look */
    [data-testid="stHeader"] { background: rgba(0,0,0,0); }
    footer { visibility: hidden; }
    </style>
    """, unsafe_allow_html=True)

# --- HERO SECTION ---
col1, col2 = st.columns([1, 2])

with col1:
    # Use a circular style for your profile pic
    st.markdown("""
        <div style="display: flex; justify-content: center;">
            <img src="https://github.com/RJA24/my-professional-portfolio/blob/main/dohis%201%20(1).png?raw=true" 
            style="border-radius: 50%; border: 4px solid #4cc9f0; width: 250px; box-shadow: 0 0 25px #4cc9f0;">
        </div>
        """, unsafe_allow_html=True)

with col2:
    st.title("Ron Jay C. Ayup")
    st.subheader("🌌 Data Analyst & Cosmic Problem Solver")
    st.write("Specializing in turning vast 'data galaxies' into actionable insights.")
    st.button("Download Mission Log (Resume)")

st.markdown("<br>", unsafe_allow_html=True)

# --- FEATURED PROJECT (GLASS CARD) ---
st.markdown('<div class="glass-card">', unsafe_allow_html=True)
c1, c2 = st.columns([2, 1])
with c1:
    st.header("🛸 Project: Abra SBI Dashboard")
    st.write("""
    A real-time geospatial monitoring system built to track provincial vaccination coverage. 
    Implemented custom ETL pipelines to sync Google Sheets with interactive Plotly maps.
    """)
    st.markdown("**Core Engines:** Python • Streamlit • Plotly • Google API")
with c2:
    st.write("<br>", unsafe_allow_html=True)
    st.link_button("Launch Dashboard 🚀", "https://your-dashboard-link.streamlit.app/")
st.markdown('</div>', unsafe_allow_html=True)

# --- SKILLS GRID ---
st.header("🛠️ Tech Stack")
s1, s2, s3, s4 = st.columns(4)
with s1:
    st.markdown('<div class="glass-card" style="text-align:center;"><b>Python</b></div>', unsafe_allow_html=True)
with s2:
    st.markdown('<div class="glass-card" style="text-align:center;"><b>Pandas</b></div>', unsafe_allow_html=True)
with s3:
    st.markdown('<div class="glass-card" style="text-align:center;"><b>Plotly</b></div>', unsafe_allow_html=True)
with s4:
    st.markdown('<div class="glass-card" style="text-align:center;"><b>SQL</b></div>', unsafe_allow_html=True)
