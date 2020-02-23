from app import app, db
from app.models import Project, Collection, Album


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Project': Project, 'Collection': Collection, 'Album': Album}