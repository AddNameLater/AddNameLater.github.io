import json
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def login():
    if request.method == "GET":
        return "This is the login page"
    elif request.method == "POST":
        return "test"

@app.route('/dashboard')
def dashboard():
    if request.method == "GET":
        return "This is the dashboard"
    elif request.method == "POST":
        return "test"

@app.route("/editprofile")
def editProfile():
    if request.method == "GET":
        return "This is the edit profile page"
    elif request.method == "POST":
        return "test"

@app.route("/tracker")
def tracker():
    if request.method == "GET":
        return "This is the tracker page"
    elif request.method == "POST":
        return "test"

@app.route("/tracker/search")
def search():
    if request.method == "GET":
        return "This is the search page"
    elif request.method == "POST":
        return "test"

@app.route("/notepad")
def notepad():
    if request.method == "GET":
        return "This is the notepade page"
    elif request.method == "POST":
        return "test"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
