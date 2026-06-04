import streamlit as st
from utils.styles import apply_custom_css
from utils.gemini_helper import generate_daily_tip

st.set_page_config(page_title="Daily Tips - FitAI", page_icon="💡", layout="wide")
apply_custom_css()

st.title("💡 Daily Tips & Motivation")

st.markdown("Need a quick boost? Get your AI-generated daily wellness advice below.")

# Use info box instead of warning
if 'api_key' not in st.session_state or not st.session_state.api_key:
    st.info("ℹ️ Ensure your API key is set in the Settings page to generate AI tips.")

if st.button("✨ Inspire Me!"):
    with st.spinner("Fetching today's motivation..."):
        tip = generate_daily_tip()
        st.success(f"**Today's Tip:**\n\n{tip}")

st.markdown("---")
st.subheader("🔥 Build Healthy Habits")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 💧 Hydration")
    st.markdown("Drink a glass of water right after waking up to kickstart your metabolism.")
    
with col2:
    st.markdown("### 🚶‍♂️ Movement")
    st.markdown("Take a 5-minute walking break for every hour you spend coding or studying.")
    
with col3:
    st.markdown("### 🧘‍♀️ Mindset")
    st.markdown("Progress is progress. Don't stress over a missed workout, just focus on the next one.")