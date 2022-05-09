from app.models import TestAttempt
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from . import db
from .models import TestAttempt, TestQuestion, User, Test
from .populate_tests import populate

routes = Blueprint('routes', __name__)

def get_theme(): return current_user.selected_theme() if current_user.is_authenticated else "Blue"

@routes.route('/populate-tables')
def populate_tables():
    try: populate()
    except: return 'not ok'
    return 'ok'

@routes.route('/')
def home(): return render_template('home.html', user=current_user, theme=get_theme())

@routes.route('/learn')
@login_required
def learn():
    return render_template(
        'learn.html',
        user = current_user,
        theme = get_theme(),
        attempts = [current_user.best_attempt(i+1) for i in range(3)],
        str=str
    )

def number_sorted(l): return sorted(l, key=lambda x: x.number)

@routes.route('/stats', methods=['GET', 'POST'])
def stats():
    if request.method == 'POST':
        if current_user.is_authenticated:
            current_user.set_theme(request.form.get("colour"))
            db.session.commit()
        else: return redirect(url_for('auth.login'))

    test_number = request.args.get('test_number')
    if not test_number or not test_number.isdigit(): test_number = 1
    test_number = int(test_number)
    if test_number not in (1,2,3): test_number = 1

    first_score = current_user.first_attempt(test_number) if current_user.is_authenticated else 0
    top_score = current_user.best_attempt(test_number) if current_user.is_authenticated else 0

    first_scores = [r.score for r in TestAttempt.query.filter_by(test_number=test_number, attempt_number=1).all()]
    avg_first_score = int(sum(first_scores) / len(first_scores)) if len(first_scores) else 0

    scores = (top_score, first_score, avg_first_score)
    unlocked = [current_user.best_attempt(i) == 100 for i in range(1,4)] if current_user.is_authenticated else []

    return render_template(
        'stats.html',
        user = current_user,
        theme = get_theme(),
        test_number = test_number,
        scores = scores,
        unlocked = unlocked,
        unlocked_all = all(unlocked)
    )

@routes.route('/learn/lesson1')
@login_required
def lesson1():
    return render_template('lesson1.html', user=current_user, theme=get_theme())

@routes.route('/learn/lesson2')
@login_required
def lesson2():
    return render_template('lesson2.html', user=current_user, theme=get_theme())

@routes.route('/learn/lesson3')
@login_required
def lesson3():
    return render_template('lesson3.html', user=current_user, theme=get_theme())

@routes.route('/learn/test')
@login_required
def test():
    test_number = request.args.get('test_number')
    if not test_number or not test_number.isdigit(): test_number = 1
    test_number = int(test_number)
    if test_number not in (1,2,3): test_number = 1
    
    questions = Test.query.filter_by(number=test_number).first().questions

    return render_template(
        'test.html',
        user=current_user,
        theme=get_theme(),
        test_number=test_number,
        questions=questions,
        len=len,
        enumerate=enumerate,
        zip=zip,
        number_sorted = number_sorted
    )

@routes.route('/learn/results', methods=['POST'])
@login_required
def results():
    test_number = int(request.form.get('test_number'))
    questions = Test.query.filter_by(number=test_number).first().questions

    correct = []
    score = 0
    for q in questions:
        got = request.form.get(str(q.number)) == q.get_correct()
        correct.append(got)
        if got: score += 1
    score = int(score / len(questions) * 100)   

    attempt_number = db.session.query(db.func.max(TestAttempt.attempt_number)).filter_by(test_number=test_number, user_id=current_user.id).scalar()
    attempt_number = attempt_number+1 if attempt_number else 1

    db.session.add(TestAttempt(
        test_number = test_number,
        score = score,
        attempt_number = attempt_number,
        user_id = current_user.id
    ))
    db.session.commit()
    flash(score)

    return render_template(
        'results.html',
        user=current_user,
        theme=get_theme(), 
        test_number=test_number,
        questions=questions,
        correct=correct,
        enumerate=enumerate,
    )