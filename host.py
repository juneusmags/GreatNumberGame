from flask import Flask, render_template, redirect, request
from flask.globals import session
import random
app = Flask(__name__)
app.secret_key = '123456'

@app.route('/')
def guess():
    if 'number' not in session:
        session['number']=random.randint(1,100)
    if 'resultguess' not in session:
        session['resultguess']=' '
    if 'color' not in session:
        session['color']= ''
    print(session['number'])
    return render_template('index.html',number=session['number'], resultguess=session['resultguess'], color = session['color'])

@app.route('/guess', methods =['POST'])
def guessres():
    guess_from_form = request.form['randomnumber']
    if int(guess_from_form) > session['number']:
        session['resultguess'] = 'Too High'
        session['color']='red'
    if int(guess_from_form) < session['number']:
        session['resultguess'] = 'Too Low'
        session['color']='red'
    if int(guess_from_form) == session['number']:
        session['resultguess'] = 'You Win'
        session['color']='green'
        session['number'] = random.randint(1,100)
    return redirect('/')





if __name__ == "__main__":
    app.run(debug=True)