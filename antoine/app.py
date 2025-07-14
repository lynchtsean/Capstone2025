from flask import Flask, render_template
import requests  # Needed to send requests to AWS API

app = Flask(__name__)

# 🏠 Homepage route
@app.route("/")
def home():
    return render_template("index.html")

# 📬 Reminder route that gets triggered when the button is clicked
@app.route("/send-reminder", methods=["POST"])
def send_reminder():
    api_url = "https://yaikepg1ej.execute-api.us-east-1.amazonaws.com/send-reminder"
    response = requests.post(api_url)

    if response.status_code == 200:
        message = "Reminder sent successfully!"
    else:
        message = f"Failed to send reminder – {response.status_code}"

    # 🔁 Reloads the homepage and optionally shows feedback
    return render_template("index.html", message=message)

# 🧪 Run the app locally
if __name__ == "__main__":
    app.run(debug=True)

