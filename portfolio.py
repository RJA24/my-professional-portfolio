import streamlit as st

st.set_page_config(page_title="Space Portfolio | Jay", layout="wide", page_icon="🚀")

# --- UPDATED FIGMA-STYLE CSS ---
st.markdown("""
    <style>
    /* 1. Updated to match Figma colors (Purple/Blue Gradient) */
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(180deg, #1A0B2E 0%, #2D1B4E 40%, #1E3A8A 100%);
        color: #ffffff;
    }

    /* 2. Custom Font & Centering for Hero */
    .hero-container {
        text-align: center;
        padding-top: 50px;
    }

    .message-from-earth {
        letter-spacing: 2px;
        font-size: 0.9rem;
        color: #E0B0FF;
        margin-bottom: -10px;
    }

    .main-title {
        font-size: 3.5rem !important;
        font-weight: 800;
        color: #E0B0FF !important;
        text-shadow: 0 0 20px rgba(188, 19, 254, 0.6);
    }

    /* 3. Floating Astronaut Animation */
    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-20px); }
        100% { transform: translateY(0px); }
    }
    .floating-astro {
        width: 200px;
        animation: float 4s ease-in-out infinite;
        margin-top: 20px;
    }

    /* Hide standard Streamlit elements */
    [data-testid="stHeader"] { background: rgba(0,0,0,0); }
    footer { visibility: hidden; }
    </style>
    """, unsafe_allow_html=True)

# --- HERO SECTION (FIGMA STYLE) ---
st.markdown('<div class="hero-container">', unsafe_allow_html=True)
st.markdown('<p class="message-from-earth">A MESSAGE FROM EARTH</p>', unsafe_allow_html=True)
st.markdown('<h1 class="main-title">HELLO FELLOW GALAXY MEMBER</h1>', unsafe_allow_html=True)
st.markdown('<h2 style="color: #ffffff; letter-spacing: 8px;">I AM JAY</h2>', unsafe_allow_html=True)

# THE ASTRONAUT (Add your image link here)
st.markdown("""
    <div style="display: flex; justify-content: center;">
        <img src="https://i.ibb.co/vz6mXmP/astronaut-laptop.png" class="floating-astro">
    </div>
    """, unsafe_allow_html=True)

st.markdown('<button style="background: none; border: 2px solid white; color: white; padding: 10px 20px; border-radius: 5px; margin-top: 20px;">CLICK TO OPEN</button>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- YOUR DASHBOARD SECTION (KEEPING YOUR WORK) ---
st.markdown("<br><br>", unsafe_allow_html=True)
st.header("🛸 Mission Report: Abra SBI Dashboard")
# ... (Keep your Project & Skills columns here)
