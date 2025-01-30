from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from dotenv import load_dotenv

load_dotenv("../.env")

import os
mail = Mail()

DB_NAME = "database.db"
db = SQLAlchemy()

def create_app():
    app = Flask(__name__, static_folder='static', template_folder='templates')
    app.config['SECRET_KEY'] = os.urandom(24)
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = 'aust21ncode@gmail.com'
    app.config['MAIL_PASSWORD'] = "pqph qshg lwvu dlvd"
    db.init_app(app)
    mail.init_app(app)
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

    

    return app