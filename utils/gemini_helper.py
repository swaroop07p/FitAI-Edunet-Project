import google.generativeai as genai
import streamlit as st
import json
import os
import uuid

# --- BULLETPROOF SESSION & DATA MANAGER ---
def load_all_users():
    if os.path.exists("user_data.json"):
        try:
            with open("user_data.json", "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

def save_user_data(user_id, key, value):
    users = load_all_users()
    if user_id not in users:
        users[user_id] = {}
    users[user_id][key] = value
    with open("user_data.json", "w") as f:
        json.dump(users, f)

def init_session_state():
    """Flawless session manager that survives sidebar navigation and page refreshes."""
    
    # 1. RESTORE OR CREATE USER ID
    if 'user_id' in st.session_state:
        # If we navigated via sidebar, the URL param drops. Put it back so F5 works.
        if st.query_params.get("user_id") != st.session_state.user_id:
            st.query_params["user_id"] = st.session_state.user_id
            
    elif "user_id" in st.query_params:
        # If we refreshed, session state is empty but URL has the ID. Restore session.
        st.session_state.user_id = st.query_params["user_id"]
        
    else:
        # Brand new visit (New User / Incognito)
        new_id = str(uuid.uuid4())
        st.session_state.user_id = new_id
        st.query_params["user_id"] = new_id
        
    user_id = st.session_state.user_id
    
    # 2. ENSURE CORE DATA STRUCTURES EXIST
    if 'user_profile' not in st.session_state:
        st.session_state.user_profile = {}
    if 'profile_complete' not in st.session_state:
        st.session_state.profile_complete = False
    if 'api_key' not in st.session_state:
        st.session_state.api_key = ""
        
    # 3. LOAD DATA FROM JSON (Only once per session initialization)
    if 'data_loaded' not in st.session_state:
        users = load_all_users()
        user_data = users.get(user_id, {})
        
        st.session_state.user_profile = user_data.get("user_profile", {})
        st.session_state.profile_complete = user_data.get("profile_complete", False)
        st.session_state.api_key = user_data.get("api_key", "")
        st.session_state.data_loaded = True
# ------------------------------------------

def configure_gemini():
    api_key = st.session_state.get('api_key', '')
    if not api_key:
        st.info("ℹ️ Please configure your Gemini API Key in the Settings page.")
        return False
    genai.configure(api_key=api_key)
    return True

def get_gemini_model():
    return genai.GenerativeModel('gemini-2.5-flash')

def generate_workout_plan(profile):
    if not configure_gemini(): return None
    model = get_gemini_model()
    
    prompt = f"""
    You are an expert AI fitness coach. Create a highly personalized weekly workout plan based on this student's profile:
    - Age: {profile.get('age')}, Gender: {profile.get('gender')}
    - Goal: {profile.get('goal')}
    - Fitness Level: {profile.get('fitness_level')}
    - Available Days: {profile.get('days_available')} days/week
    - Duration: {profile.get('duration')} mins/session
    - Equipment: {profile.get('equipment')}
    - Medical Conditions: {profile.get('medical_conditions', 'None')}

    Format the output with clear markdown tables for the schedule. Include warm-ups, specific exercises (sets, reps, rest time), cool-downs, and beginner safety notes.
    """
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error generating plan: {e}"

def generate_diet_plan(profile):
    if not configure_gemini(): return None
    model = get_gemini_model()
    
    prompt = f"""
    You are an expert nutritionist. Create a personalized, budget-friendly 7-day meal plan for a student:
    - Goal: {profile.get('goal')}
    - Diet Type: {profile.get('diet_type')}
    - Cultural Preference: {profile.get('cultural_preference')} (Incorporate authentic local dishes where possible)
    - Budget: {profile.get('budget')}
    - Allergies: {profile.get('allergies', 'None')}

    The meals must be practical for a student lifestyle (affordable, easy to prep, or easy to find in a hostel/canteen). Provide a daily breakdown (Breakfast, Lunch, Snack, Dinner) in markdown tables, and a short affordable grocery shopping list. Ensure protein/carb/fat balance is noted.
    """
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error generating plan: {e}"
        
def generate_daily_tip():
    if not configure_gemini(): return "Stay hydrated and keep moving!"
    try:
        model = get_gemini_model()
        response = model.generate_content("Give me a short, highly motivating 2-sentence fitness or nutrition tip for a college student.")
        return response.text
    except:
        return "Consistency is key. Keep showing up!"