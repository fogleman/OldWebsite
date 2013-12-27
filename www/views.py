from flask import render_template, url_for, redirect
from www import app

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

@app.route('/craft/')
def craft():
    return render_template('craft.html')

@app.route('/star-rocket/')
def star_rocket():
    return render_template('star-rocket.html')

@app.route('/dcpu/')
def dcpu():
    return render_template('dcpu.html')

@app.route('/ricochet/')
def ricochet():
    return render_template('ricochet.html')

@app.route('/sync/')
def sync():
    return render_template('sync.html')
