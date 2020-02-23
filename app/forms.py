from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class ProjectForm(FlaskForm):
    topic = StringField('Topic', validators=[DataRequired()])
    name = StringField('Name in Database', validators=[DataRequired()])    
    timestamp = DateField('Start on (format<%Y-%m-%d>)', validators=[DataRequired()])   # format<%Y-%m-%d>
    timespan = IntegerField('Span (weeks)', validators=[DataRequired()])     # weeks
    description = TextAreaField('Description')
    submit = SubmitField('Upload')


class CollectionForm(FlaskForm):
    topic = StringField('Topic', validators=[DataRequired()])
    name = StringField('Name in Database', validators=[DataRequired()])
    timestamp = DateField('Start On (format<%Y-%m-%d>)', validators=[DataRequired()])     # format<%Y-%m-%d>
    description = TextAreaField('Description')
    submit = SubmitField('Upload')


class AlbumForm(FlaskForm):
    topic = StringField('Topic', validators=[DataRequired()])
    name = StringField('Name in Database', validators=[DataRequired()])
    timestamp = DateField('Start On (format<%Y-%m-%d>)', validators=[DataRequired()])     # format<%Y-%m-%d>
    description = TextAreaField('Description')
    submit = SubmitField('Upload')