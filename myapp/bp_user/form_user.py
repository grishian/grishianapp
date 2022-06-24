from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField, PasswordField, BooleanField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo

class UserForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    submit = SubmitField('Submit')
