from flask import Flask

app = Flask(__name__)



@app.route("/goodbye")
def good_bye():
    return "Good bye!"

@app.route("/hello")
def hello_world():
    return "Hello, World!"