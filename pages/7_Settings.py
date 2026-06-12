import streamlit as st
from utils.styles import apply_custom_css
from utils.gemini_helper import init_session_state, save_user_data

# 1. PAGE CONFIG MUST BE FIRST
st.set_page_config(page_title="Settings - FitAI", page_icon="⚙️")

# 2. APPLY STYLES
apply_custom_css()

# 3. INITIALIZE SECURE SESSION (Restores data & ID)
init_session_state()

st.title("⚙️ Settings")

st.subheader("API Configuration")
st.markdown("FitAI uses Google's Gemini API to generate intelligent plans.")

api_key = st.text_input("Enter Gemini API Key", type="password", value=st.session_state.get('api_key', ''))

if st.button("Save API Key"):
    st.session_state.api_key = api_key
    
    # Save to JSON using the URL ID
    current_user_id = st.session_state.user_id
    save_user_data(current_user_id, "api_key", api_key)
    
    st.success("API Key saved securely!")

st.markdown("---")
st.subheader("Data Management")
if st.button("Reset My Data", type="primary"):
    current_user_id = st.session_state.user_id
    
    # Clear data in the JSON file ONLY for this user
    save_user_data(current_user_id, "user_profile", {})
    save_user_data(current_user_id, "profile_complete", False)
    save_user_data(current_user_id, "api_key", "")
    
    # Clear session state but preserve the ID so they don't break the routing
    st.session_state.user_profile = {}
    st.session_state.profile_complete = False
    st.session_state.api_key = ""
    st.session_state.data_loaded = False
    
    st.success("Your personal data has been wiped. Your session remains active.")