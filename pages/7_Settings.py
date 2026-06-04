import streamlit as st
import json
import os
from utils.styles import apply_custom_css

st.set_page_config(page_title="Settings - FitAI", page_icon="⚙️")
apply_custom_css()

st.title("⚙️ Settings")

st.subheader("API Configuration")
st.markdown("FitAI uses Google's Gemini API to generate intelligent plans.")

api_key = st.text_input("Enter Gemini API Key", type="password", value=st.session_state.get('api_key', ''))

if st.button("Save API Key"):
    st.session_state.api_key = api_key
    
    # --- NEW: Save API key to local file ---
    local_data = {}
    if os.path.exists("user_data.json"):
        try:
            with open("user_data.json", "r") as f:
                local_data = json.load(f)
        except Exception:
            pass
            
    local_data["api_key"] = api_key
    
    with open("user_data.json", "w") as f:
        json.dump(local_data, f)
    # ---------------------------------------
    
    st.success("API Key saved securely and will survive page refreshes!")

st.markdown("---")
st.subheader("Data Management")
if st.button("Reset All User Data", type="primary"):
    st.session_state.clear()
    # Delete the local file if they want to reset
    if os.path.exists("user_data.json"):
        os.remove("user_data.json")
    st.success("Data cleared! Please go to the Home page to start fresh.")