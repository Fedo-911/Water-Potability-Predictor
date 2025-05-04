# 💧 Water Potability Predictor

This is a simple and interactive Streamlit web application that predicts the **potability** (drinkability) of water based on various water quality parameters. It uses a pre-trained **Random Forest** model to classify water as potable or not potable.

## 🚀 Features

- Clean and user-friendly web interface
- Accepts user input for key water quality metrics
- Predicts whether the water is safe to drink
- Provides visual feedback with clear result messages
- Responsive and styled with custom CSS for an improved look

## 🧪 Input Parameters

The model uses the following water quality features as input:

- ph – Acidity/alkalinity of water
- Hardness – Concentration of calcium and magnesium
- Solids – Total dissolved solids (TDS)
- Chloramines – Concentration of disinfectants
- Sulfate – Amount of sulfate in water
- Conductivity – Water’s ability to conduct electricity
- Organic_carbon – Organic carbon levels
- Trihalomethanes – Chemical compounds formed during chlorination
- Turbidity – Clarity of water

## 📦 Requirements

- Python 3.7+
- Streamlit
- joblib
- pandas

You can install the dependencies using:

pip install streamlit joblib pandas


📁 Files
app.py – Main Streamlit app

RandomForest – Pre-trained model file (should be in the same directory)

README.md – Project documentation


▶️ How to Run
To run the app locally:
streamlit run app.py
Then open your browser and go to http://localhost:8501

🧠 Model Information
Model Type: Random Forest Classifier

Trained using water quality dataset with labeled potability

Outputs: 0 (Not Potable) or 1 (Potable)

Also provides a probability/confidence score

📌 Notes
Ensure that the RandomForest model file exists and is correctly serialized via joblib.

For deployment (e.g., Streamlit Cloud), make sure to include all necessary files and optionally a requirements.txt.

