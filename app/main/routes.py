from flask import render_template, redirect
from app import db
from app.main.forms import ProjectForm, CollectionForm, AlbumForm
from app.models import Project, Collection, Album
from app.main import bp


@bp.route('/')
@bp.route('/index')
def index():
    return render_template('index.html')

@bp.route('/design')
def design():
    return render_template('design.html')

@bp.route('/weblab')
def weblab():
    return render_template('weblab.html')

@bp.route('/sketch')
def sketch():
    return render_template('sketch.html')

@bp.route('/photography')
def photography():
    return render_template('photography.html')

@bp.route('/adventure')
def adventure():
    return render_template('adventure.html')

@bp.route('/about')
def about():
    return render_template('about.html')

@bp.route('/design/new', methods=['GET', 'POST'])
def project():
    form = ProjectForm()
    item = 'Project'
    if form.validate_on_submit():
        return redirect('/design')
    return render_template('new.html', form=form, item=item)

@bp.route('/sketch/new', methods=['GET', 'POST'])
def collection():
    form = CollectionForm()
    item = 'Collection'
    if form.validate_on_submit():
        return redirect('/sketch')
    return render_template('new.html', form=form, item=item)

@bp.route('/photography/new', methods=['GET', 'POST'])
def album():
    form = AlbumForm()
    item = 'Album'
    if form.validate_on_submit():
        return redirect('/photography')
    return render_template('new.html', form=form, item=item)