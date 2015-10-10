import os
from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return "hello world"

@app.route('/stuff')
def hey():
    myVar = 'xoSauce'
    return render_template('get_data.html', myVar=myVar)

if __name__ == '__main__':
    app.run(threaded=True)
