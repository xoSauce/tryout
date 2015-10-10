import os
from flask import Flask, request, redirect, url_for
from flask import make_response
from flask import render_template
app = Flask(__name__)
app.secret_key = 'F12Zr47j\3yX R~X@H!jmM]Lwf/,?KT'

def generateSessionKey():
	import string
	import random
	return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for i in range(12))

@app.route('/set', methods=['GET','POST'])
def setSession():
	response = redirect('/')
	response.set_cookie('myapp_user', generateSessionKey())
	return response	

@app.route('/')
def index():
	user_id = request.cookies.get('myapp_user')
	if user_id:	
		return "Welcome - Already set" + user_id
	else:
		return redirect('/set')

@app.route('/play')
def hey():
    return render_template('get_data.html')

if __name__ == '__main__':
    app.run(threaded=True, debug=True)
