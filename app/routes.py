from app import app
from app.forms import ProjectForm, CollectionForm, AlbumForm
from flask import render_template, redirect


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/design')
def design():
    return render_template('design.html')

@app.route('/weblab')
def weblab():
    return render_template('weblab.html')

@app.route('/sketch')
def sketch():
    return render_template('sketch.html')

@app.route('/photography')
def photography():
    return render_template('photography.html')

@app.route('/adventure')
def adventure():
    return render_template('adventure.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/design/new', methods=['GET', 'POST'])
def project():
    form = ProjectForm()
    item = 'Project'
    if form.validate_on_submit():
        return redirect('/design')
    return render_template('new.html', form=form, item=item)

@app.route('/sketch/new', methods=['GET', 'POST'])
def collection():
    form = CollectionForm()
    item = 'Collection'
    if form.validate_on_submit():
        return redirect('/sketch')
    return render_template('new.html', form=form, item=item)

@app.route('/photography/new', methods=['GET', 'POST'])
def album():
    form = AlbumForm()
    item = 'Album'
    if form.validate_on_submit():
        return redirect('/photography')
    return render_template('new.html', form=form, item=item)