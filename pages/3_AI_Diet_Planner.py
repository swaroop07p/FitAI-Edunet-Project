import streamlit as st
from utils.styles import apply_custom_css
from utils.gemini_helper import generate_diet_plan, init_session_state

# 1. PAGE CONFIG MUST BE FIRST
st.set_page_config(page_title="AI Diet Planner - FitAI", page_icon="🥗", layout="wide")

# 2. INITIALIZE SESSION AND STYLES
apply_custom_css()

init_session_state()

# 3. RESPONSIVE TABLE CSS (Forces text to wrap on mobile devices)
st.markdown("""
    <style>
    .stMarkdown table {
        width: 100% !important;
        table-layout: auto;
    }
    .stMarkdown th, .stMarkdown td {
        word-break: break-word !important;
        white-space: normal !important;
        padding: 8px !important;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state variables if they don't exist
if 'user_profile' not in st.session_state:
    st.session_state.user_profile = {}
if 'profile_complete' not in st.session_state:
    st.session_state.profile_complete = False
if 'api_key' not in st.session_state:
    st.session_state.api_key = ""

st.markdown('<div class="title-container">🥗 <span class="gradient-text">AI Personalized Diet Planner</span></div>', unsafe_allow_html=True)
# st.title("🥗 AI Personalized Diet Planner")

if not st.session_state.get('profile_complete', False):
    st.warning("Please complete your profile first!")
    st.stop()

st.info(f"Generating plan based on: **{st.session_state.user_profile.get('diet_type', '')}** | Culture: **{st.session_state.user_profile.get('cultural_preference', '')}** | Budget: **{st.session_state.user_profile.get('budget', '')}**")

if st.button("🍽️ Generate AI Meal Plan"):
    with st.spinner("Crafting a delicious, affordable meal plan for you..."):
        plan = generate_diet_plan(st.session_state.user_profile)
        
        if plan:
            st.session_state.current_diet_plan = plan
            st.success("Meal Plan Generated!")

if 'current_diet_plan' in st.session_state:
    with st.expander("View Your Weekly Meal Plan", expanded=True):
        # The CSS injected above will automatically apply to this markdown render
        st.markdown(st.session_state.current_diet_plan)
        
        st.download_button(
            label="📥 Download Plan as TXT",
            data=st.session_state.current_diet_plan,
            file_name="FitAI_Diet_Plan.txt",
            mime="text/plain"
        )