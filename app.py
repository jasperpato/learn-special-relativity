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
    user = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = "Incorrect name or password"
            user = "admin"
        else:
            return redirect(url_for('learn'))

    return render_template('login.html', error = error)

@app.route('/learn/lesson-1')
def lesson1():
    return render_template('lesson-1.html')

@app.route('/learn/lesson-2')
def lesson2():
    return render_template('lesson-2.html')

@app.route('/learn/lesson-3')
def lesson3():
    return render_template('lesson-3.html')

@app.route('/learn/test-1')
def test1():
    return render_template('test-1.html')

@app.route('/learn/test-2')
def test2():
    return render_template('test-2.html')

@app.route('/learn/test-3')
def test3():
    return render_template('test-3.html')

if __name__ == '__main__':
    app.run(debug=True)
