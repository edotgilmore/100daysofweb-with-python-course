from flask import render_template
from program import app
from datetime import date

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Template Demo', time=date.today()) #timenow)

@app.route('/100Days')
def p100days():
    return render_template('pork_papa.html')
