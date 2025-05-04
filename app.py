  # CODE FOR Water Potability Predictor
import streamlit as st
import joblib
# import numpy as np

# --- Page Config ---
st.set_page_config(
    page_title="Water Potability Predictor",
    layout="centered",  # Best for responsiveness
    page_icon="💧"
)

# --- Custom CSS ---
st.markdown("""
    <style>
        body {
            background-color: #e6f2ff;
        }
        .main {
            background-color: #ffffff;
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #007acc;
            text-align: center;
            font-size: 2.5rem;
        }
        .stButton > button {
            background-color: #007acc;
            color: white;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# --- App Title ---
st.markdown("<h1>💧 Water Potability Prediction</h1>", unsafe_allow_html=True)

# --- Load Model ---
model = joblib.load("RandomForest")

# --- Input Section ---
columns = [
    "ph", "Hardness", "Solids", "Chloramines", "Sulfate",
    "Conductivity", "Organic_carbon", "Trihalomethanes", "Turbidity"
]

user_inputs = []

st.markdown("### 🧪 Enter the water quality parameters:")
for col in columns:
    val = st.number_input(f"{col}", format="%.1f")
    user_inputs.append(val)

# --- Prediction Button ---
import pandas as pd

if st.button("Check Potability 💡"):
    input_df = pd.DataFrame([user_inputs], columns=columns)
    prediction = model.predict(input_df)[0]
    proba = model.predict_proba(input_df)[0][1]
    if prediction == 1:
        st.success("✅ The water is *Potable* (Safe to drink).")
    else:
        st.error("🚫 The water is *Not Potable* (Unsafe to drink).")




