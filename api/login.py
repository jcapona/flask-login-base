from flask import Blueprint
from .models.base import db

login = Blueprint('login', __name__)

@login.route('/login')
def log_in():
    return 'login'

@login.route('/register')
def signup():
    return 'register'

@login.route('/logout')
def logout():
    return 'logout'

