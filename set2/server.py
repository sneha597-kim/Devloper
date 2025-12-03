from flask import Flask, send_from_directory
app = Flask(__name__)

@app.route("/")
def register():
    return send_from_directory(".", "RegistrationForm_597.html")

@app.route("/login")
def login():
    return send_from_directory(".", "login.html")

app.run(host="0.0.0.0", port=5000)
