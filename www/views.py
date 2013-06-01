from flask import render_template, url_for, redirect
from forms import CommentForm
from www import app, db
from models import Comment
import datetime

@app.errorhandler(404)
def error_404(e):
    return render_template('404.html'), 404

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

@app.route('/memes/')
def memes():
    return redirect(url_for('imeme'))

@app.route('/scale/')
def scale():
    return render_template('scale.html')

@app.route('/phrases/')
def phrases():
    return render_template('phrases.html')
