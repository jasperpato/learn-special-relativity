from flask import Blueprint, render_template, request, redirect, url_for, flash

MIN_USERNAME_LENGTH = 4
MIN_PASSWORD_LENGTH = 7

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    user = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = "Incorrect name or password"
            user = "admin"
        else:
            return redirect(url_for('routes.learn'))

    return render_template('login.html', error = error)

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        passwordConfirm = request.form.get('passwordConfirm')

        if len(username) < MIN_USERNAME_LENGTH:
            flash("Username must be at least 4 characters", category='error')
        elif len(password) < MIN_PASSWORD_LENGTH:
            flash("Passwor must be at least 7 characters", category='error')
        elif password != passwordConfirm:
            flash("Passwords do not match", category='error')
        else:
            flash("Account created!", category='success')


    return render_template('sign-up.html')