from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from api.models.base import db
from api.models.person import Person

from api.forms.login import LoginForm, RegisterForm


login = Blueprint('login', __name__)


@login.route('/login', methods=['GET', 'POST'])
def login_route():
    form = LoginForm()
    if not form.validate_on_submit():
        return render_template('login.html', form=form)

    email = form.email.data
    password = form.password.data
    remember = True if form.remember.data else False

    person = Person.query.filter_by(email=email).first()

    if not person or not check_password_hash(person.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('login.login_route'))

    login_user(person, remember=remember)
    return redirect(url_for('login.profile'))


@login.route('/signup', methods=['POST', 'GET'])
def signup():
    form = RegisterForm()
    if not form.validate_on_submit():
        return render_template('register.html', form=form)

    email = form.email.data
    password = form.password.data
    name = form.name.data

    # check if the user is already registered
    person = Person.query.filter_by(email=email).first()
    if person:
        flash('Email address already exists')
        return redirect(url_for('login.signup'))

    # if not, register the user
    new_user = Person(email=email, name=name, password=generate_password_hash(password, method='sha256'))

    db.session.add(new_user)
    db.session.commit()
    flash('Thanks for registering! Please login')
    return redirect(url_for('login.login_route'))


@login.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('generic.index'))


@login.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

