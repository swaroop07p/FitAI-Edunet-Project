import streamlit as st

def apply_custom_css():
    st.markdown("""
        <style>
        /* Target a specific class instead of the whole h1 tag */
        .gradient-text {
            background: -webkit-linear-gradient(45deg, #00F2FE, #4FACFE);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 2.5rem; /* Matches default st.title size */
            font-weight: 700;
            display: inline;
        }
        
        .title-container {
            font-size: 2.25rem;
            font-weight: 700;
            margin-bottom: 1.5rem;
        }
                
        /* H3/Markdown ### Container */
        .h3-container {
            font-size: 0.5rem;  /* Matches Streamlit's default h3/### size */
            font-weight: 600;
            margin-bottom: 0.75rem;
            margin-top: 0.5rem;
        }
        
        /* Gradient Headers */
        h1, h2, h3 {
            /* CHANGED: Swapped orange gradient for Cyan (#00F2FE) to Blue/Teal (#4FACFE) */
            background: -webkit-linear-gradient(45deg, #00F2FE, #4FACFE);
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
            /* CHANGED: Swapped button background to matching Cyan gradient */
            background: linear-gradient(90deg, #00F2FE 0%, #4FACFE 100%);
            color: black !important;
            font-weight: bold;
            transition: all 0.3s ease;
        }
        
        .stButton>button:hover {
            transform: scale(1.05);
            /* CHANGED: Updated the glow effect to use a semi-transparent Cyan (rgba(0, 242, 254, 0.4)) */
            box-shadow: 0 5px 15px rgba(0, 242, 254, 0.4);
        }
        </style>
    """, unsafe_allow_html=True)