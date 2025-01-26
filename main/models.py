from flask_login import UserMixin
from datetime import date

from . import db

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)
    speciality = db.Column(db.String(100), nullable=False)
    company = db.Column(db.String(100), nullable=False)
    date_created = db.Column(db.Date, default=date.today)
    is_admin = db.Column(db.Boolean, default=False)
    profile_image = db.Column(db.String(100), default='default.png') 
    cormfirm_code = db.Column(db.String(7), default="0000000")
    account_confirmed = db.Column(db.Boolean, default=False)

class HomePageProductsData(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    image_path = db.Column(db.String(100), default='default.png')
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(1000000000), nullable=False)

class ShopProducts(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    image_path = db.Column(db.String(100))
    title = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(1000000000), nullable=False)
    price = db.Column(db.String(1000000), nullable=True)