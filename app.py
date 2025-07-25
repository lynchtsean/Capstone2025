import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'antoine'))

from flask import Flask, render_template, request, redirect, url_for
from threading import Timer
from datetime import datetime, timedelta
import requests  # Needed to send requests to AWS API
from s3_helpers import get_subscribers, save_subscribers



app = Flask(__name__)

def send_reminder(email, message):
    aws_url = "https://your-aws-endpoint.example.com/send"
    payload = {"email": email, "message": message}
    try:
        requests.post(aws_url, json=payload)
    except Exception as e:
        app.logger.error(f"Failed to send reminder: {e}")

def schedule_reminder(email, message, send_time_str):
    # Parse the user’s requested time (format: "YYYY-MM-DD HH:MM")
    send_time = datetime.strptime(send_time_str, "%Y-%m-%d %H:%M")
    delay = (send_time - datetime.now()).total_seconds()

    if delay <= 0:
        raise ValueError("Send time must be in the future")

    # Start a background thread that will call send_reminder()
    Timer(delay, send_reminder, args=(email, message)).start()

@app.route("/reminders", methods=["POST"])
def create_reminder():
    email = request.form["email"]
    message = request.form["message"]
    send_time = request.form["send_time"]  # match your form field name

    try:
        schedule_reminder(email, message, send_time)
    except ValueError as err:
        return render_template("error.html", error=str(err)), 400

    return redirect(url_for("confirmation"))

# 🏠 Homepage route
@app.route("/")
def home():
    return render_template("index.html")

# 📬 Reminder route that gets triggered when the button is clicked
@app.route("/send-reminder", methods=["POST"])
def trigger_reminder():
    api_url = "https://yaikepg1ej.execute-api.us-east-1.amazonaws.com/send-reminder"
    response = requests.post(api_url)

    message = "Reminder sent successfully!" if response.status_code == 200 else f"Failed to send reminder – {response.status_code}"
    return render_template("index.html", message=message)

# 📥 Subscribe route that saves user info to S3
@app.route("/subscribe", methods=["POST"])
def subscribe():
    email = request.form.get("email")
    phone = request.form.get("phone")

    # Fetch current subscribers from S3
    subscribers = get_subscribers()

    # Update or add the new subscriber
    subscribers[email] = {
        "phone": phone,
        "enabled": True
    }

    # Save updated subscribers back to S3
    save_subscribers(subscribers)

    return render_template("success.html", email=email)

# 🧪 Run the app locally
if __name__ == "__main__":
    app.run(debug=True)

# trigger deploy
