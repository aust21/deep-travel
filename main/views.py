from flask import Flask, Blueprint, render_template, request, redirect, url_for

views = Blueprint("views", __name__)

@views.route("/")
def home():
    return render_template("home/home.html")

@views.route("/book", methods=["GET", "POST"])
def book_seat():
    if request.method == "POST":
        # Get form data
        name = request.form.get("name")
        email = request.form.get("email")
        destination = request.form.get("destination")
        departure = request.form.get("departure")

        # Validate form fields
        if all([name, email, destination, departure]):
            return redirect(url_for("views.thanks"))
        else:
            return redirect(url_for("views.error"))
    
    return render_template("home/book.html")


@views.route("/homestead")
def homestead():
    return render_template("resources/homestead.html")

@views.route("/teratron")
def tetraton():
    return render_template("resources/teratron.html")

@views.route("/spaceship")
def spaceship():
    return render_template("resources/ship.html")

@views.route("/thank-you")
def thanks():
    return render_template("resources/thanks.html")

@views.route("/error")
def error():
    return render_template("resources/error.html")