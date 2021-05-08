from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

MIN_USERNAME_LENGTH = 4
MIN_PASSWORD_LENGTH = 7

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password_hash, password):
                flash("Logged in successfully!", category="success")
                login_user(user, remember=True)
                return redirect(url_for('routes.home'))
            else:
                flash("Incorrect password, try again.", category="error")
        else:
            flash("User does not exist", category="error")

    return render_template('login.html', user=current_user)

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        passwordConfirm = request.form.get('passwordConfirm')

        user = User.query.filter_by(username=username).first()

        if user:
            flash("Username already exists", category="error")
        elif len(username) < MIN_USERNAME_LENGTH:
            flash("Username must be at least 4 characters", category='error')
        elif len(password) < MIN_PASSWORD_LENGTH:
            flash("Passwor must be at least 7 characters", category='error')
        elif password != passwordConfirm:
            flash("Passwords do not match", category='error')
        else:
            new_user = User(username=username, password_hash=generate_password_hash(password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()

            login_user(new_user, remember=True)

            flash("Account created!", category='success')
            return redirect(url_for('routes.home'))

    return render_template('sign-up.html', user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('routes.home'))
