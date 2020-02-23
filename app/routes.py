from app import app
from app.forms import ProjectForm
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/design')
def design():
    return render_template('design.html')

@app.route('/design/new')
def project():
    form = ProjectForm()
    return render_template('new_project.html', form=form)