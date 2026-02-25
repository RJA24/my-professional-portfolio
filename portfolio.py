import streamlit as st
import plotly.express as px
import pandas as pd

# MUST BE FIRST
st.set_page_config(page_title="Space Portfolio | Ron Jay C. Ayup", layout="wide", page_icon="🚀")

# --- DATA & ASSETS ---
df = pd.DataFrame(dict(
    r=[90, 85, 80, 75, 85],
    theta=['Python (AI-Assisted)','Data Tracking','Video Editing','Canva Design','NIP Automation']))

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
    
    /* NEW: Typing Animation CSS */
    .typing-text {
        overflow: hidden;
        border-right: 3px solid #BC13FE; /* Neon purple cursor */
        white-space: nowrap;
        animation: typing 3.5s steps(45, end) forwards, blink 0.8s step-end infinite;
        font-size: 1.7rem;
        font-weight: bold;
        color: #4cc9f0;
        margin-top: -10px;
        margin-bottom: 15px;
        max-width: fit-content;
    }
    
    @keyframes typing {
        from { width: 0; }
        to { width: 100%; }
    }
    
    @keyframes blink {
        from, to { border-color: transparent; }
        50% { border-color: #BC13FE; }
    }
    
    .glass-card {
        background: rgba(255, 255, 255, 0.07);
        backdrop-filter: blur(15px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 25px;
        margin-bottom: 20px;
    }
    h1, h2, h3 { color: #4cc9f0 !important; text-shadow: 0 0 15px rgba(76, 201, 240, 0.6); }
    
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
    
    div[role="radiogroup"] > label {
        background: rgba(255, 255, 255, 0.05);
        padding: 10px 15px;
        border-radius: 10px;
        margin-bottom: 5px;
        transition: 0.3s;
        cursor: pointer;
    }
    div[role="radiogroup"] > label:hover {
        background: rgba(76, 201, 240, 0.2);
    }
    
    .project-list {
        line-height: 1.8;
        font-size: 1.05rem;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2026/2026462.png", width=80)
    st.markdown("### 📡 Mission Control")
    
    page = st.radio("Select Sector:", ["🏠 Basecamp (Home)", "🛸 Mission Logs (Projects)"])
    
    st.markdown("---")
    st.markdown("### 🔗 Comm Links")
    st.markdown("📫 [Email](mailto:ronjay.1204@gmail.com)")
    st.markdown("🐙 [GitHub](https://github.com/RJA24)")
    st.markdown("💼 [LinkedIn](https://www.linkedin.com/in/ron-jay-ayup-a1824b3b3)")
    st.markdown("▶️ [YouTube](https://www.youtube.com/@JangTVyt)")
    st.markdown("🎵 [TikTok](https://www.tiktok.com/@jangtv_)")

# ==========================================
# PAGE 1: HOME (BASECAMP)
# ==========================================
if page == "🏠 Basecamp (Home)":
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
        
        # NEW: The animated typing text replaces the standard subheader
        st.markdown('<div class="typing-text">🌌 Tech-Forward Virtual Assistant & Data Analyst</div>', unsafe_allow_html=True)
        
        st.markdown("""
        **Mission Overview:** I am a highly adaptable professional bridging the gap between complex data and compelling digital media. With a solid foundation in health data management, I specialize in transforming raw numbers into actionable insights and engaging content. Whether I'm orchestrating AI-assisted Python scripts, designing high-impact visual campaigns in Canva, or editing dynamic video content across platforms, I bring a unique, multi-disciplinary approach to problem-solving. I'm actively seeking Virtual Assistant roles where I can leverage my blend of analytical precision and creative storytelling to help teams operate at warp speed.
        """)
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.download_button("Download Mission Log (Resume)", data=dummy_resume, file_name="Ron_Jay_Resume.pdf", mime="application/pdf")

    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- CORE VA SERVICES SECTION ---
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.header("🛠️ Core VA Services")
    s1, s2, s3 = st.columns(3)
    with s1:
        st.markdown("### 📊 Data & Dashboards")
        st.write("Google Sheets automation, real-time data tracking (like NIP workflows), and transforming raw data into clear, interactive Streamlit/Plotly dashboards.")
    with s2:
        st.markdown("### 🎬 Multimedia Magic")
        st.write("End-to-end video editing using Premiere Pro and CapCut for YouTube, TikTok, and Reels, plus eye-catching graphic design via Canva.")
    with s3:
        st.markdown("### 🤖 AI-Powered Support")
        st.write("Leveraging AI tools to vibe-code custom solutions, streamline repetitive tasks, and bring tech-forward efficiency to daily administrative operations.")
    st.markdown('</div>', unsafe_allow_html=True)

    c1, c2 = st.columns([1, 1])
    with c1:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.subheader("📊 Skill Universe")
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with c2:
        st.markdown('<div class="glass-card" style="height: 100%;">', unsafe_allow_html=True)
        st.subheader("📬 Contact the Bridge")
        
        # --- NEW WORKING CONTACT FORM WITH REDIRECT & AUTORESPONSE ---
        contact_form = """
        <form action="https://formsubmit.co/ronjay.1204@gmail.com" method="POST">
             <input type="hidden" name="_captcha" value="false">
             <input type="hidden" name="_next" value="https://your-portfolio-url.streamlit.app/">
             <input type="hidden" name="_autoresponse" value="Thanks for reaching out! I have received your message and will get back to you as soon as I can.">
             <input type="text" name="name" placeholder="Your Name" required style="width: 100%; padding: 10px; margin-bottom: 10px; border-radius: 5px; border: 1px solid #ccc; background: rgba(255, 255, 255, 0.1); color: white;">
             <input type="email" name="email" placeholder="Your Email" required style="width: 100%; padding: 10px; margin-bottom: 10px; border-radius: 5px; border: 1px solid #ccc; background: rgba(255, 255, 255, 0.1); color: white;">
             <textarea name="message" placeholder="Your Message" required style="width: 100%; padding: 10px; margin-bottom: 10px; border-radius: 5px; border: 1px solid #ccc; height: 100px; background: rgba(255, 255, 255, 0.1); color: white;"></textarea>
             <button type="submit" style="padding: 10px 20px; border-radius: 50px; background: linear-gradient(45deg, #7209b7, #3f37c9); color: white; border: none; cursor: pointer; width: 100%; transition: 0.3s ease;">Send Signal 🛸</button>
        </form>
        """
        st.markdown(contact_form, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# PAGE 2: PROJECTS (MISSION LOGS)
# ==========================================
elif page == "🛸 Mission Logs (Projects)":
    st.title("🛸 Mission Logs & Deep Space Projects")
    st.write("A detailed archive of my data monitoring systems, visual design layouts, public health tracking architecture, and video content.")
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- Project 1: Abra SBI ---
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    p1_col1, p1_col2 = st.columns([1, 2])
    with p1_col1:
        st.image("https://images.unsplash.com/photo-1551288049-bebda4e38f71?q=80&w=2070&auto=format&fit=crop", use_container_width=True)
    with p1_col2:
        st.header("Abra SBI Dashboard")
        st.write("A real-time geospatial monitoring system built to track provincial vaccination coverage, synthesizing complex data for rapid decision making.")
        st.markdown("**Core Engines:** `Python` • `Streamlit` • `Plotly` • `Google API`")
        st.link_button("Launch Dashboard 🚀", "https://your-dashboard-link.streamlit.app/")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- Project 2: Google Sheets NIP Trackers ---
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.header("📊 NIP Data Tracking & Automation")
    st.write("Engineered comprehensive Google Sheet trackers to monitor, evaluate, and manage National Immunization Program (NIP) activities, streamlining data collection for vital public health initiatives.")
    st.markdown("**Core Engines:** `Google Sheets` • `Data Management` • `NIP Tracking` • `Data Validation`")
    st.markdown("<br>", unsafe_allow_html=True)
    
    nip_c1, nip_c2 = st.columns(2)
    with nip_c1:
        st.markdown("### 💉 Immunization Campaigns")
        st.markdown("""
        <div class="project-list">
        • School Based Immunization Tracker (2024 & 2025) <br>
        • bOPV Supplemental Immunization Activity (2023 & 2024) <br>
        • MR Supplemental Immunization Activity (2023 & 2024)
        </div>
        """, unsafe_allow_html=True)

    with nip_c2:
        st.markdown("### 📋 Logistics & Outbreak Response")
        st.markdown("""
        <div class="project-list">
        • COVID-19 Vaccination Tracker <br>
        • Flu Vaccination Tracker <br>
        • Vaccine Physical Inventory Tracker <br>
        • <i>And many more custom surveillance tools...</i>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # --- Project 3: Canva Visuals & Cartography ---
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.header("🎨 Visual Design & Cartography")
    st.write("Conceptualized and designed high-impact visual assets and maps for critical public health initiatives and disaster risk reduction programs.")
    st.markdown("**Core Engines:** `Canva` • `Graphic Design` • `Cartography`")
    st.markdown("<br>", unsafe_allow_html=True)
    
    canva_c1, canva_c2 = st.columns(2)
    with canva_c1:
        st.markdown("### 🏥 Health & Training Events")
        st.markdown("""
        <div class="project-list">
        • Buntis Congress Sticker Layout <br>
        • Basic Life Support & Standard First Aid Training Tarpaulin <br>
        • Hearts Month Celebration 2026 Tarpaulin <br>
        • National Oral Health Month 2026 Tarpaulin
        </div>
        """, unsafe_allow_html=True)

    with canva_c2:
        st.markdown("### 🚨 DRRM-H & Mapping")
        st.markdown("""
        <div class="project-list">
        • DRRM Plan Cover Page Layout <br>
        • Pre-planning of the 2026-2028 DRRM-H Plan Tarpaulin <br>
        • Finalization of the 2026-2028 DRRM-H Plan Tarpaulin <br>
        • High Resolution Health Facility Map of Abra
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # --- Project 4: Video Content Creation ---
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.header("🎬 Video Production & Content Creation")
    st.write("Editing, directing, and producing highly engaging multimedia content tailored for varying social media algorithms and audiences.")
    st.markdown("**Core Engines:** `Premiere Pro` • `CapCut` • `After Effects` • `Filmora` • `PowerDirector`")
    st.markdown("<br>", unsafe_allow_html=True)
    
    vid_c1, vid_c2 = st.columns(2)
    with vid_c1:
        st.markdown("### 📱 Distribution Platforms")
        st.markdown("""
        <div class="project-list">
        • YouTube Content <br>
        • TikTok Shorts <br>
        • Facebook Reels & Long-form Video
        </div>
        """, unsafe_allow_html=True)

    with vid_c2:
        st.markdown("### ✂️ Editorial Toolkit")
        st.markdown("""
        <div class="project-list">
        • Advanced Timeline Editing & Transitions <br>
        • Motion Graphics & Basic VFX <br>
        • Multi-platform Format Optimization
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
