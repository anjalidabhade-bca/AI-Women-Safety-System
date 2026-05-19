# 🛡 AI-Powered Smart Women Safety Intelligence System

An advanced AI-based women safety web application designed to provide real-time emergency assistance, intelligent risk prediction, distress detection, and live safety monitoring using Machine Learning and modern web technologies.

---

# 🚀 Features

## 🔴 Emergency SOS System
- One-click emergency alert
- Live location sharing
- Emergency siren/alarm activation
- Continuous tracking mode

---

## 🧠 AI-Based Risk Prediction
- Predicts unsafe areas using Machine Learning
- Uses historical crime data
- Generates risk levels:
  - Low
  - Medium
  - High

---

## 📍 Live Heatmap Visualization
- Interactive map with heatmap zones
- Real-time incident updates
- Displays dangerous locations visually

---

## 💬 Distress Detection (NLP)
- Detects fear/panic messages
- AI analyzes distress probability
- Auto-triggers emergency actions

---

## ⚖ Women Safety Laws Section
- Important women protection laws
- Awareness and legal guidance

---

## 📘 Safety Instructions Section
- Emergency safety guidance
- Self-protection instructions
- Quick help information

---

## 📡 Real-Time Monitoring
- Live location updates
- Motion detection support
- Real-time dashboard visualization

---

# 🛠 Technologies Used

## Frontend
- HTML
- CSS
- JavaScript
- Leaflet.js
- Socket.IO

## Backend
- Python
- Flask

## Database
- MySQL
- mysql-connector-python

## Machine Learning
- Scikit-learn
- NLP
- Random Forest Classifier
- Logistic Regression

## APIs & Maps
- Google Maps API
- Leaflet Heatmaps

---

# 🧠 AI Models Used

## 1️⃣ Crime Risk Prediction Model
Predicts unsafe areas using:
- Location
- Time
- Crime frequency

### Algorithm:
- Random Forest Classifier

---

## 2️⃣ Distress Detection Model
Detects panic/distress messages using NLP.

### Algorithm:
- Logistic Regression
- TF-IDF Vectorizer

---

# 📂 Project Structure

```bash
AI_Women_Safety_System/
│
├── app.py
├── crime_model.py
├── distress_model.py
├── crime_data.csv
│
├── templates/
│   ├── dashboard.html
│   ├── login.html
│   ├── register.html
│   ├── laws.html
│   ├── instructions.html
│
├── static/
│   ├── style.css
│   ├── script.js
│   ├── logo.png
│   ├── sidebar_logo.png
│   ├── sounds/
│       └── sos.mp3
```

---

# ⚙ Installation

## 1️⃣ Clone Project

```bash
git clone https://github.com/yourusername/AI_Women_Safety_System.git
```

---

## 2️⃣ Install Dependencies

```bash
pip install flask mysql-connector-python pandas scikit-learn flask-socketio
```

---

## 3️⃣ Configure MySQL Database

Create database:

```sql
CREATE DATABASE women_safety_system;
USE women_safety_system;
```

Create tables:

```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(255),
    phone VARCHAR(20)
);

CREATE TABLE incidents (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    latitude FLOAT,
    longitude FLOAT,
    risk_level VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE distress_logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    message TEXT,
    distress_score FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

# ▶ Run Project

## Train AI Models

```bash
python crime_model.py
python distress_model.py
```

## Start Flask Server

```bash
python app.py
```

---

# 🌐 Open in Browser

```bash
http://127.0.0.1:5007
```

---

# 🔥 Future Enhancements

- Mobile App Integration
- AI Camera Monitoring
- Face Recognition
- Voice Distress Detection
- Real-Time SMS Alerts
- Predictive Crime Analytics
- AI Chatbot Support

---

# 🎯 Project Objectives

- Enhance women safety using AI
- Provide real-time emergency response
- Predict unsafe areas intelligently
- Improve public safety awareness

---

# 👨‍💻 Developed By

Your Name Here

---

# 📜 License

This project is developed for educational and research purposes.

---

# ⭐ Impact

This project combines:
- Artificial Intelligence
- Real-Time Monitoring
- Safety Automation
- Predictive Analytics

to create a smart women safety ecosystem.