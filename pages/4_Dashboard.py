import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from utils.styles import apply_custom_css
from utils.gemini_helper import init_session_state

# This single line handles everything securely!
st.set_page_config(page_title="Dashboard - FitAI", page_icon="📊", layout="wide")

apply_custom_css()

init_session_state()

# Initialize session state variables if they don't exist
if 'user_profile' not in st.session_state:
    st.session_state.user_profile = {}
if 'profile_complete' not in st.session_state:
    st.session_state.profile_complete = False
if 'api_key' not in st.session_state:
    st.session_state.api_key = ""

st.markdown('<div class="title-container">📊 <span class="gradient-text">Progress Dashboard</span></div>', unsafe_allow_html=True)
# st.title("📊 Progress Dashboard")

if not st.session_state.get('profile_complete', False):
    st.warning("Complete your profile to see your dashboard.")
    st.stop()

profile = st.session_state.user_profile

col1, col2, col3, col4 = st.columns(4)
col1.metric("Current Weight", f"{profile['weight']} kg")
col2.metric("Current BMI", profile['bmi'])
col3.metric("Water Intake Goal", "3 Liters")
col4.metric("Workout Consistency", "85%", "+5%")

st.markdown("### Weekly Tracking")
# Mock data for demonstration purposes
dates = pd.date_range(end=pd.Timestamp.today(), periods=7)
mock_weights = [profile['weight'] + 1, profile['weight'] + 0.8, profile['weight'] + 0.5, profile['weight'] + 0.5, profile['weight'] + 0.2, profile['weight'], profile['weight'] - 0.2]

df = pd.DataFrame({'Date': dates, 'Weight (kg)': mock_weights})

fig, ax = plt.subplots(figsize=(10, 4))
fig.patch.set_facecolor('#0E1117')
ax.set_facecolor('#0E1117')
ax.plot(df['Date'], df['Weight (kg)'], marker='o', color='#FF4B4B', linewidth=2)
ax.set_title("Weight Progress (Last 7 Days)", color='white')
ax.tick_params(colors='white')
for spine in ax.spines.values(): spine.set_edgecolor('#555')

st.pyplot(fig)

with st.expander("Log Daily Activity"):
    st.checkbox("Completed Workout Today")
    st.slider("Water Glasses Logged", 0, 15, 5)
    st.button("Save Daily Log")