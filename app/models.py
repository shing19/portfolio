from app import db


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    topic = db.Column(db.Text, unique=True)
    timestamp = db.Column(db.Date, index=True, unique=True)
    timespan = db.Column(db.Integer, index=True)
    description = db.Column(db.Text)
    url = db.Column(db.String)
    
    def __repr__(self):
        return 'Project {}'.format(self.topic)


class Collection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    topic = db.Column(db.Text, unique=True)
    timestamp = db.Column(db.Date, index=True, unique=True)
    description = db.Column(db.Text)
    url = db.Column(db.String)

    def __repr__(self):
        return 'Collection {}'.format(self.topic)


class Album(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    topic = db.Column(db.Text, unique=True)
    timestamp = db.Column(db.Date, index=True, unique=True)
    description = db.Column(db.Text)
    url = db.Column(db.String)

    def __repr__(self):
        return 'Album {}'.format(self.topic)