import streamlit as st
from utils.styles import apply_custom_css
from utils.gemini_helper import generate_workout_plan
from utils.gemini_helper import init_session_state

# This single line handles everything securely!
st.set_page_config(page_title="AI Workout Planner - FitAI", page_icon="💪", layout="wide")

init_session_state()

apply_custom_css()

# Initialize session state variables if they don't exist
if 'user_profile' not in st.session_state:
    st.session_state.user_profile = {}
if 'profile_complete' not in st.session_state:
    st.session_state.profile_complete = False
if 'api_key' not in st.session_state:
    st.session_state.api_key = ""

st.title("💪 AI Personalized Workout Planner")

if not st.session_state.get('profile_complete', False):
    st.warning("Please complete your profile first!")
    st.stop()

st.info(f"Generating plan based on: **{st.session_state.user_profile['goal']}** | **{st.session_state.user_profile['equipment']}** | **{st.session_state.user_profile['days_available']} days/week**")

if st.button("⚡ Generate AI Workout Plan"):
    with st.spinner("Analyzing profile and generating your custom routine..."):
        plan = generate_workout_plan(st.session_state.user_profile)
        
        if plan:
            st.session_state.current_workout_plan = plan
            st.success("Workout Plan Generated!")

if 'current_workout_plan' in st.session_state:
    with st.expander("View Your Current Plan", expanded=True):
        st.markdown(st.session_state.current_workout_plan)
        
        st.download_button(
            label="📥 Download Plan as TXT",
            data=st.session_state.current_workout_plan,
            file_name="FitAI_Workout_Plan.txt",
            mime="text/plain"
        )