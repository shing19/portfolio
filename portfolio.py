from app import db, create_app
from app.models import Project, Collection, Album


app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Project': Project, 'Collection': Collection, 'Album': Album}