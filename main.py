import flask
import random
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/pages/author/<author>/<id>")
def page(author, id):
    context = {}
    context["name"] = id
    context["author"] = author
    context["text"] = """some_unusual_page_text"""
    return render_template("page.html", context = context)
@app.route("/")
def index():
    context = {}
    memes = ["Страница1", "Hallo"]
    random.shuffle(memes)
    a = open("answer.txt","r")
    ans = a.readlines()
    a.close()
    a = open("answer1.txt","r")
    ans1 = a.readlines()
    a.close()
    a = open("answer2.txt","r")
    ans2 = a.readlines()
    a.close()
    context["mem"] = memes[0]
    return render_template("index.html", text = ans, text1= ans1, text2 = ans2, context = context)


app.run(debug=True,port = 5001, host = "0.0.0.0")
