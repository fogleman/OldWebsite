from flask import render_template, url_for, redirect
from forms import CommentForm
from www import app, db
from models import Comment
import datetime

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/projects/')
def projects():
    return render_template('projects.html')

@app.route('/resume/')
def resume():
    return render_template('resume.html')

@app.route('/imeme/')
def imeme():
    return render_template('imeme.html')

@app.route('/scale/')
def scale():
    return render_template('scale.html')
