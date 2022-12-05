import json
from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager
from werkzeug.security import generate_password_hash, check_password_hash
from pymongo import MongoClient

app = Flask(__name__)

loginu = LoginManager(app)

uri = "mongodb+srv://Editor:Code9@diet-tracker.ncrahr5.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)
db = client.DietTracker

@app.route('/', methods=['POST'])
def login():
    if request.method == "POST":
        response_body = request.form
        print(response_body)
        print(request.form.get("password"))
        return response_body

@app.route('/createaccount', methods=['POST'])
def createAccount():
    if request.method == "POST":
        response_body = request.form
        print(response_body)
        print(request.form.get("password"))
        return response_body

@app.route('/dashboard')
def dashboard():
    if request.method == "GET":
        return "This is the dashboard"
    elif request.method == "POST":
        return "test"

@app.route("/editprofile", methods=['GET', 'POST'])
def editProfile():
    if request.method == "GET":
        #For response body, call GET functions for user data inside json variable
        coll = db.Users
        result = coll.find_one({"name": "User2"})
        qresult = list(result.values())
        response_body = {
            "userName" : str(qresult[1]),
            "password" : str(qresult[3]),
            "height" : int(qresult[4]),
            "age" : int(qresult[9]),
            "gender" : str(qresult[8]),
            "weight" : int(qresult[5]),
            "flag" : int(qresult[7])
        }
        return response_body
    elif request.method == "POST":
        #To get specific variable from json file, call request.form.get(<variable name>)
        response_body = request.form
        print(response_body)
        print(request.form.get("password"))
        return response_body

@app.route("/tracker", methods=['GET', 'POST'])
def tracker():
    if request.method == "GET":
        response_body = {
            "calories" : 1200,
            "carbohydrates" : 69,
            "fat" : 21,
            "protein" : 44,
            "totalCals": 2200,
            "totalCarbs": 275,
            "totalFat": 61,
            "totalProtein": 82
        }
        return response_body
    elif request.method == "POST":
        response_body = request.form
        print(response_body)
        print(request.form.get("protein"))
        return response_body

@app.route("/tracker/search", methods=['GET', 'POST'])
def search():
    if request.method == "GET":
        return "This is the search page"
    elif request.method == "POST":
        return "test"

@app.route("/notepad", methods=['GET', 'POST'])
def notepad():
    if request.method == "GET":
        return "This is the notepade page"
    elif request.method == "POST":
        return "test"

@app.route('/userinfo/<username>', methods=['GET', 'POST'])
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

@app.route('/signup', methods=['POST'])
def signup_post():
    coll = db.Users

    username = request.form.get('userName')
    password = request.form.get('password')

    #will return if user under given username already exists
    existCheck = coll.find_one({"name": username})
    if existCheck:
        return redirect(url_for('APIs.login')) #placeholder, ideally would redirect to blank signup form
    
    #add new user data to database
    passhash = generate_password_hash(password) #generates a hash which is what the database will store
    new_user = coll.insert_one({"name": username, "password": passhash}) #inserts new user into Users collection

    #redirect user to login page after successful registration
    return redirect(url_for('APIs.login'))

@app.route('/login', methods=['POST'])
def login_post():
    db = client.DietTracker
    coll = db.Users
    # login code
    username = request.form.get('userName')
    password = request.form.get('password')

    #check enterted details
    user = coll.find_one({"name": "User1"})
    if not user: #if username doesn't match db
        return redirect(url_for('APIs.login'))
    uservals = list(user.values())
    currentUserHash = uservals[2]
    if not check_password_hash(currentUserHash, password): #if pass is wrong
        return redirect(url_for('APIs.login'))

    #passing both checks means user is verified
    return 

    


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
