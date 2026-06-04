import streamlit as st
import matplotlib.pyplot as plt
from utils.styles import apply_custom_css

st.set_page_config(page_title="BMI & Health - FitAI", page_icon="⚖️", layout="wide")
apply_custom_css()

st.title("⚖️ BMI & Health Analysis")

if not st.session_state.get('profile_complete', False):
    st.info("👋 Please complete your profile setup first to view your BMI analysis.")
    st.stop()

profile = st.session_state.user_profile
bmi = profile.get('bmi', 0)

# Determine BMI Category
if bmi < 18.5:
    category = "Underweight"
    color = "#3498db"
    advice = "Focus on a caloric surplus with nutrient-dense foods like nuts, dairy, and lean proteins to build healthy mass safely."
elif 18.5 <= bmi < 24.9:
    category = "Normal weight"
    color = "#2ecc71"
    advice = "Great job! Maintain your current balanced lifestyle, focusing on consistency in your workouts and diet."
elif 25 <= bmi < 29.9:
    category = "Overweight"
    color = "#f1c40f"
    advice = "Incorporate more cardiovascular exercises and monitor your daily caloric intake to reach a comfortable weight."
else:
    category = "Obese"
    color = "#e74c3c"
    advice = "Prioritize low-impact exercises (like swimming or cycling) and focus on a structured caloric deficit plan."

col1, col2 = st.columns([1, 1.5])

with col1:
    st.markdown(f"### Your BMI: **{bmi}**")
    st.markdown(f"### Category: <span style='color:{color}'>**{category}**</span>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown(f"**Health Suggestion:**\n{advice}")
    
    st.markdown("### Daily Targets")
    st.metric("Recommended Water Intake", "3.0 - 3.5 Liters")
    st.metric("Sleep Goal", "7 - 8 Hours")

with col2:
    st.markdown("### BMI Scale Chart")
    fig, ax = plt.subplots(figsize=(8, 3))
    
    # Make chart background transparent for Light/Dark mode compatibility
    fig.patch.set_alpha(0.0)
    ax.set_facecolor((0, 0, 0, 0))
    
    categories_list = ['Underweight', 'Normal', 'Overweight', 'Obese']
    ranges = [18.5, 6.4, 5.0, 10.1] # Block widths
    colors = ['#3498db', '#2ecc71', '#f1c40f', '#e74c3c']
    
    left = 0
    for i in range(len(ranges)):
        ax.barh(0, ranges[i], left=left, color=colors[i], height=0.5, label=categories_list[i])
        left += ranges[i]
        
    # Draw user's BMI indicator
    ax.axvline(x=bmi, color='gray', linestyle='-', linewidth=4, label='Your BMI')
    ax.text(bmi, 0.35, f' {bmi}', va='center', fontweight='bold', color='gray')
    
    ax.set_yticks([])
    ax.set_xlim(10, 40)
    ax.set_xlabel('BMI Value', color='gray')
    ax.tick_params(colors='gray')
    
    for spine in ax.spines.values():
        spine.set_edgecolor('gray')
        
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.3), ncol=4, frameon=False)
    
    st.pyplot(fig)