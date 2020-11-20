from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, SelectField, SelectField, RadioField, BooleanField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class DataForm(FlaskForm):

    """
    The form for entering values during patient encounter. Feel free to add additional 
    fields for the remaining features in the data set (features missing in the form 
    are set to default values in `predict.py`).
    """

    collection = StringField('Name of collection', validators=[DataRequired()])
    budget = IntegerField('What is the budget', validators=[NumberRange(min=0, max=100000000)])
   
    genres = StringField('Name of the genre')
    original_Language= StringField('Enter the two first numbers of the language')
    popularity = FloatField('what is the popularity of the film?')

    production_companies = StringField('Name of the production_companies')
    production_countries = StringField('Name of the production countries')
    
    release_date = StringField('Release date -> dd/mm/yy')
    cast = StringField('Id and Names of the cast')

    runtime = FloatField('Runtime of the movie')

    spoken_language = StringField('What language is the movie in?')

    submit = SubmitField('Submit')
