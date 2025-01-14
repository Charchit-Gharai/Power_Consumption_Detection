import streamlit as st
import joblib
import numpy as np

# Load the pre-trained Random Forest model

model = joblib.load("random_forest_regressor_model.joblib")

# Enhanced CSS styling
st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #fdfbfb 0%, #ebedee 100%);
        font-family: 'Arial', sans-serif;
    }
    h1 {
        text-align: center;
        color: #1a73e8;
        font-size: 2.5rem;
        margin-bottom: 20px;
    }
    .stNumberInput > div > div > input {
        background-color: #f1f3f4;
        border-radius: 5px;
        padding: 10px;
        border: none;
        box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);
        transition: box-shadow 0.3s ease;
    }
    .stNumberInput > div > div > input:focus {
        box-shadow: 0px 0px 8px rgba(26, 115, 232, 0.7);
    }
    .stButton button {
        background-color: #1a73e8;
        color: white;
        font-size: 16px;
        padding: 10px 20px;
        border-radius: 5px;
        transition: background-color 0.3s ease;
    }
    .stButton button:hover {
        background-color: #174ea6;
    }
    .result-card {
        background-color: #f1f8ff;
        border-left: 4px solid #1a73e8;
        padding: 15px;
        border-radius: 5px;
        font-size: 1.2em;
        color: #333;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# App title
st.title("⚡ SMART METER ⚡")

# User input section
st.markdown("""
    <div style="text-align: center; font-size: 1.5rem; font-weight: bold; color: #333333;">
        Enter the Values:
    </div>
""", unsafe_allow_html=True)

# User input section
voltage = st.number_input("Voltage (V)", min_value=0.0, max_value=500.0, value=0.0, step=0.1)
current = st.number_input("Current (A)", min_value=0.0, max_value=100.0, value=0.0, step=0.1)
sub_metering_1 = st.number_input("Sub Metering 1 (W)", min_value=0.0, max_value=100.0, value=0.0, step=0.1)
sub_metering_2 = st.number_input("Sub Metering 2 (W)", min_value=0.0, max_value=100.0, value=0.0, step=0.1)
sub_metering_3 = st.number_input("Sub Metering 3 (W)", min_value=0.0, max_value=100.0, value=0.0, step=0.1)

# Prediction button
if st.button("Predict"):
    try:
        with st.spinner("Analyzing..."):
            # Prepare the input data for prediction
            input_data = np.array([[voltage, current, sub_metering_1, sub_metering_2, sub_metering_3]])

            # Display the input data in one line with labels and units
            st.markdown("### Input Data for Prediction:")
            st.write(f"**Voltage:** {voltage} V, **Current:** {current} A, **Sub Metering 1:** {sub_metering_1} W, **Sub Metering 2:** {sub_metering_2} W, **Sub Metering 3:** {sub_metering_3} W")
            
            # Predict using the loaded model
            prediction = model.predict(input_data)[0]
            
            # Display the result
            st.markdown(f"""
                <div class="result-card">
                    <strong>Predicted Power Consumption:</strong> {prediction:.2f} kW/hr
                </div>
            """, unsafe_allow_html=True)
    except Exception as e:
        # Display the error if prediction fails
        st.error(f"❌ An error occurred during prediction: {e}")


