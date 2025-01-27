from flask import Flask, Blueprint, render_template

views = Blueprint("views", __name__)

@views.route("/")
def home():
    return render_template("home/home.html")