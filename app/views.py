from app import app, db
from flask import render_template

@app.route('/')
def index():
	param = {
		'title': 'Flask Base',
		'message': 'Flask Base installed successfully, enjoy hacking.'
	}
	return render_template('index.html',
							param = param)
