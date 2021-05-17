from app.models import TestAttempt
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from . import db
from .models import TestAttempt, User


routes = Blueprint('routes', __name__)

@routes.route('/')
def home():
    if current_user.is_authenticated:
        user = User.query.filter_by(id = current_user.id).first()
        theme = user.selected_theme()
    else:
        theme = "Blue"

    return render_template('home.html', user=current_user, theme=theme)

@routes.route('/learn')
@login_required
def learn():
    user = User.query.filter_by(id = current_user.id).first()
    bestAttempt1 = user.best_attempt(1)
    bestAttempt2 = user.best_attempt(2)
    bestAttempt3 = user.best_attempt(3)
    theme = user.selected_theme()

    return render_template('learn.html', user=current_user, bestAttempt1=bestAttempt1, bestAttempt2=bestAttempt2, bestAttempt3=bestAttempt3, theme=theme)

@routes.route('/stats', methods=['GET', 'POST'])
def stats():
    if current_user.is_authenticated:
        user = User.query.filter_by(id = current_user.id).first()
        theme = user.selected_theme()
    else:
        theme = "Blue"

    testData = {}
    tests = TestAttempt.query.all()
    top = [0,0,0]
    sum = [0,0,0]
    total = [0,0,0]
    for t in tests:
        id = t.testId - 1
        if t.score > top[id]:
            top[id] = t.score
        sum[id] += t.score
        total[id] += 1
    for i in range(3):
        if total[i] > 0:
            testData['topScore' + str(i+1)] = str(top[i])
            testData['avScore' + str(i+1)] = str(int(float(sum[i])/total[i]))
        else:
            testData['topScore' + str(i+1)] = '0'
            testData['avScore' + str(i+1)] = '0'
    testData['bestAttempt1'] = '0'
    testData['bestAttempt2'] = '0'
    testData['bestAttempt3'] = '0'

    if current_user.is_authenticated:
        testData['bestAttempt1'] = str(user.best_attempt(1))
        testData['bestAttempt2'] = str(user.best_attempt(2))
        testData['bestAttempt3'] = str(user.best_attempt(3))
    
    if request.method == 'POST':
        if current_user.is_authenticated:
            user.set_theme(request.form.get("colour"))
            theme = user.selected_theme()
            db.session.commit()
        else:
            return redirect(url_for('auth.login'))

    return render_template('stats.html', user=current_user, testData = testData, theme=theme )

@routes.route('/learn/lesson-1')
@login_required
def lesson1():
    user = User.query.filter_by(id = current_user.id).first()
    theme = user.selected_theme()
    return render_template('lesson-1.html', user=current_user, theme=theme)

@routes.route('/learn/lesson-2')
@login_required
def lesson2():
    user = User.query.filter_by(id = current_user.id).first()
    theme = user.selected_theme()
    return render_template('lesson-2.html', user=current_user, theme=theme)

@routes.route('/learn/lesson-3')
@login_required
def lesson3():
    user = User.query.filter_by(id = current_user.id).first()
    theme = user.selected_theme()
    return render_template('lesson-3.html', user=current_user, theme=theme)

@routes.route('/learn/test-1')
@login_required
def test1():
    user = User.query.filter_by(id = current_user.id).first()
    theme = user.selected_theme()
    
    return render_template('test-1.html', user=current_user, theme=theme)

@routes.route('/learn/results-1', methods=['POST'])
@login_required
def results1():
    user = User.query.filter_by(id = current_user.id).first()
    theme = user.selected_theme()
    correct_answers = {1:"B", 2:"A", 3:"B", 4:"B", 5:"4"}
    score = 0
    answers = {}

    for i in range(1,6):
        a = request.form.get( 'question' + str(i) )
        answers[ str(i) ] = a
        if a == correct_answers[i]:
            score += 1
            
    score = int(score / len(correct_answers) * 100)
    new_test_attempt = TestAttempt(testId=1, score=score, user_id=current_user.id)
    db.session.add(new_test_attempt)
    db.session.commit()
    flash(score)

    return render_template('results-1.html', user=current_user, theme=theme, answers=answers, correct=correct_answers)

@routes.route('/learn/test-2')
@login_required
def test2():
    user = User.query.filter_by(id = current_user.id).first()
    theme = user.selected_theme()
    return render_template('test-2.html', user=current_user, theme=theme)

@routes.route('/learn/results-2', methods=['POST'])
@login_required
def results2():
    user = User.query.filter_by(id = current_user.id).first()
    theme = user.selected_theme()
    correct_answers = {1:"A", 2:"A", 3:"B", 4:"A", 5:"A"}
    score = 0
    answers = {}

    for i in range(1,6):
        a = request.form.get( 'question' + str(i) )
        answers[ str(i) ] = a
        if a == correct_answers[i]:
            score += 1
            
    score = int(score / len(correct_answers) * 100)
    new_test_attempt = TestAttempt(testId=2, score=score, user_id=current_user.id)
    db.session.add(new_test_attempt)
    db.session.commit()
    flash(score)

    return render_template('results-2.html', user=current_user, theme=theme, answers=answers, correct=correct_answers)

@routes.route('/learn/test-3', methods=['GET', 'POST'])
@login_required
def test3():
    user = User.query.filter_by(id = current_user.id).first()
    theme = user.selected_theme()
    return render_template('test-3.html', user=current_user, theme=theme)

@routes.route('/learn/results-3', methods=['POST'])
@login_required
def results3():
    user = User.query.filter_by(id = current_user.id).first()
    theme = user.selected_theme()
    correct_answers = {1:"2", 2:"A", 3:"A", 4:"20", 5:"20"}
    score = 0;
    answers = {}

    for i in range(1,6):
        a = request.form.get( 'question' + str(i) )
        answers[ str(i) ] = a
        if a == correct_answers[i]:
            score += 1
            
    score = int(score / len(correct_answers) * 100)
    new_test_attempt = TestAttempt(testId=3, score=score, user_id=current_user.id)
    db.session.add(new_test_attempt)
    db.session.commit()
    flash(score)

    return render_template('results-3.html', user=current_user, theme=theme, answers=answers, correct=correct_answers)