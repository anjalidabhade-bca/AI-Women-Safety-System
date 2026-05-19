from flask import Flask, render_template, request, jsonify, redirect, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
import os
from flask_socketio import SocketIO
import pickle
import datetime
import requests
import webbrowser
import urllib.parse
from config import get_db_connection

app = Flask(__name__)
app.secret_key = "women_safety_secret_key"

socketio = SocketIO(app)
ADMIN_EMAIL = "admin"
ADMIN_PASSWORD = "admin123"


# WOMEN HELPLINE


WOMEN_HELPLINE = "1091"


# LOAD ML MODELS

risk_model = pickle.load(open("models/risk_model.pkl","rb"))
distress_model, vectorizer = pickle.load(open("models/distress_model.pkl","rb"))
anomaly_model = pickle.load(open("models/anomaly_model.pkl","rb"))


# FORMAT PHONE NUMBER


def format_number(number):

    number = str(number).strip()

    if not number.startswith("91"):
        number = "91" + number

    return number



# SEND WHATSAPP ALERT


def send_whatsapp(number, message):

    encoded_message = urllib.parse.quote(message)

    whatsapp_url = f"https://wa.me/{number}?text={encoded_message}"

    print("Opening WhatsApp chat for:", number)

    webbrowser.open(whatsapp_url)



# FIND NEAREST POLICE STATION


def find_nearest_police(lat, lon):
    try:
        url = "https://overpass-api.de/api/interpreter"

        query = f"""
        [out:json];
        node["amenity"="police"](around:5000,{lat},{lon});
        out;
        """

        response = requests.get(url, params={'data': query}, timeout=5)
        data = response.json()

        if len(data["elements"]) > 0:
            police = data["elements"][0]

            name = police.get("tags", {}).get("name", "Nearby Police Station")

            plat = police["lat"]
            plon = police["lon"]

            link = f"https://www.google.com/maps?q={plat},{plon}"

            return name, link

    except Exception as e:
        print("Police API error:", e)
        flash("Unable to fetch police location")

    # fallback if error happens
    fallback = f"https://www.google.com/maps/search/police+station/@{lat},{lon},14z"

    return "Nearby Police Station", fallback



# LOGIN PAGE


@app.route("/")
def home():
    return render_template("login.html")



# LOGIN


@app.route("/login", methods=["POST"])
def login():

    email = request.form["email"]
    password = request.form["password"]
    
    if not email or not password:
        flash("Please enter all fields")
        return redirect("/")

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id,name,password FROM users WHERE email=%s",(email,))
    user = cursor.fetchone()

    conn.close()

    if user and check_password_hash(user[2], password):

        session["user_id"] = user[0]
        session["user_name"] = user[1]

        flash("Login Successful")

        return redirect("/dashboard")

    flash("Wrong Email or Password")

    return redirect("/")
    
    
    
#ADMIN LOGIN ROUTE
@app.route("/admin_login", methods=["GET","POST"])
def admin_login():

    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        if email == ADMIN_EMAIL and password == ADMIN_PASSWORD:
            session["admin"] = True
            return redirect("/admin")

        flash("Wrong Admin Credentials")

    return render_template("admin_login.html")
    
    
#LOGOUT FOR ADMIN
@app.route("/admin_logout")
def admin_logout():
    session.pop("admin", None)
    return redirect("/admin_login")



# REGISTER PAGE


@app.route("/register_page")
def register_page():
    return render_template("register.html")



# REGISTER USER

