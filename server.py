from flask import Flask , render_template, request, redirect, session, flash
import random

app = Flask(__name__)
app.secret_key='159487263'

@app.route('/')
def index():
    if 'count' not in session:
        session['count'] = 0
    if 'result' not in session:
        result = 'hidden'
    else:
        result = session['result']
        session['result'] = 'hidden'
    if 'reset' not in session:
        reset = 'hidden'
    else:
        reset = session['reset']
        session['reset'] = 'hidden'
    if 'color' not in session:
        color = 'hidden'
    else:
        color = session['color']
        session['color'] = 'hidden'
    if 'message' not in session:
        session["message"]= ""
    if 'number' not in session:
        session['number']=random.randrange(1,101)
    number = session['number']
    return render_template("index.html", message=session['message'], color=color, reset=reset, result=result, number=number)

@app.route('/guess', methods=['POST'])
def guess():
    session['result'] = 'hidden'
    session['count'] += 1
    session['color'] = 'hidden'
    session['reset'] = 'hidden'
    guess = int(request.form['number'])
    if guess == session['number']:
        session['message']= 'You got it!'
        session['color']= 'hidden'
        session['result']= 'result'
        session['reset'] = 'resetButton'
        session['count'] = 0
        return redirect('/')
    if session['count'] >= 5:
        session['message']= 'Game Over!'
        session['color'] = 'destroy'
        session['color']= 'hidden'
        session['result']= 'result2'
        session['reset'] = 'resetButton'
        return redirect('/')
    if guess > session['number']:
        session['message']= 'Too High!'
        session['color'] = 'red'
    elif guess < session['number']:
        session['message']= 'Too Low!'
        session['color'] = 'blue' 
    return redirect('/')

@app.route('/reset')
def reset():
    session['count'] = 0
    session['number']
    session.pop("number")
    session.pop("message")
    session.pop('result')
    return redirect('/')
app.run(debug=True)