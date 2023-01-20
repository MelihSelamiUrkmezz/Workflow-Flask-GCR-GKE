from flask import Flask

app = Flask(__name__)



@app.route("/goodbye")
def good_bye():
    return "Good bye bro!"

@app.route("/hello")
def hello_world():
    return "Hello, World Bro! How're you?"