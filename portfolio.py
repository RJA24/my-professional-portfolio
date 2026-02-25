import streamlit as st

st.set_page_config(page_title="Space Portfolio | Ron Jay", layout="wide", page_icon="🚀")

# --- FIGMA PIXEL-PERFECT CSS ---
st.markdown("""
    <style>
    /* 1. Deep Space Background to match Figma */
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(180deg, #0D0221 0%, #24143E 40%, #1A1A2E 100%);
        color: #ffffff;
    }

    /* 2. Neon Purple Typography */
    .hero-text {
        text-align: center;
        font-family: 'Inter', sans-serif;
    }
    
    .message-tag {
        color: #BC13FE;
        letter-spacing: 4px;
        font-size: 0.8rem;
        font-weight: bold;
        margin-bottom: 0px;
    }

    .galaxy-title {
        font-size: 3.2rem !important;
        font-weight: 900;
        color: #ffffff !important;
        text-shadow: 0 0 20px rgba(188, 19, 254, 0.8);
        margin-top: -10px;
    }

    .name-hero {
        font-size: 2.5rem;
        letter-spacing: 10px;
        color: #ffffff;
        opacity: 0.9;
    }

    /* 3. The Floating Astronaut Animation */
    @keyframes float {
        0% { transform: translateY(0px) rotate(0deg); }
        50% { transform: translateY(-20px) rotate(2deg); }
        100% { transform: translateY(0px) rotate(0deg); }
    }
    .astro-img {
        width: 300px;
        animation: float 5s ease-in-out infinite;
        filter: drop-shadow(0 0 15px rgba(76, 201, 240, 0.4));
    }

    /* Removing standard Streamlit clutter */
    [data-testid="stHeader"] { background: rgba(0,0,0,0); }
    footer { visibility: hidden; }
    </style>
    """, unsafe_allow_html=True)

# --- HERO SECTION ---
st.markdown('<div class="hero-text">', unsafe_allow_html=True)
st.markdown('<p class="message-tag">A MESSAGE FROM EARTH</p>', unsafe_allow_html=True)
st.markdown('<h1 class="galaxy-title">HELLO FELLOW GALAXY MEMBER</h1>', unsafe_allow_html=True)
st.markdown('<h2 class="name-hero">I AM RON JAY</h2>', unsafe_allow_html=True)

# Centered Astronaut (Using a transparent PNG is key!)
st.markdown("""
    <div style="display: flex; justify-content: center; margin-top: 30px;">
        <img src="https://github.com/RJA24/my-professional-portfolio/blob/main/dohis%201%20(1)%20-%20Copy.png?raw=true">
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div style="text-align:center; margin-top:20px;"><button style="background:none; border: 1px solid #BC13FE; color: white; padding: 10px 30px; border-radius: 5px; cursor: pointer;">CLICK TO OPEN</button></div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
