import streamlit as st
from utils.styles import apply_custom_css
from utils.gemini_helper import init_session_state

# Page Configuration
st.set_page_config(
    page_title="FitAI - Student Fitness Planner",
    page_icon="🏋️",
    layout="centered",
    initial_sidebar_state="expanded"
)

# This single line handles everything securely!
init_session_state()

apply_custom_css()

# Initialize empty state for EVERY new device/tab
if 'user_profile' not in st.session_state:
    st.session_state.user_profile = {}
if 'profile_complete' not in st.session_state:
    st.session_state.profile_complete = False
if 'api_key' not in st.session_state:
    st.session_state.api_key = ""

# --- NEW: Pull data from the browser ---
# load_browser_data()
# ---------------------------------------

# Hero Section

st.markdown('<div class="title-container">🏋️ <span class="gradient-text">FitAI</span></div>', unsafe_allow_html=True)
# st.title("⚡ FitAI")
st.subheader("Smart AI Fitness & Diet Planner for Students")

st.markdown("""
Welcome to your personal AI fitness assistant! 

Juggling classes, projects, and a tight budget makes staying healthy tough. FitAI generates **highly personalized, affordable, and practical** workout routines and meal plans tailored specifically to your student lifestyle.

### Core Features:
* 🎯 **Goal-Oriented Workouts:** Tailored to your equipment and schedule.
* 🍛 **Cultural & Local Diet Plans:** Enjoy meals that fit your palate and wallet.
* 📊 **Smart Tracking:** Monitor your BMI, consistency, and daily habits.
""")

st.write("") # Spacer
if st.button("🚀 Get Started Now"):
    st.switch_page("pages/1_Profile_Setup.py")

st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Powered by Streamlit & Google Gemini AI</p>", unsafe_allow_html=True)