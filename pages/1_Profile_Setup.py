import streamlit as st
from utils.styles import apply_custom_css

st.set_page_config(page_title="Profile Setup - FitAI", page_icon="👤", layout="wide")
apply_custom_css()

st.title("👤 User Profile Setup")
st.markdown("Tell us about yourself so our AI can craft the perfect plan for you.")

with st.form("profile_form"):
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("Basic Info")
        name = st.text_input("Full Name", value=st.session_state.user_profile.get("name", ""))
        age = st.number_input("Age", min_value=16, max_value=100, value=st.session_state.user_profile.get("age", 20))
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
        height = st.number_input("Height (cm)", min_value=100, max_value=250, value=st.session_state.user_profile.get("height", 170))
        weight = st.number_input("Weight (kg)", min_value=30, max_value=200, value=st.session_state.user_profile.get("weight", 65))
        
    with col2:
        st.subheader("Fitness Goals")
        goal = st.selectbox("Primary Goal", ["Weight Loss", "Muscle Gain", "Fat Loss", "General Fitness", "Endurance"])
        fitness_level = st.select_slider("Current Fitness Level", options=["Beginner", "Intermediate", "Advanced"])
        equipment = st.selectbox("Available Equipment", ["No Equipment", "Dumbbells", "Resistance Bands", "Gym Access", "Yoga Mat"])
        days_available = st.slider("Workout Days per Week", 1, 7, 4)
        duration = st.selectbox("Time per Session", ["15 mins", "30 mins", "45 mins", "60+ mins"])

    with col3:
        st.subheader("Dietary Profile")
        diet_type = st.selectbox("Diet Type", ["Vegetarian", "Vegan", "Non-Vegetarian", "Eggetarian"])
        # Adding local cultural preferences context
        cultural_preference = st.text_input("Cultural Food Preference", value="e.g., South Indian, North Indian, Mediterranean", help="E.g., specific coastal dishes like Neer Dosa or Fish Curry, or standard hostel mess food.")
        budget = st.selectbox("Student Budget Level", ["Low", "Medium", "High"])
        allergies = st.text_input("Food Allergies (if any)", placeholder="e.g., Peanuts, Dairy")
        medical = st.text_input("Medical Conditions", placeholder="e.g., Asthma, Knee pain")

    submitted = st.form_submit_button("Save & Generate Profile 💾")

    if submitted:
        bmi = round(weight / ((height/100)**2), 2)
        
        profile_data = {
            "name": name, "age": age, "gender": gender, "height": height, "weight": weight, "bmi": bmi,
            "goal": goal, "fitness_level": fitness_level, "equipment": equipment, "days_available": days_available,
            "duration": duration, "diet_type": diet_type, "cultural_preference": cultural_preference,
            "budget": budget, "allergies": allergies, "medical_conditions": medical
        }
        
        st.session_state.user_profile = profile_data
        st.session_state.profile_complete = True
        
        # --- NEW: Save to local file ---
        import json
        import os
        
        # Load existing data first so we don't overwrite the API key
        local_data = {}
        if os.path.exists("user_data.json"):
            with open("user_data.json", "r") as f:
                local_data = json.load(f)
                
        local_data["user_profile"] = profile_data
        local_data["profile_complete"] = True
        
        with open("user_data.json", "w") as f:
            json.dump(local_data, f)
        # -------------------------------
        
        st.success(f"Profile saved successfully! Your BMI is {bmi}.")
        st.balloons()