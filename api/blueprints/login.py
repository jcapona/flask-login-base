from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from api.models.base import db
from api.models.person import Person


login = Blueprint('login', __name__)

@login.route('/login', methods=['GET'])
def login_get():
    return render_template('login.html')


@login.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    person = Person.query.filter_by(email=email).first()

    if not person or not check_password_hash(person.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('login.login_post'))

    login_user(person, remember=remember)
    return redirect(url_for('login.profile'))


@login.route('/register')
def register():
    return render_template('register.html')


@login.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('generic.index'))


@login.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    # check if the user is already registered
    person = Person.query.filter_by(email=email).first()
    if person:
        flash('Email address already exists')
        return redirect(url_for('login.register'))

    # if not, register the user
    new_user = Person(email=email, name=name, password=generate_password_hash(password, method='sha256'))

    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('login.log_in'))


@login.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

