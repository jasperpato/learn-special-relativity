from flask import Flask, render_template, request, redirect, url_for
# from app import app, routes
# from app.forms import LoginForm

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/learn')
def learn():
    return render_template('learn.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'max' or request.form['password'] != 'password':
            error = "You are not allowed here"
        else:
            return redirect(url_for('learn'))

    return render_template('login.html', error = error)



if __name__ == '__main__':
    app.run(debug=True)