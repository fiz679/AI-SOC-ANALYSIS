# ==========================================
# AI SOC Assistant - Train AI Model
# ==========================================

import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

print("=" * 60)
print("      AI SOC Assistant - Model Training")
print("=" * 60)

# ------------------------------------------
# Load Dataset
# ------------------------------------------

print("\nLoading dataset...")

df = pd.read_csv("cybersecurity_threat_detection_logs.csv")

# Use only 100000 records for faster training
df = df.sample(n=100000, random_state=42)

print("Dataset Loaded Successfully!")
print("Dataset Shape:", df.shape)

# ------------------------------------------
# Encode Categorical Features
# ------------------------------------------

label_encoders = {}

categorical_columns = [
    "protocol",
    "action",
    "log_type",
    "user_agent",
    "request_path"
]

for col in categorical_columns:
    encoder = LabelEncoder()
    df[col] = encoder.fit_transform(df[col])
    label_encoders[col] = encoder

# Encode Target

target_encoder = LabelEncoder()

df["threat_label"] = target_encoder.fit_transform(df["threat_label"])

# ------------------------------------------
# Features & Target
# ------------------------------------------

X = df.drop(
    columns=[
        "timestamp",
        "source_ip",
        "dest_ip",
        "threat_label"
    ]
)

y = df["threat_label"]

# ------------------------------------------
# Split Dataset
# ------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ------------------------------------------
# Train AI Model
# ------------------------------------------

print("\nTraining Random Forest Model...")

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

print("Training Complete!")

# ------------------------------------------
# Evaluate
# ------------------------------------------

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy")

print(f"{accuracy*100:.2f}%")

print("\nClassification Report")

print(classification_report(y_test, y_pred))

# ------------------------------------------
# Save Model
# ------------------------------------------

joblib.dump(model, "soc_model.pkl")
joblib.dump(target_encoder, "target_encoder.pkl")

print("\nModel Saved Successfully!")