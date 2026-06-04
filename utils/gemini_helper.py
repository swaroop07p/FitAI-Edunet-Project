import google.generativeai as genai
import streamlit as st
import json
import os

# Helper to load saved data
def load_local_data():
    if os.path.exists("user_data.json"):
        try:
            with open("user_data.json", "r") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}

def configure_gemini():
    # 1. Try session state first
    api_key = st.session_state.get('api_key', '')
    
    # 2. Try loading from local JSON file if session state is empty (e.g., after refresh)
    if not api_key:
        local_data = load_local_data()
        api_key = local_data.get('api_key', '')
        st.session_state.api_key = api_key # Restore to session
        
    # 3. Try Streamlit secrets safely (prevents the crash)
    try:
        if not api_key and 'API_KEY' in st.secrets:
            api_key = st.secrets["API_KEY"]
    except Exception:
        pass # It is completely fine if the secrets file doesn't exist
        
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