"# AI-SOC-ANALYSIS" 
# 🛡️ AI SOC Assistant

An AI-powered Security Operations Center (SOC) Assistant that automatically analyzes cybersecurity log files and classifies security events as **Benign**, **Suspicious**, or **Malicious** using Machine Learning.

---

## 📌 Problem Statement

Modern organizations generate a huge volume of security logs from firewalls, servers, applications, and network devices. Manually analyzing these logs is time-consuming, error-prone, and can delay the detection of cyber threats.

The AI SOC Assistant automates security log analysis using Artificial Intelligence and Machine Learning to identify suspicious activities, classify threats based on severity, and assist security teams in faster incident response.

---

## 🚀 Features

- Upload cybersecurity log files (.csv)
- AI-based threat detection
- Classifies security events into:
  - Benign
  - Suspicious
  - Malicious
- Interactive security dashboard
- Threat distribution visualization
- Machine Learning-based predictions
- Reduces manual log analysis effort

---

## 🧠 Machine Learning Model

- **Algorithm:** Random Forest Classifier
- **Accuracy:** 97.66%
- **Task:** Multi-class threat classification

The model analyzes security log patterns and predicts the possible threat category.

---

## 🛠️ Tech Stack

### Programming & Frameworks
- Python
- Streamlit

### Data Processing
- Pandas
- NumPy

### Machine Learning
- Scikit-learn
- Random Forest Classifier
- Joblib

### Visualization
- Plotly

---

## 📂 Project Structure

```
AI-SOC-ANALYSIS/
│
├── app.py                 # Streamlit application
├── train_model.py         # Model training script
├── soc_model.pkl          # Trained ML model
├── target_encoder.pkl     # Label encoder
├── requirements.txt       # Dependencies
├── README.md
│
└── .streamlit/
    └── config.toml
```

---

## ⚙️ Installation & Usage

Clone the repository:

```bash
git clone https://github.com/fiz679/AI-SOC-ANALYSIS.git
```

Navigate to the project directory:

```bash
cd AI-SOC-ANALYSIS
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## 📊 Dataset

**Dataset:** Cybersecurity Threat Detection Logs

The dataset contains security event information such as:
- Network protocols
- Source and destination information
- Actions
- Log types
- Threat labels
- User activity patterns

The dataset is not included in this repository because it exceeds GitHub's file size limitations.

---

## 🔮 Future Enhancements

- Real-time security log monitoring
- SIEM platform integration
- Automated threat alerts
- Explainable AI (XAI) for prediction reasoning
- Deep Learning-based threat detection
- Real-time SOC dashboard

---

## 👥 Project Team

This project was developed as a collaborative academic project by students from the Computer Science and Engineering department.

| Name | Department | Role |
|------|------------|------|
| **Fiza Fathima** | CSE (Cybersecurity) | Team Leader |
| **Fouziya Tabasum** | CSE | Team Member |
| **Bushra Tarannum** | CSE | Team Member |
| **Sadiya Banu** | CSE | Team Member |

---

## 🎓 Institution

**Ghousia College of Engineering**  
Department of Computer Science and Engineering
