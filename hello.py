import os
from flask import Flask
from flask import render_template
app = Flask(__name__)
app.secret_key = 'F12Zr47j\3yX R~X@H!jmM]Lwf/,?KT'

def sumSessionCounter():
	try:
		session['counter'] += 1
	except KeyError:
		session['counter'] = 1

def generateSessionKey():
	import string
	import random
	return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(N))

@app.route('/')
def hello():
	sumSessionCounter()
    return generateSessionKey()

@app.route('/stuff')
def hey():
    myVar = 'xoSauce'
    return render_template('get_data.html', myVar=myVar)

if __name__ == '__main__':
    app.run(threaded=True)
