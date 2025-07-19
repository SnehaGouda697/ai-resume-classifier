# 🧠 AI Resume Classifier

A simple AI-based resume classification tool that predicts whether a resume should be **shortlisted** or **rejected** based on keywords and text content. Built using **Python**, **Flask**, and a **rule-based model**.

---

## 🚀 Features

- Accepts resume text input
- Uses a basic rule-based classifier (keywords like "python", "project", etc.)
- API built with Flask
- Returns JSON response or integrates with an HTML frontend

---

## 🛠️ Tech Stack

- Python
- Flask
- Pandas
- Scikit-learn (for interface only)
- HTML/CSS (basic frontend)

---

## 📁 Folder Structure
i-resume-classifier/
│
├── model/
│ ├── train_model.py # Trains and saves the model
│ └── resume_classifier.pkl # Saved model
│
├── static/
│ └── style.css # Optional styling
│
├── templates/
│ └── index.html # Frontend UI
│
├── app.py # Flask backend API
├── resume_data.csv # Sample labeled data
├── test_api.py # Python script to test the API
└── README.md # Project description
