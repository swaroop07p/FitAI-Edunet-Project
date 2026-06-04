import streamlit as st
import json
import os
from utils.styles import apply_custom_css

# Page Configuration
st.set_page_config(
    page_title="FitAI - Student Fitness Planner",
    page_icon="🏋️",
    layout="centered",
    initial_sidebar_state="expanded"
)

apply_custom_css()

# --- NEW: Load from JSON to survive refreshes ---
if 'user_profile' not in st.session_state:
    if os.path.exists("user_data.json"):
        try:
            with open("user_data.json", "r") as f:
                data = json.load(f)
                st.session_state.user_profile = data.get("user_profile", {})
                st.session_state.profile_complete = data.get("profile_complete", False)
                if "api_key" in data:
                    st.session_state.api_key = data["api_key"]
        except Exception:
            st.session_state.user_profile = {}
            st.session_state.profile_complete = False
    else:
        st.session_state.user_profile = {}
        st.session_state.profile_complete = False
# ------------------------------------------------

# Initialize session state variables
if 'profile_complete' not in st.session_state:
    st.session_state.profile_complete = False
if 'user_profile' not in st.session_state:
    st.session_state.user_profile = {}

# Hero Section
st.title("⚡ FitAI")
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