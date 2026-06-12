import streamlit as st
from utils.styles import apply_custom_css
from utils.gemini_helper import init_session_state, save_user_data

# 1. PAGE CONFIG MUST BE FIRST
st.set_page_config(page_title="Profile Setup - FitAI", page_icon="👤", layout="wide")

# 2. APPLY STYLES
apply_custom_css()

# 3. INITIALIZE SECURE SESSION (Restores data & ID)
init_session_state()

st.title("👤 User Profile Setup")
st.markdown("Tell us about yourself so our AI can craft the perfect plan for you.")

with st.form("profile_form"):
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("Basic Info")
        name = st.text_input("Full Name", value=st.session_state.user_profile.get("name", ""))
        age = st.number_input("Age", min_value=16, max_value=100, value=st.session_state.user_profile.get("age", 20))
        
        # Helper to get the correct index for selectboxes based on saved data
        gender_options = ["Male", "Female", "Other"]
        saved_gender = st.session_state.user_profile.get("gender", "Male")
        gender_idx = gender_options.index(saved_gender) if saved_gender in gender_options else 0
        gender = st.selectbox("Gender", gender_options, index=gender_idx)
        
        height = st.number_input("Height (cm)", min_value=100, max_value=250, value=st.session_state.user_profile.get("height", 170))
        weight = st.number_input("Weight (kg)", min_value=30, max_value=200, value=st.session_state.user_profile.get("weight", 65))
        
    with col2:
        st.subheader("Fitness Goals")
        goal_opts = ["Weight Loss", "Muscle Gain", "Fat Loss", "General Fitness", "Endurance"]
        saved_goal = st.session_state.user_profile.get("goal", "General Fitness")
        goal_idx = goal_opts.index(saved_goal) if saved_goal in goal_opts else 3
        goal = st.selectbox("Primary Goal", goal_opts, index=goal_idx)
        
        fit_lvl_opts = ["Beginner", "Intermediate", "Advanced"]
        saved_fit = st.session_state.user_profile.get("fitness_level", "Beginner")
        fitness_level = st.select_slider("Current Fitness Level", options=fit_lvl_opts, value=saved_fit)
        
        equip_opts = ["No Equipment", "Dumbbells", "Resistance Bands", "Gym Access", "Yoga Mat"]
        saved_equip = st.session_state.user_profile.get("equipment", "No Equipment")
        equip_idx = equip_opts.index(saved_equip) if saved_equip in equip_opts else 0
        equipment = st.selectbox("Available Equipment", equip_opts, index=equip_idx)
        
        days_available = st.slider("Workout Days per Week", 1, 7, st.session_state.user_profile.get("days_available", 4))
        
        dur_opts = ["15 mins", "30 mins", "45 mins", "60+ mins"]
        saved_dur = st.session_state.user_profile.get("duration", "45 mins")
        dur_idx = dur_opts.index(saved_dur) if saved_dur in dur_opts else 2
        duration = st.selectbox("Time per Session", dur_opts, index=dur_idx)

    with col3:
        st.subheader("Dietary Profile")
        diet_opts = ["Vegetarian", "Vegan", "Non-Vegetarian", "Eggetarian"]
        saved_diet = st.session_state.user_profile.get("diet_type", "Vegetarian")
        diet_idx = diet_opts.index(saved_diet) if saved_diet in diet_opts else 0
        diet_type = st.selectbox("Diet Type", diet_opts, index=diet_idx)
        
        cultural_preference = st.text_input("Cultural Food Preference", value=st.session_state.user_profile.get("cultural_preference", ""), placeholder="e.g., South Indian, Mediterranean")
        
        budg_opts = ["Low", "Medium", "High"]
        saved_budg = st.session_state.user_profile.get("budget", "Low")
        budg_idx = budg_opts.index(saved_budg) if saved_budg in budg_opts else 0
        budget = st.selectbox("Student Budget Level", budg_opts, index=budg_idx)
        
        allergies = st.text_input("Food Allergies (if any)", value=st.session_state.user_profile.get("allergies", ""))
        medical = st.text_input("Medical Conditions", value=st.session_state.user_profile.get("medical_conditions", ""))

    submitted = st.form_submit_button("Save & Generate Profile 💾")

    if submitted:
        bmi = round(weight / ((height/100)**2), 2)
        
        profile_data = {
            "name": name, "age": age, "gender": gender, "height": height, "weight": weight, "bmi": bmi,
            "goal": goal, "fitness_level": fitness_level, "equipment": equipment, "days_available": days_available,
            "duration": duration, "diet_type": diet_type, "cultural_preference": cultural_preference,
            "budget": budget, "allergies": allergies, "medical_conditions": medical
        }
        
        # 1. Update active session
        st.session_state.user_profile = profile_data
        st.session_state.profile_complete = True
        
        # 2. Save securely to JSON file using the current user's unique ID
        current_user_id = st.session_state.user_id
        save_user_data(current_user_id, "user_profile", profile_data)
        save_user_data(current_user_id, "profile_complete", True)
        
        st.success(f"Profile saved successfully! Your BMI is {bmi}.")
        st.balloons()