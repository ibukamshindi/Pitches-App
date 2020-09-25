from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField
from wtforms.validators import Required, Email, EqualTo
from ..models import User
from wtforms import ValidationError


class UpdateProfile(FlaskForm):
    bio = TextAreaField('ABOUT YOU', validators=[Required()])
    submit = SubmitField('SUBMIT')


class PitchForm(FlaskForm):
    category_id = SelectField('Which category best suits your new post?', choices=[('1', 'Promotions'), ('2', 'Pick-up Lines'), ('3', 'Interview')])
    content = TextAreaField('YOUR PITCH')
    submit = SubmitField('SUBMIT')


class CommentForm(FlaskForm):
    comment_id = TextAreaField('WRITE COMMENT')
    submit = SubmitField('SUBMIT')