from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/CS')      # /CS → Study Flask
def CS():          
    return "study flask!"  

@app.route('/ME')      # /ME → Study Solidworks
def ME():          
    return "Study Solidwork!" 

@app.route('/EEE')
def EEE():
    return "Study circuits!"