@app.route("/register", methods=["POST"])
def register():

    name = request.form["name"]
    email = request.form["email"]
    password = request.form["password"]
    contact1 = request.form["emergency_contact1"]
    contact2 = request.form["emergency_contact2"]

    #  VALIDATION (ADD HERE)
    if not name or not email or not password:
        flash("All fields are required")
        return redirect("/register_page")

    if "@" not in email:
        flash("Invalid email")
        return redirect("/register_page")

    if len(password) < 6:
        flash("Password must be at least 6 characters")
        return redirect("/register_page")

    # HASH AFTER VALIDATION
    hashed_password = generate_password_hash(password)

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO users
        (name,email,password,emergency_contact1,emergency_contact2)
        VALUES (%s,%s,%s,%s,%s)
    """,(name,email,hashed_password,contact1,contact2))

    conn.commit()
    conn.close()

    flash("Account Created Successfully")

    
    return redirect("/")
    
#ADMIN DASHBOARD PAGE    
    
@app.route("/admin")
def admin():

    if not session.get("admin"):
        return redirect("/admin_login")

    conn = get_db_connection()
    cursor = conn.cursor()

    # Total users
    cursor.execute("SELECT COUNT(*) FROM users")
    total_users = cursor.fetchone()[0]

    # Total incidents
    cursor.execute("SELECT COUNT(*) FROM incidents")
    total_incidents = cursor.fetchone()[0]

    # Risk counts
    cursor.execute("SELECT COUNT(*) FROM incidents WHERE risk_level=0")
    low = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM incidents WHERE risk_level=1")
    medium = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM incidents WHERE risk_level=2")
    high = cursor.fetchone()[0]

    # High risk only
    high_risk = high

    # Recent incidents
    cursor.execute("""
        SELECT latitude, longitude, risk_level, month
        FROM incidents ORDER BY id DESC LIMIT 10
    """)
    incidents = cursor.fetchall()

    conn.close()

    # Dummy forecast
    forecast_labels = ["Jan","Feb","Mar"]
    forecast_values = [210,190,220]

    return render_template(
        "admin.html",
        total_users=total_users,
        total_incidents=total_incidents,
        high_risk=high_risk,
        low=low,
        medium=medium,
        high=high,
        incidents=incidents,
        forecast_labels=forecast_labels,
        forecast_values=forecast_values
    )



#MAIN DASHBOARD


@app.route("/dashboard")
def dashboard():

    if "user_id" not in session:
        return redirect("/")

    return render_template("dashboard.html", name=session["user_name"])
    

# INSTRUCTIONS PAGE


@app.route("/instructions")
def instructions():

    if "user_id" not in session:
        return redirect("/")

    return render_template("instructions.html")
    
#LAWS PAGE   
@app.route("/laws")
def laws():
    return render_template("laws.html")
    
    
#USER PROFILE PAGE   
@app.route("/profile")
def profile():

    if "user_id" not in session:
        return redirect("/")

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT name,email,emergency_contact1,emergency_contact2
    FROM users WHERE id=%s
    """,(session["user_id"],))

    user = cursor.fetchone()

    conn.close()

    return render_template(
        "profile.html",
        name=user[0],
        email=user[1],
        contact1=user[2],
        contact2=user[3]
    )
    

    

# SAFEST ROUTE PAGE


@app.route("/safest_route")
def safest_route():

    if "user_id" not in session:
        return redirect("/")

    return render_template("safe_route.html")



# LIVE TRACKING PAGE


@app.route("/live_tracking")
def live_tracking():
    return render_template("live_tracking.html")


# HEATMAP DATA


@app.route("/heatmap_data")
def heatmap_data():

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT latitude, longitude FROM incidents")

    data = cursor.fetchall()

    conn.close()

    return jsonify(data)



# DISTRESS DETECTION


@app.route("/check_distress", methods=["POST"])
def check_distress():

    data = request.json
    message = data["message"]

    transformed = vectorizer.transform([message])
    prediction = distress_model.predict(transformed)[0]

    distress_flag = True if prediction == 1 else False

    return jsonify({"distress": distress_flag})
    



# SOS + RISK PREDICTION
#LOCATION SHARING ON WHATSAPP

@app.route("/predict_risk", methods=["POST"])
def predict_risk():

    data = request.json

    features = [[data["crime_rate"], data["hour"]]]

    risk = risk_model.predict(features)[0]

    nearest_police, police_link = find_nearest_police(data["lat"], data["lng"])

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO incidents
        (user_id,latitude,longitude,risk_level,crime_rate,hour,month)
        VALUES (%s,%s,%s,%s,%s,%s,%s)
    """,(session.get("user_id",1),
         data["lat"],
         data["lng"],
         risk,
         data["crime_rate"],
         data["hour"],
         datetime.datetime.now().month))

    conn.commit()

    cursor.execute("""
        SELECT emergency_contact1, emergency_contact2
        FROM users WHERE id=%s
    """,(session.get("user_id",1),))

    contact1, contact2 = cursor.fetchone()

    conn.close()

    contact1 = format_number(contact1)
    contact2 = format_number(contact2)

    maps_link = f"https://www.google.com/maps?q={data['lat']},{data['lng']}"

    tracking_link = "http://127.0.0.1:5000/live_tracking"

    message = f"""🚨 EMERGENCY ALERT 🚨

User may be in danger.

Live Location: {maps_link}

Track Live Location: {tracking_link}

Nearest Police Station: {nearest_police}

Police Station Map: {police_link}
"""

    if data.get("first_alert", False):

        send_whatsapp(contact1, message)
        send_whatsapp(contact2, message)

    socketio.emit("new_marker",{
        "lat":data["lat"],
        "lng":data["lng"],
        "risk":risk
    })

    return jsonify({"risk":risk})
    
#USER LOGOUT    
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")



# RUN SERVER


if __name__ == "__main__":
    socketio.run(app, debug=True)