from flask import render_template
from program import app
from datetime import date

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Big Pork Daddy', time=date.today()) #timenow)

@app.route('/pork_papa')
def pork_papa():
    return render_template('pork_papa.html')
