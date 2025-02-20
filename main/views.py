import os
import random

from flask import Flask, Blueprint, render_template, request, redirect, url_for, current_app
from flask_login import current_user
from flask_mail import Message

from main import mail

views = Blueprint("views", __name__)

def send_mail(name, email, destination, seat_number, flight_code):
    msg = Message('Deep Travel | Travel Ticket',
                  sender=current_app.config['MAIL_USERNAME'],
                  recipients=[email])

    msg.html = render_template('email/ticket.html',
                               name=name,
                               destination=destination,
                               seat_number=seat_number,
                               flight_code=flight_code
                               )

    mail.send(msg)

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
        seat_number = random.randint(1, 100)
        flight_code = "#" + str(random.randint(1213, 3323))

        # Validate form fields
        if all([name, email, destination, departure]):
            send_mail(name, email, destination, seat_number, flight_code)
            return redirect(url_for("views.thanks"))
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