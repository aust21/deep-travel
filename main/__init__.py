from flask import Flask, render_template, flash, request
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

import os

DB_NAME = "database.db"
db = SQLAlchemy()


def create_app():
    app = Flask(__name__, static_folder='static', template_folder='templates')
    app.config['SECRET_KEY'] = os.urandom(24)
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    # db.init_app(app)
    from .models import User
    from .views import views

    app.register_blueprint(views, url_prefix="/")

    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    @app.route("/")
    def index():
        return render_template("home/home.html")
    

    return app