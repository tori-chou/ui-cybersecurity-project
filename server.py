from flask import Flask, render_template, request, jsonify, redirect, url_for, session
from data import lessons, quiz_questions
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def home():
    session['answers'] = {}
    session['lesson_views'] = {}
    return render_template('home.html')

@app.route('/learn/<int:lesson_id>')
def learn(lesson_id):
    if 1 <= lesson_id <= len(lessons):
        now = datetime.now()
        views = session.get('lesson_views', {})
        durations = session.get('lesson_durations', {})

        previous_id = str(lesson_id - 1)
        if previous_id in views:
            start_time = datetime.fromisoformat(views[previous_id])
            durations[previous_id] = (now - start_time).total_seconds()
        views[str(lesson_id)] = now.isoformat()
        session['lesson_views'] = views
        session['lesson_durations'] = durations
        print("Views:", session['lesson_views'])
        print("Durations:", session['lesson_durations'])
        
        lesson = lessons[lesson_id - 1]
        return render_template('learn.html', lesson=lesson, next_id=lesson_id + 1, total_lessons=len(lessons))
    else:
        return redirect(url_for('quiz', question_id=1))

@app.route('/quiz/<int:question_id>', methods=['GET', 'POST'])
def quiz(question_id):
    if 'answers' not in session:
        session['answers'] = {}

    answer = None

    if request.method == 'POST':
        answer = request.form.get('answer')
        answers = session.get('answers', {})
        answers[str(question_id)] = answer
        session['answers'] = answers  # <-- triggers session update

    if 1 <= question_id <= len(quiz_questions):
        question = quiz_questions[question_id - 1]
        if not answer:
            answer = session.get('answers', {}).get(str(question_id))
        return render_template('quiz.html', question=question, next_id=question_id + 1, total_questions=len(quiz_questions), answer=answer)
    else:
        return redirect(url_for('results'))


@app.route('/results')
def results():
    answers = session.get('answers', {})
    score = 0
    for idx, q in enumerate(quiz_questions):
        if answers.get(str(idx + 1)) == q['answer']:
            score += 1
    return render_template(
        'results.html',
        score=score,
        total=len(quiz_questions),
        answers=answers,
        questions=quiz_questions
    )

@app.route('/review')
def review():
    answers = session.get('answers', {})
    incorrect = []
    for idx, q in enumerate(quiz_questions):
        q_num = str(idx + 1)
        if answers.get(q_num) != q['answer']:
            incorrect.append({
                'question_number': q_num,
                'question': q['question'],
                'your_answer': answers.get(q_num),
                'correct_answer': q['answer'],
                'explanation': q.get('explanation', ''),
                "image": q.get("image", None)
            })
    return render_template('review.html', incorrect_questions=incorrect)

@app.route('/log_timeout', methods=['POST'])
def log_timeout():
    data = request.get_json()
    question_id = data.get('question_id')

    if 'timeouts' not in session:
        session['timeouts'] = []

    if question_id not in session['timeouts']:
        session['timeouts'].append(question_id)
        session.modified = True

    print(f"⚠️ Timeout logged for Q{question_id}")
    return jsonify({'status': 'ok'})
    
if __name__ == '__main__':
   app.run(debug = True, port=5001)