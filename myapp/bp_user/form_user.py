from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField, PasswordField, BooleanField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo


class UserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    submit = SubmitField('Submit')
