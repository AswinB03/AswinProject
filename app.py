import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load('air_quality_model.pkl')

# Streamlit App UI
st.set_page_config(page_title="Air Quality Predictor", layout="centered")

st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>🌫️ Air Quality Level Predictor</h1>", unsafe_allow_html=True)

st.markdown("### Enter the pollutant values below:")

pm25 = st.slider("PM2.5 (μg/m³)", 0, 500, 50)
pm10 = st.slider("PM10 (μg/m³)", 0, 500, 80)
no2 = st.slider("NO2 (ppb)", 0, 200, 40)
so2 = st.slider("SO2 (ppb)", 0, 200, 20)
co = st.slider("CO (ppm)", 0, 50, 1)
o3 = st.slider("O3 (ppb)", 0, 200, 30)

# Predict Button
if st.button("🔍 Predict AQI"):
    input_data = np.array([[pm25, pm10, no2, so2, co, o3]])
    prediction = model.predict(input_data)[0]

    # Show result
    st.success(f"🌍 Estimated Air Quality Index (AQI): **{round(prediction)}**")

    # Display AQI category
    if prediction <= 50:
        st.info("✅ Good Air Quality")
    elif prediction <= 100:
        st.warning("⚠️ Moderate Air Quality")
    elif prediction <= 150:
        st.error("😷 Unhealthy for Sensitive Groups")
    else:
        st.error("☠️ Unhealthy Air Quality")
      
