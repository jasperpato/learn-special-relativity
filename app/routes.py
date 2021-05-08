from flask import Blueprint, render_template
from flask_login import login_required, current_user


routes = Blueprint('routes', __name__)

@routes.route('/')
def home():
    return render_template('home.html', user=current_user)

@routes.route('/learn')
@login_required
def learn():
    return render_template('learn.html', user=current_user)

@routes.route('/learn/lesson-1')
@login_required
def lesson1():
    return render_template('lesson-1.html', user=current_user)

@routes.route('/learn/lesson-2')
@login_required
def lesson2():
    return render_template('lesson-2.html', user=current_user)

@routes.route('/learn/lesson-3')
@login_required
def lesson3():
    return render_template('lesson-3.html', user=current_user)

@routes.route('/learn/test-1')
@login_required
def test1():
    return render_template('test-1.html', user=current_user)

@routes.route('/learn/test-2')
@login_required
def test2():
    return render_template('test-2.html', user=current_user)

@routes.route('/learn/test-3')
@login_required
def test3():
    return render_template('test-3.html', user=current_user)
