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