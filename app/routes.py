from flask import render_template, request, url_for, flash, redirect
from app import app

@app.route('/')
def index():
	return render_template('index.html')