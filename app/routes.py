from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Daniel'}
    return '''
<html>
    <head>
        <title>Hello page-Small Restaurant Rev.</title>
    </head>
    <body>
        <h1>Hello, ''' + user['username'] + '''</h1>
    </body
</html>
'''

@app.route('/CS')      # /CS → Study Flask
def CS():          
    return "study flask!"  

@app.route('/ME')      # /ME → Study Solidworks
def ME():          
    return "Study Solidwork!" 

@app.route('/EEE')
def EEE():
    return "Study circuits!"