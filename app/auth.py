from flask import Blueprint, Flask, render_template, request, redirect, url_for

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

@auth.route('/logout')
def logout():
    return "<p>Log Out<p>"

@auth.route('/sign-up')
def sign_up():
    return "<p>Sign-Up<p>"