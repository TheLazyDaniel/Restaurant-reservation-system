from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Daniel','age': 19}
    return render_template('example1.html', title = 'Home', user = user)

@app.route('/notitle')      
def CS():          
    user = {'username': 'Daniel','age': 19}
    return render_template('example2.html', user = user)

@app.route('/ME')      # /ME → Study Solidworks
def ME():          
    return "Study Solidwork!" 

@app.route('/EEE')
def EEE():
    return "Study circuits!"