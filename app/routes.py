from flask import Blueprint, Flask, render_template, request, redirect, url_for

routes = Blueprint('routes', __name__)

@routes.route('/')
def home():
    return render_template('home.html')

@routes.route('/learn')
def learn():
    return render_template('learn.html')

@routes.route('/learn/lesson-1')
def lesson1():
    return render_template('lesson-1.html')

@routes.route('/learn/lesson-2')
def lesson2():
    return render_template('lesson-2.html')

@routes.route('/learn/lesson-3')
def lesson3():
    return render_template('lesson-3.html')

@routes.route('/learn/test-1')
def test1():
    return render_template('test-1.html')

@routes.route('/learn/test-2')
def test2():
    return render_template('test-2.html')

@routes.route('/learn/test-3')
def test3():
    return render_template('test-3.html')
