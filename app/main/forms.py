from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required

class PitchForm(FlaskForm):
    title = StringField('Pitch Title', validators = [Required()])
    post = TextAreaField('Your Pitch', validators = [Required()])
    submit = SubmitField('Submit')

class ReviewForm(FlaskForm):
    review = TextAreaField('Your Review or Comments', validators = [Required()])
    submit = SubmitField('Submit')
