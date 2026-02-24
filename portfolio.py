import streamlit as st

st.set_page_config(page_title="Portfolio | Ron Jay C. Ayup", layout="wide", page_icon="💼")

# --- CUSTOM CSS FOR PROFESSIONAL FEEL ---
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #007bff; color: white; }
    .project-card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #007bff;
        box-shadow: 2px 2px 15px rgba(0,0,0,0.05);
    }
    </style>
    """, unsafe_allow_html=True)

# --- HERO SECTION ---
col1, col2 = st.columns([1, 2], gap="large")
with col1:
    # You can add a professional headshot here
    st.image("https://github.com/RJA24/my-professional-portfolio/blob/main/dohis%201%20(1).png?raw=true", width=250) 

with col2:
    st.title("Your Name Here")
    st.write("📍 Abra, Philippines")
    st.subheader("Data Analyst | Health Information Systems Specialist")
    st.write("""
    I specialize in transforming complex health data into interactive visual stories. 
    With a focus on public health and provincial-scale monitoring, I build tools that 
    help decision-makers act faster and more accurately.
    """)
    st.button("✉️ Contact Me")

st.markdown("---")

# --- FEATURED PROJECT ---
st.header("🚀 Featured Project")
with st.container():
    st.markdown('<div class="project-card">', unsafe_allow_html=True)
    c1, c2 = st.columns([2, 1])
    with c1:
        st.subheader("Abra Provincial SBI Monitoring Dashboard")
        st.write("""
        Developed a real-time tracking system for the School-Based Immunization program. 
        The system automates data collection from 27 municipalities and visualizes 
        vaccination density using geospatial 'plasma' mapping.
        """)
        st.info("**Tech:** Python, Streamlit, Plotly, Google Sheets API, GIS Mapping")
    with c2:
        st.write(" ")
        st.write(" ")
        # Link to your actual live dashboard
        st.link_button("View Live Dashboard", "https://abra-sbi-dashboard-5uubqi6rcsqdknxudevhrv.streamlit.app/")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")

# --- SKILLS ---
st.header("🛠️ Technical Toolbox")
sk1, sk2, sk3 = st.columns(3)
with sk1:
    st.write("**Data Analysis**")
    st.caption("Pandas, NumPy, Python, Excel Automation")
with sk2:
    st.write("**Visualization**")
    st.caption("Plotly Express, Mapbox, GIS, Matplotlib")
with sk3:
    st.write("**Infrastructure**")
    st.caption("Streamlit Cloud, Git/GitHub, Google Cloud APIs")

# --- FOOTER ---
st.markdown("<br><br><center>Built with ❤️ using Python & Streamlit</center>", unsafe_allow_html=True)
