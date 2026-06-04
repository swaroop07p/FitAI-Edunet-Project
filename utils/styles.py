import streamlit as st

def apply_custom_css():
    st.markdown("""
        <style>
        /* Gradient Headers */
        h1, h2, h3 {
            background: -webkit-linear-gradient(45deg, #FF4B4B, #FF8F00);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        /* Stylish Cards for metrics - using theme-aware transparency */
        div[data-testid="metric-container"] {
            background-color: rgba(128, 128, 128, 0.1);
            border-radius: 10px;
            padding: 15px;
            border: 1px solid rgba(128, 128, 128, 0.2);
        }
        /* Button styling */
        .stButton>button {
            border-radius: 20px;
            border: none;
            background: linear-gradient(90deg, #FF4B4B 0%, #FF8F00 100%);
            color: white !important;
            font-weight: bold;
            transition: all 0.3s ease;
        }
        .stButton>button:hover {
            transform: scale(1.05);
            box-shadow: 0 5px 15px rgba(255, 75, 75, 0.4);
        }
        </style>
    """, unsafe_allow_html=True)