import streamlit as st
import numpy as np
import joblib

# --- 1. Load the Model and Scaler ---
model = joblib.load('pulsar_model.pkl')
scaler = joblib.load('pulsar_scaler.pkl')

# Hardcode the optimal threshold you discovered
OPTIMAL_THRESHOLD = 0.84

# --- 2. Build the Web App UI ---
st.title("🌌 Pulsar Star Predictor")
st.write("""
Enter the statistical characteristics of a radio frequency signal below. 
This model will predict whether the signal is a **Pulsar Star** or just **Background Space Noise**, 
using a heavily tuned Logistic Regression model optimized for imbalanced astrophysics data.
""")

st.header("Input Signal Characteristics")

# Create columns for a cleaner layout
col1, col2 = st.columns(2)

with col1:
    mean_ip = st.number_input("Mean of the Integrated Profile", value=100.0)
    std_ip = st.number_input("Std Dev of the Integrated Profile", value=45.0)
    kurtosis_ip = st.number_input("Excess Kurtosis of Integrated Profile", value=0.5)
    skewness_ip = st.number_input("Skewness of Integrated Profile", value=1.0)

with col2:
    mean_dm = st.number_input("Mean of the DM-SNR Curve", value=3.0)
    std_dm = st.number_input("Std Dev of the DM-SNR Curve", value=15.0)
    kurtosis_dm = st.number_input("Excess Kurtosis of DM-SNR Curve", value=8.0)
    skewness_dm = st.number_input("Skewness of DM-SNR Curve", value=90.0)

# --- 3. Prediction Logic ---
if st.button("Classify Signal"):
    # Group the inputs into a numpy array (must match the order of your training data!)
    features = np.array([[mean_ip, std_ip, kurtosis_ip, skewness_ip, 
                          mean_dm, std_dm, kurtosis_dm, skewness_dm]])
    
    # Scale the new data using the saved scaler
    scaled_features = scaler.transform(features)
    
    # Get the probability of being a Pulsar (Class 1)
    probability = model.predict_proba(scaled_features)[0][1]
    
    st.markdown("---")
    st.subheader("Results:")
    
    # Apply your custom threshold
    if probability >= OPTIMAL_THRESHOLD:
        st.success(f"🌠 **PULSAR DETECTED!**")
        st.write(f"The model is highly confident. Probability score: **{probability:.2f}** (Threshold: {OPTIMAL_THRESHOLD})")
    else:
        st.warning(f"📻 **Background Noise.**")
        st.write(f"This is likely space noise/RFI. Probability score: **{probability:.2f}** (Threshold: {OPTIMAL_THRESHOLD})")