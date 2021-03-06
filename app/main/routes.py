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
    projects = Project.query.order_by(Project.timestamp.desc())
    return render_template('design.html', projects=projects)

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

@bp.route('/portfolio')
def portfolio():
    files = []
    for i in range(53):
        file = '/portfolio/' + str(i) + ".png"
        files.append(file)
    return render_template('portfolio.html', files=files)

@bp.route('/design/new', methods=['GET', 'POST'])
def project():
    form = ProjectForm()
    item = 'Project'
    if form.validate_on_submit():
        project = Project(topic=form.topic.data, name=form.name.data, timestamp=form.timestamp.data, timespan=form.timespan.data, description=form.description.data)
        db.session.add(project)
        db.session.commit()
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

@bp.route('/test', methods=['GET', 'POST'])
def test():
    return render_template('test.html')