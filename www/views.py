from flask import render_template, url_for, redirect
from forms import CommentForm
from www import app, db
from models import Comment
import datetime

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resume/')
def resume():
    return render_template('resume.html')
