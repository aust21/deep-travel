from flask import Flask, Blueprint, render_template

views = Blueprint("views", __name__)

@views.route("/")
def home():
    return render_template("home/home.html")

@views.route("/book", methods=["GET", "POST"])
def book_seat():
    return render_template("home/book.html")

@views.route("/homestead")
def homestead():
    return render_template("resources/homestead.html")

@views.route("/tetraton")
def tetraton():
    return "hi"

@views.route("/spaceship")
def spaceship():
    return "yhup"