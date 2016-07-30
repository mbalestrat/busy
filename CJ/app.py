from flask import Flask, render_template, request, redirect, url_for
from group_code import *
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/check_username/', methods=['POST'])
def check_username():
	username = request.form['username']
	if username != 'bob':
		return render_template('home.html', username_free=True, username=username)
	else:
		return render_template('home.html', username_free=False, username=username)

@app.route('/compare/')
def compare():
	code = generate_code()
	return render_template('compare.html', group_code=code)

if __name__ == '__main__':
	app.run(debug=True)