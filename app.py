# app.py
from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to My Python App 🚀"

@app.route("/health")
def health():
    return jsonify({
        "status": "OK",
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

@app.route("/user/<name>")
def user(name):
    return jsonify({
        "message": f"Hello {name}",
        "app": "Simple Flask App"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
