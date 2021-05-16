from app.models import TestAttempt
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from . import db
from .models import TestAttempt, User


routes = Blueprint('routes', __name__)

@routes.route('/')
def home():
    return render_template('home.html', user=current_user)

@routes.route('/learn')
@login_required
def learn():
    user = User.query.filter_by(id = current_user.id).first()
    bestAttempt1 = user.best_attempt(1)
    bestAttempt2 = user.best_attempt(2)
    bestAttempt3 = user.best_attempt(3)
    return render_template('learn.html', user=current_user, bestAttempt1=bestAttempt1, bestAttempt2=bestAttempt2, bestAttempt3=bestAttempt3)

@routes.route('/stats')
def stats():
    return render_template('stats.html', user=current_user)

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

@routes.route('/learn/test-1', methods=['GET', 'POST'])
@login_required
def test1():
    if request.method == 'POST':

        correct_answers = ["B", "A", "B", "B", "4"]
        score = 0;

        for i in range(len(correct_answers)):
            if request.form.get('question'+str(i+1)) == correct_answers[i]:
              score += 1
            
        score = int(score / len(correct_answers) * 100)
        new_test_attempt = TestAttempt(testId=1, score=score, user_id=current_user.id)
        db.session.add(new_test_attempt)
        db.session.commit()
        flash(score)

        return redirect(url_for('routes.learn'))
    
    return render_template('test-1.html', user=current_user)

@routes.route('/learn/test-2', methods=['GET', 'POST'])
@login_required
def test2():
    if request.method == 'POST':

        correct_answers = ["A", "A", "B", "A", "A"]
        score = 0;

        for i in range(len(correct_answers)):
            if request.form.get('question'+str(i+1)) == correct_answers[i]:
              score += 1
            
        score = int(score / len(correct_answers) * 100)
        new_test_attempt = TestAttempt(testId=2, score=score, user_id=current_user.id)
        db.session.add(new_test_attempt)
        db.session.commit()
        flash(score)

        return redirect(url_for('routes.learn'))
    return render_template('test-2.html', user=current_user)

@routes.route('/learn/test-3', methods=['GET', 'POST'])
@login_required
def test3():
    if request.method == 'POST':

        correct_answers = ['2', "A", "A", '20', '20']
        score = 0;

        for i in range(len(correct_answers)):
            if request.form.get('question'+str(i+1)) == correct_answers[i]:
              score += 1
        
        score = int(score / len(correct_answers) * 100)
        new_test_attempt = TestAttempt(testId=3, score=score, user_id=current_user.id)
        db.session.add(new_test_attempt)
        db.session.commit()
        flash(score)

        return redirect(url_for('routes.learn'))
    return render_template('test-3.html', user=current_user)
