import streamlit as st
import pandas as pd
import joblib
import plotly.express as px

# Load Model
model = joblib.load("soc_model.pkl")
target_encoder = joblib.load("target_encoder.pkl")

st.set_page_config(page_title="AI SOC Assistant", layout="wide")

st.title("🛡️ AI SOC Assistant")
st.subheader("Intelligent Security Log Analysis using Machine Learning")

uploaded_file = st.file_uploader(
    "Upload Security Log CSV",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.write("File uploaded successfully!")
st.write(df.shape)
 st.success("Dataset uploaded successfully!")

    st.write("### Uploaded Dataset")
    st.dataframe(df.head())

    # Copy dataframe
    data = df.copy()

    # Drop unnecessary columns
    data = data.drop(
        columns=["timestamp", "source_ip", "dest_ip"],
        errors="ignore"
    )

    # Encode categorical columns
    categorical_columns = [
        "protocol",
        "action",
        "log_type",
        "user_agent",
        "request_path"
    ]

    for col in categorical_columns:
        if col in data.columns:
            data[col] = data[col].astype("category").cat.codes

    # Remove label column if present
    if "threat_label" in data.columns:
        data = data.drop(columns=["threat_label"])

    # Prediction
    predictions = model.predict(data)
   st.write("Prediction is about to start...")
    labels = target_encoder.inverse_transform(predictions)
    df["Predicted Threat"] = labels

    st.write("## AI Prediction")
    st.dataframe(df.head(20))

    # Dashboard
    benign = (df["Predicted Threat"] == "benign").sum()
    suspicious = (df["Predicted Threat"] == "suspicious").sum()
    malicious = (df["Predicted Threat"] == "malicious").sum()

    c1, c2, c3 = st.columns(3)

    c1.metric("Benign", benign)
    c2.metric("Suspicious", suspicious)
    c3.metric("Malicious", malicious)

    chart = px.bar(
        x=["Benign", "Suspicious", "Malicious"],
        y=[benign, suspicious, malicious],
        title="Threat Distribution"
    )

    st.plotly_chart(chart, use_container_width=True)