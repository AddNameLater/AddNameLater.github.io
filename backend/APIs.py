import json
from flask import Flask, render_template, request
from flask_login import LoginManager
from pymongo import MongoClient

app = Flask(__name__)

loginf = LoginManager(app)

uri = "mongodb+srv://Editor:Code9@diet-tracker.ncrahr5.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)

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
        #For response body, call GET functions for user data inside json variable
        response_body = {
            "userName" : "test",
            "password" : "testPW",
            "height" : 68,
            "age" : 21,
            "gender" : "Female",
            "weight" : 155,
            "flag" : 3
        }
        return response_body
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

@app.route('/userinfo/<username>')
def userlogin(username):
    if request.method == "GET":
        db = client.DietTracker
        coll = db.Users
        result = coll.find_one({"name": username}, {"_id": 0})
        qresult = list(result.values())
        qres = ("User ID: " + str(qresult[0]) + "\nUser Name: " + str(qresult[1]) + "\nHeight(inches): " + str(qresult[3]) + "\nWeight(lbs): " + str(qresult[4]) + "\nExercise Class: " + str(qresult[5]))
        return qres
    elif request.method == "POST":
        return "test"   

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
