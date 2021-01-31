from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/scopes")
def scopes():
    return render_template("scopes.html")

@app.route("/servers")
def servers():
    return render_template("servers.html")

@app.route("/hotlines")
def hotlines():
    return render_template("hotlines.html")