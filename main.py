import flask
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    a = open("answer.txt","r")
    ans = a.readlines()
    a.close()
    a = open("answer1.txt","r")
    ans1 = a.readlines()
    a.close()
    a = open("answer2.txt","r")
    ans2 = a.readlines()
    a.close()
    return render_template("index.html", text = ans, text1= ans1, text2 = ans2)

app.run(debug=True,port = 5001, host = "0.0.0.0")