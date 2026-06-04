import streamlit as st
from utils.styles import apply_custom_css
from utils.gemini_helper import generate_diet_plan

st.set_page_config(page_title="AI Diet Planner - FitAI", page_icon="🥗", layout="wide")
apply_custom_css()

st.title("🥗 AI Personalized Diet Planner")

if not st.session_state.get('profile_complete', False):
    st.warning("Please complete your profile first!")
    st.stop()

st.info(f"Generating plan based on: **{st.session_state.user_profile['diet_type']}** | Culture: **{st.session_state.user_profile['cultural_preference']}** | Budget: **{st.session_state.user_profile['budget']}**")

if st.button("🍎 Generate AI Meal Plan"):
    with st.spinner("Crafting a delicious, affordable meal plan for you..."):
        plan = generate_diet_plan(st.session_state.user_profile)
        
        if plan:
            st.session_state.current_diet_plan = plan
            st.success("Meal Plan Generated!")

if 'current_diet_plan' in st.session_state:
    with st.expander("View Your Weekly Meal Plan", expanded=True):
        st.markdown(st.session_state.current_diet_plan)
        
        st.download_button(
            label="📥 Download Plan as TXT",
            data=st.session_state.current_diet_plan,
            file_name="FitAI_Diet_Plan.txt",
            mime="text/plain"
        )